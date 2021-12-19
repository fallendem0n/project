import player
import exchange
import net
import localeInfo
import chat
import item

import ui
import mouseModule
import uiPickMoney
import wndMgr
import app
if app.__ENABLE_NEW_OFFLINESHOP__:
	import uiOfflineShop
###################################################################################################
## Exchange
class ExchangeDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.TitleName = 0
		self.tooltipItem = 0
		self.xStart = 0
		self.yStart = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		PythonScriptLoader = ui.PythonScriptLoader()
		PythonScriptLoader.LoadScriptFile(self, "UIScript/exchangedialog.py")

		## Owner
		self.OwnerSlot = self.GetChild("Owner_Slot")
		self.OwnerSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectOwnerEmptySlot))
		self.OwnerSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectOwnerItemSlot))
		self.OwnerSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInOwnerItem))
		self.OwnerSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.OwnerMoney = self.GetChild("Owner_Money_Value")
		self.OwnerAcceptLight = self.GetChild("Owner_Accept_Light")
		self.OwnerAcceptLight.Disable()
		self.OwnerMoneyButton = self.GetChild("Owner_Money")
		self.OwnerMoneyButton.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))
		if app.ENABLE_CHEQUE_SYSTEM and app.ENABLE_NEW_EXCHANGE_WINDOW:
			self.OwnerChequeIcon = self.GetChild("Owner_Cheque_Icon")
		if app.ENABLE_CHEQUE_SYSTEM:
			self.OwnerCheque = self.GetChild("Owner_Cheque_Value")
			self.OwnerChequeButton = self.GetChild("Owner_Cheque")
			self.OwnerChequeButton.SetEvent(ui.__mem_func__(self.OpenPickChequeDialog))

		## Target
		self.TargetSlot = self.GetChild("Target_Slot")
		self.TargetSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInTargetItem))
		self.TargetSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.TargetMoney = self.GetChild("Target_Money_Value")
		if app.ENABLE_CHEQUE_SYSTEM:
			self.TargetCheque = self.GetChild("Target_Cheque_Value")
		if app.ENABLE_CHEQUE_SYSTEM and app.ENABLE_NEW_EXCHANGE_WINDOW:
			self.TargetChequeIcon = self.GetChild("Target_Cheque_Icon")
		self.TargetAcceptLight = self.GetChild("Target_Accept_Light")
		self.TargetAcceptLight.Disable()

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
		dlgPickMoney.SetTitleName(localeInfo.EXCHANGE_MONEY)
		dlgPickMoney.SetMax(7)
		if app.ENABLE_CHEQUE_SYSTEM:
			dlgPickMoney.SetMaxCheque(3)
		dlgPickMoney.Hide()
		self.dlgPickMoney = dlgPickMoney

		## Button
		self.AcceptButton = self.GetChild("Owner_Accept_Button")
		self.AcceptButton.SetToggleDownEvent(ui.__mem_func__(self.AcceptExchange))

		self.TitleName = self.GetChild("TitleName")
		self.GetChild("TitleBar").SetCloseEvent(net.SendExchangeExitPacket)

	def Destroy(self):
		print "---------------------------------------------------------------------------- DESTROY EXCHANGE"
		self.ClearDictionary()
		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0
		self.OwnerSlot = 0
		self.OwnerMoney = 0
		self.OwnerAcceptLight = 0
		self.OwnerMoneyButton = 0
		if app.ENABLE_CHEQUE_SYSTEM and app.ENABLE_NEW_EXCHANGE_WINDOW:
			self.OwnerChequeIcon = 0
		self.TargetSlot = 0
		self.TargetMoney = 0
		self.TargetAcceptLight = 0
		self.TitleName = 0
		self.AcceptButton = 0
		self.tooltipItem = 0

	def OpenDialog(self):
		import constInfo
		constInfo.shop_acik_bro = 1
		if app.ENABLE_LEVEL_IN_TRADE:
			self.TitleName.SetText(localeInfo.EXCHANGE_TITLE % (exchange.GetNameFromTarget(), exchange.GetLevelFromTarget()))
		else:
			self.TitleName.SetText(localeInfo.EXCHANGE_TITLE % (exchange.GetNameFromTarget()))
		self.AcceptButton.Enable()
		self.AcceptButton.SetUp()
		self.Show()

		(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()

	def CloseDialog(self):
		import constInfo
		constInfo.shop_acik_bro = 0
		wndMgr.OnceIgnoreMouseLeftButtonUpEvent()

		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		self.dlgPickMoney.Close()
		self.Hide()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OpenPickMoneyDialog(self):

		if exchange.GetElkFromSelf() > 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANT_EDIT_MONEY)
			return

		if app.ENABLE_CHEQUE_SYSTEM:
			self.dlgPickMoney.Open(player.GetElk(),player.GetCheque())
			self.dlgPickMoney.SetFocus(0)
		else:
			self.dlgPickMoney.Open(player.GetElk())

	if app.ENABLE_CHEQUE_SYSTEM:
		def OpenPickChequeDialog(self):
			if exchange.GetChequeFromSelf() > 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANT_EDIT_MONEY)
				return
			self.dlgPickMoney.Open(player.GetElk(),player.GetCheque())
			self.dlgPickMoney.SetFocus(1)

		def OnPickMoney(self, money, cheque):
			if exchange.GetChequeFromSelf() <=0:
				net.SendExchangeChequeAddPacket(cheque)
			if exchange.GetElkFromSelf() <= 0:
				net.SendExchangeElkAddPacket(money)
	else:
		def OnPickMoney(self, money):
			net.SendExchangeElkAddPacket(money)

	def AcceptExchange(self):
		net.SendExchangeAcceptPacket()
		self.AcceptButton.Disable()

	def SelectOwnerEmptySlot(self, SlotIndex):

		if False == mouseModule.mouseController.isAttached():
			return

		if mouseModule.mouseController.IsAttachedMoney():
			net.SendExchangeElkAddPacket(mouseModule.mouseController.GetAttachedMoneyAmount())
		else:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			if (player.SLOT_TYPE_INVENTORY == attachedSlotType
				or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType):

				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
				SrcSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
				DstSlotNumber = SlotIndex
				if app.__ENABLE_NEW_OFFLINESHOP__:
					if uiOfflineShop.IsBuildingShop() and uiOfflineShop.IsSaleSlot(attachedInvenType, mouseModule.mouseController.GetAttachedSlotNumber()):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OFFLINESHOP_CANT_SELECT_ITEM_DURING_BUILING)
						return
				itemID = player.GetItemIndex(attachedInvenType, SrcSlotNumber)
				item.SelectItem(itemID)

				if item.IsAntiFlag(item.ANTIFLAG_GIVE):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
					mouseModule.mouseController.DeattachObject()
					return

				net.SendExchangeItemAddPacket(attachedInvenType, SrcSlotNumber, DstSlotNumber)
			if app.ENABLE_SPECIAL_STORAGE:
				if player.SLOT_TYPE_UPGRADE_INVENTORY == attachedSlotType or\
					player.SLOT_TYPE_BOOK_INVENTORY == attachedSlotType or\
					player.SLOT_TYPE_STONE_INVENTORY == attachedSlotType:
					attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
					SrcSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
					DstSlotNumber = SlotIndex

					itemID = player.GetItemIndex(attachedSlotType, SrcSlotNumber)
					item.SelectItem(itemID)

					if item.IsAntiFlag(item.ANTIFLAG_GIVE):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
						mouseModule.mouseController.DeattachObject()
						return

					for i in xrange(2):
						isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(i)
						
						if slotIndex == SrcSlotNumber and isActivated == True:
							chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE_LOCKED_ITEM)
							mouseModule.mouseController.DeattachObject()
							return

					if player.IsEquipmentSlot(SrcSlotNumber):
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE_EQUIPPED_ITEMS)
						mouseModule.mouseController.DeattachObject()
						return

					if player.GetItemSealDate(attachedInvenType, SrcSlotNumber) == item.E_SEAL_DATE_UNLIMITED_TIMESTAMP:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE_SEALED_ITEMS)
						mouseModule.mouseController.DeattachObject()
						return

					if player.GetItemSealDate(attachedInvenType, SrcSlotNumber) > 0:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE_SEALED_ITEMS)
						mouseModule.mouseController.DeattachObject()
						return

					if player.IsBasicItem(attachedInvenType, SrcSlotNumber) == True:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE_BASIC_ITEMS)
						mouseModule.mouseController.DeattachObject()
						return

					net.SendExchangeItemAddPacket(attachedInvenType, SrcSlotNumber, DstSlotNumber)

		mouseModule.mouseController.DeattachObject()

	def SelectOwnerItemSlot(self, SlotIndex):

		if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():

			money = mouseModule.mouseController.GetAttachedItemCount()
			net.SendExchangeElkAddPacket(money)

	def RefreshOwnerSlot(self):
		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			itemIndex = exchange.GetItemVnumFromSelf(i)
			itemCount = exchange.GetItemCountFromSelf(i)
			if 1 == itemCount:
				itemCount = 0
			self.OwnerSlot.SetItemSlot(i, itemIndex, itemCount)
		self.OwnerSlot.RefreshSlot()

	def RefreshTargetSlot(self):
		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			itemIndex = exchange.GetItemVnumFromTarget(i)
			itemCount = exchange.GetItemCountFromTarget(i)
			if 1 == itemCount:
				itemCount = 0
			self.TargetSlot.SetItemSlot(i, itemIndex, itemCount)
		self.TargetSlot.RefreshSlot()

	def Refresh(self):

		self.RefreshOwnerSlot()
		self.RefreshTargetSlot()

		if app.ENABLE_CHEQUE_SYSTEM:
			self.OwnerMoney.SetText(localeInfo.NumberToGoldNotText(exchange.GetElkFromSelf()))
			self.TargetMoney.SetText(localeInfo.NumberToGoldNotText(exchange.GetElkFromTarget()))

			self.OwnerCheque.SetText(str(exchange.GetChequeFromSelf()))
			self.TargetCheque.SetText(str(exchange.GetChequeFromTarget()))
		else:
			self.OwnerMoney.SetText(str(exchange.GetElkFromSelf()))
			self.TargetMoney.SetText(str(exchange.GetElkFromTarget()))

		if True == exchange.GetAcceptFromSelf():
			self.OwnerAcceptLight.Down()
		else:
			self.AcceptButton.Enable()
			self.AcceptButton.SetUp()
			self.OwnerAcceptLight.SetUp()

		if True == exchange.GetAcceptFromTarget():
			self.TargetAcceptLight.Down()
		else:
			self.TargetAcceptLight.SetUp()

	def OverInOwnerItem(self, slotIndex):

		if 0 != self.tooltipItem:
			self.tooltipItem.SetExchangeOwnerItem(slotIndex)

	def OverInTargetItem(self, slotIndex):

		if 0 != self.tooltipItem:
			self.tooltipItem.SetExchangeTargetItem(slotIndex)

	def OverOutItem(self):

		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OnTop(self):
		self.tooltipItem.SetTop()

	def OnUpdate(self):

		USE_EXCHANGE_LIMIT_RANGE = 1000

		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xStart) > USE_EXCHANGE_LIMIT_RANGE or abs(y - self.yStart) > USE_EXCHANGE_LIMIT_RANGE:
			(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()
			net.SendExchangeExitPacket()

import ui
import player
import mouseModule
import net
import app
import snd
import item
import chat
import uiScriptLocale
import uiCommon
import uiPickMoney
import localeInfo
import constInfo
import translate
import uiToolTip

BILGI_AL = [
	"Neslereri s�r�kleyerek ekleyebilirsiniz.",
	"Silmekten vazge�ti�iniz nesnenin �st�ne t�klayarak kald�rabilirsiniz.",
]

class DeleteItem(ui.ScriptWindow):
	def __init__(self):	
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()
		self.itemStock = {}
		self.tooltipItem = None
		self.itemDropQuestionDialog = None
		self.bilgialbuton = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/DeleteItem.py")
		except:
			import exception
			exception.Abort("OfflineShopBuilderWindow.LoadWindow.LoadObject")
			
		try:
			self.itemSlot = self.GetChild("ItemSlot")
			self.btnOk = self.GetChild("OkButton")
			self.btnSat = self.GetChild("SatButton")
			self.btnClose = self.GetChild("CloseButton")
			self.btnIptal = self.GetChild("VazgecButton")
			self.board = self.GetChild("Board")
			self.bilgialbuton = self.GetChild("bilgialkardes")
		except:
			import exception
			exception.Abort("OfflineShopBuilderWindow.LoadWindow.BindObject")
			
		self.btnOk.SetEvent(ui.__mem_func__(self.OnOk))
		self.btnSat.SetEvent(ui.__mem_func__(self.OnSat))
		self.btnClose.SetEvent(ui.__mem_func__(self.Temizle))
		self.board.SetCloseEvent(ui.__mem_func__(self.OnClose))
		self.btnIptal.SetEvent(ui.__mem_func__(self.OnClose))
		
		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.OnSelectEmptySlot))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.itemSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.OnSelectItemSlot))
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OnOverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		
		self.bilgialbuton.SetToolTipWindow2(self.__ToolTipOlustur("Bilgilendirme", BILGI_AL))
	
	def Destroy(self):
		self.ClearDictionary()
		
		self.itemSlot = None
		self.btnOk = None
		self.btnSat = None
		self.btnClose = None
		self.board = None
		self.itemDropQuestionDialog = None
		self.bilgialbuton = None

	def Open(self):
		self.Temizle()
		self.SetCenterPosition()
		self.Refresh()
		self.Show()

	def Close(self):
		self.itemStock = {}
		self.Hide()

	def Temizle(self):
		self.itemStock = {}
		self.Refresh()

	def __ToolTipOlustur(self, title, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(title)

		for desc in descList:
			toolTip.AutoAppendTextLine(desc)

		toolTip.AlignHorizonalCenter()
		toolTip.SetTop()
		return toolTip

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def Refresh(self):
		for i in xrange(60):
			if (not self.itemStock.has_key(i)):
				self.itemSlot.ClearSlot(i)
				continue

			pos = self.itemStock[i]
			itemCount = player.GetItemCount(*pos)
			if (itemCount <= 1):
				itemCount = 0
			self.itemSlot.SetItemSlot(i, player.GetItemIndex(*pos), itemCount)

		self.itemSlot.RefreshSlot()

	def OnSelectEmptySlot(self, selectedSlotPos):

		isAttached = mouseModule.mouseController.isAttached()
		if (isAttached):
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			mouseModule.mouseController.DeattachObject()

			if app.ENABLE_SPECIAL_STORAGE:
				if player.SLOT_TYPE_INVENTORY != attachedSlotType and \
					player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType and \
					player.SLOT_TYPE_UPGRADE_INVENTORY != attachedSlotType and \
					player.SLOT_TYPE_BOOK_INVENTORY != attachedSlotType and \
					player.SLOT_TYPE_STONE_INVENTORY != attachedSlotType:
					return
			else:
				if (player.SLOT_TYPE_INVENTORY != attachedSlotType and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedSlotType):
					return

			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

			itemVNum = player.GetItemIndex(attachedInvenType, attachedSlotPos)
			item.SelectItem(itemVNum)

			attrSlot = [player.GetItemAttribute(attachedSlotPos, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
			if int(attachedSlotPos) > 180:
				self.uyari2 = uiCommon.PopupDialog()
				self.uyari2.SetText("Giyili itemleri silemessin.")
				self.uyari2.Open()
				return

			self.itemStock[selectedSlotPos] = (attachedInvenType, attachedSlotPos)
			self.Refresh()


	def OnSelectItemSlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if (isAttached):
			snd.PlaySound("sound/ui/loginfail.wav")
			mouseModule.mouseController.DeattachObject()

		else:
			if (not selectedSlotPos in self.itemStock):
				return

			invenType, invenPos = self.itemStock[selectedSlotPos]
			del self.itemStock[selectedSlotPos]
			self.Refresh()

	def OnOk(self):
		if (len(self.itemStock) == 0):
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Silinecek nesne yok.")
			return

		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText("Se�ilen (|cffFDD017|h%d Adet|h|r) nesneyi silmek istiyor musun?" % (len(self.itemStock)))
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
		itemDropQuestionDialog.Open()
		self.itemDropQuestionDialog = itemDropQuestionDialog

	def OnSat(self):
		if (len(self.itemStock) == 0):
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Sat�lacak nesne yok.")
			return

		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText("Se�ilen (|cffFDD017|h%d Adet|h|r) nesneyi satmak istiyor musun?" % (len(self.itemStock)))
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestSellItem(arg))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestSellItem(arg))
		itemDropQuestionDialog.Open()
		self.itemDropQuestionDialog = itemDropQuestionDialog

	def Sil(self):
		for privatePos, (itemWindowType, itemSlotIndex) in self.itemStock.items():

			net.SendItemDeletePacket(itemSlotIndex, itemWindowType)
			del self.itemStock[privatePos]

			self.Refresh()

	def Sat(self):
		for privatePos, (itemWindowType, itemSlotIndex) in self.itemStock.items():

			net.SendItemSellPacket(itemSlotIndex, itemWindowType)
			del self.itemStock[privatePos]

			self.Refresh()

	def RequestDropItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			self.Sil()

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

	def RequestSellItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			self.Sat()

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None


	def OnClose(self):
		self.Close()
		
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnOverInItem(self, slotIndex):
		if (self.tooltipItem):
			if (self.itemStock.has_key(slotIndex)):
				self.tooltipItem.SetDeleteItem(*self.itemStock[slotIndex] + (slotIndex,))

	def OnOverOutItem(self):
		if (self.tooltipItem):
			self.tooltipItem.HideToolTip()

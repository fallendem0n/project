import ui
import uiToolTip
import item
import net
import mouseModule
import player
import constInfo

class KygnItemSil(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Ekran()
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

	def __Initialize(self):
		self.SlotArray = []
		self.VnumArray = []

	def __Ekran(self):
		KygnPyYukle = ui.PythonScriptLoader()
		KygnPyYukle.LoadScriptFile(self, "UIScript/kygnitemsil.py")

		KygnObject = self.GetChild
		self.titleBar = KygnObject("titlebar")
		self.ItemSlot = KygnObject("itemslot")
		self.ItemSilmeButonu = KygnObject("ItemSilmeButonu")


		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close2))
		self.ItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.ItemSlot.SetOverInItemEvent(ui.__mem_func__(self.__OnOverInItem))
		self.ItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OnOverOutItem))
		self.ItemSilmeButonu.SetEvent(ui.__mem_func__(self.__Button))

	def __Button(self):
		net.SendChatPacket("/remove_item_system_button")
		for i in xrange(len(self.SlotArray)):
			self.ItemSlot.ClearSlot(self.SlotArray[i])

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			self.PutSocket(selectedSlotPos, attachedSlotPos)
			mouseModule.mouseController.DeattachObject()

	def InventoryRightClick(self, NewItemIndex):
		for i in xrange(59):
			if i not in self.SlotArray:
				self.PutSocket(i, NewItemIndex)
				break

	def __OnOverInItem(self, slotIndex):
		self.tooltipItem.ClearToolTip()
		for i in xrange(len(self.SlotArray)):
			if slotIndex == self.SlotArray[i]:
				self.tooltipItem.SetInventoryItem(self.VnumArray[i])

	def __OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def PutSocket(self, PutNewSlot, NewItemSlot):
		if NewItemSlot not in self.VnumArray:
			item.SelectItem(NewItemSlot)
			sizeX, sizeY = item.GetItemSize()
			if sizeY == 3:
				self.SlotArray += [int(PutNewSlot)]
				self.SlotArray += [int(PutNewSlot + 10)]
				self.SlotArray += [int(PutNewSlot + 20)]
			elif sizeY == 2:
				self.SlotArray += [int(PutNewSlot)]
				self.SlotArray += [int(PutNewSlot + 10)]
			else:
				self.SlotArray += [int(PutNewSlot)]
			self.ItemSlot.SetItemSlot(PutNewSlot, player.GetItemIndex(player.INVENTORY, NewItemSlot), player.GetItemCount(player.INVENTORY, NewItemSlot))
			self.VnumArray += [int(NewItemSlot)]
			net.SendChatPacket("/add_remove_item_index %d" % int(NewItemSlot))
		else:
			return

	def Show(self):
		ui.ScriptWindow.Show(self)

	def OnPressEscapeKey(self):
		self.Close2()
		return True

	def OnUpdate(self):
		self.ItemSlot.RefreshSlot()

	def Close(self):
		self.Hide()

	def Close2(self):
		net.SendChatPacket("/remove_item_system_close")
		constInfo.ITEM_REMOVE_WINDOW_STATUS = 0
		self.SlotArray = []
		self.VnumArray = []
		self.tooltipItem = None
		self.Hide()

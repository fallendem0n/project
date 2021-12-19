import app
import ui
import uiScriptLocale
import uiTooltip
import mouseModule
import constInfo
import localeInfo
import chat
import net
import player
import dbg
import background


class BlackMarket(ui.ScriptWindow):
	class SearchResultItem(ui.Window):

		def __init__(self, parent, index):
			ui.Window.__init__(self)
			
			self.parent = parent
			
			self.isLoad = True
			self.isSelected = False
			
			self.index = index
			


			self.SetParent(parent)
			self.InitItem()

			
		def InitItem(self):
			startX = 5
			yPos = -2
			
			self.bmImage = ui.ThinBoardCircle()
			self.bmImage.SetParent(self)
			self.bmImage.SetSize(210,40)
			self.bmImage.SetPosition(startX,yPos)
			self.bmImage.Show()
			
			
			
			self.wonslot = ui.MakeImageBox(self, "d:/ymir work/ui/public/cheque_slot.sub", 3, yPos+2)
			self.wonslot.SetTop()
			self.wonslot.SetParent(self.bmImage)
			self.wonslot.SetPosition(62, 10)
			self.wonslot.Show()
			
			self.wonicon = ui.MakeImageBox(self, "d:/ymir work/ui/game/windows/cheque_icon.sub", 3, yPos+2)
			self.wonicon.SetTop()
			self.wonicon.SetParent(self.wonslot)
			self.wonicon.SetPosition(-20, 3)
			self.wonicon.Show()
			
			self.won = ui.TextLine()
			self.won.SetParent(self.wonslot)
			self.won.SetPosition(2, 2)
			self.won.Show()
			
			self.moneyslot = ui.MakeImageBox(self, "d:/ymir work/ui/public/gold_slot.sub", 3, yPos+2)
			self.moneyslot.SetTop()
			self.moneyslot.SetParent(self.bmImage)
			self.moneyslot.SetPosition(112, 10)
			self.moneyslot.Show()
			
			self.moneyicon = ui.MakeImageBox(self, "d:/ymir work/ui/game/windows/money_icon.sub", 3, yPos+2)
			self.moneyicon.SetTop()
			self.moneyicon.SetParent(self.moneyslot)
			self.moneyicon.SetPosition(-20, 3)
			self.moneyicon.Show()
			
			self.yang = ui.TextLine()
			self.yang.SetParent(self.moneyslot)
			self.yang.SetPosition(2, 2)
			self.yang.Show()
			
			self.slot = ui.SlotWindow()
			self.slot.SetParent(self.bmImage)
			self.slot.SetPosition(3, 3)
			self.slot.SetSlotBaseImage("d:/ymir work/ui/public/Slot_Base.sub", 1.0, 1.0, 1.0, 1.0)
			self.slot.AppendSlot(0, 0, 0, 32, 32)
			self.slot.RefreshSlot()
			self.slot.Show()

						
			self.SetSize(self.bmImage.GetWidth(), self.bmImage.GetHeight())
			

			
		def SetWonText(self, name):
			self.won.SetText(name)

		def SetYangText(self, count):
			self.yang.SetText(localeInfo.NumberToMoneyString(str(count)))
			
		def SetItemImage(self, vnum):
			self.slot.SetItemSlot(0, int(vnum),0)


		def Select(self):

			self.isSelected = True
			self.isLoad = True

		def UnSelect(self):
			self.isSelected = False
			self.isLoad = True




	def __init__(self):
		ui.ScriptWindow.__init__(self)
		

		
		
		self.selectedItemIndex = -1
		self.board = None
		self.tooltipItem = None

		self.searchResultItems = []

		self.information = {}
		
		self.currentPage = 1
		self.pageCount = 1
		self.perPage = 9
		self.itemCount = 0
		self.timerdone = 0
		self.timer = 0
		self.interface = 0
		self.won = 0
		self.yang = 0
		
		self.LoadWindow()
		
		
	def Destroy(self):
		self.ClearDictionary()
		self.searchResultItems[:] = [] 
		self.titleBar = None
		self.questScrollBar = None
		self.questShowingStartIndex = None
		self.tooltipItem = None
		self.interface = 0
		self.information = {}
		self.timerdone = 0
		self.timer = 0
		self.won = 0
		self.yang = 0
		



	def __del__(self):
		self.Destroy()
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/blackmarket.py")
		except:
			import exception
			exception.Abort("BlackMarket.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.RefreshSymbol = GetObject("RefreshSymbol")
			self.itemslot = self.GetChild("itemslot")
			self.won_text = self.GetChild("won_text")
			self.gold_text = self.GetChild("gold_text")
			self.submit = self.GetChild("submit")
			self.questScrollBar = self.GetChild("info_ScrollBar")
			self.questShowingStartIndex = 0
			self.questScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
			
			self.board.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
			# self.SetOnRunMouseWheelEvent(self.OnQuestScroll2)

		except:
			import exception
			exception.Abort("BlackMarket.LoadDialog.BindObject")
			
			
			
		self.submit.SetEvent(ui.__mem_func__(self.Submit))
			
			
		self.itemslot.SetUnselectItemSlotEvent(self.OnUseItemSlot)
		self.itemslot.SetSelectItemSlotEvent(self.OnUseItemSlot)
		self.itemslot.SetUseSlotEvent(self.OnUseItemSlot)
		self.itemslot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemslot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.itemslot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
			

	
	
	def Submit(self):
		for key, info in self.information.iteritems():
			net.SendItemBlackMarketPacket(info[4], info[3])
			
		self.information = {}
		for i in range(self.itemslot.GetSlotCount()):
			self.itemslot.ClearSlot(i)
			self.itemslot.RefreshSlot()
		
		self.yang = 0
		self.won = 0
		self.gold_text.SetText(localeInfo.NumberToMoneyString(str(self.yang)))
		self.won_text.SetText(str(self.won))
	
	
	def IsInList(self, pos):
		(inv_type, inv_pos) = pos
		for key, info in self.information.iteritems():
			if (info and info[3] == inv_type and info[4] == inv_pos):
				return True
		return False
	
	
	def __OnSelectEmptySlot(self, selectedSlotPos):
		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

			itemIndex = player.GetItemIndex(attachedInvenType, attachedSlotPos)
			itemCount = player.GetItemCount(attachedInvenType, attachedSlotPos)
			mouseModule.mouseController.DeattachObject()
			
			canpass = 0
			
			if player.IsEquipmentSlot(attachedInvenType, attachedSlotPos):
				return

			if self.IsInList((attachedInvenType, attachedSlotPos)):
				return
				
			for i in range(len(constInfo.blackmarket)):
				if int(constInfo.blackmarket[i].split("#")[1]) == itemIndex:
					canpass = 1
					
			if canpass == 0:
				return				
				

			details = [ selectedSlotPos, itemIndex, itemCount, attachedInvenType, attachedSlotPos ]
			self.information[selectedSlotPos] = details
			self.RefreshGain(itemIndex,itemCount,0)
			self.SetBuildItem(selectedSlotPos, itemIndex, itemCount)
	
	
	def OnUseItemSlot(self, slotIndex):
		if self.information.has_key(slotIndex):
			self.RefreshGain(self.information[slotIndex][1],self.information[slotIndex][2],1)
			self.SetBuildItem(self.information[slotIndex][0], 0, 0)
			del self.information[slotIndex]


	def OverInItem(self, slot):
		if not self.tooltipItem:
			return

		self.tooltipItem.ClearToolTip()
		if self.information.has_key(slot):
			details = self.information[slot]
			self.tooltipItem.SetInventoryItem(details[4], details[3])


	def OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
			
			
	def RefreshGain(self, index, count, islem):
		if index != 0:
			won = 0
			yang = 0
			
			for i in range(len(constInfo.blackmarket)):
				if int(constInfo.blackmarket[i].split("#")[1]) == int(index):
					won = int(constInfo.blackmarket[i].split("#")[2])
					yang= int(constInfo.blackmarket[i].split("#")[3])
					
					
			if islem == 0:
				self.won = int(self.won+(won*(int(count))))
				self.yang = int(self.yang+(yang*(int(count))))
			else:
				self.won = int(self.won-(won*(int(count))))
				self.yang = int(self.yang-(yang*(int(count))))
			
			self.gold_text.SetText(localeInfo.NumberToMoneyString(str(self.yang)))
			self.won_text.SetText(str(self.won))
	
			
			
	def SetBuildItem(self, selectedSlotPos, itemIndex, itemCount):
		if int(itemIndex) == 0:
			self.itemslot.ClearSlot(selectedSlotPos)
			self.itemslot.RefreshSlot()
		else:
			self.itemslot.SetItemSlot(selectedSlotPos, itemIndex, itemCount)
			
	def BindInterface(self, interface):
		self.interface = interface

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

		
	def OnQuestScroll2(self, len):
		if str(len) == "True":
			self.questScrollBar.OnDown()
		else:
			self.questScrollBar.OnUp()
		
	def OnQuestScroll(self):
		questCount = len(constInfo.blackmarket)
		scrollLineCount = max(0, questCount - 8)
		startIndex = int(scrollLineCount * self.questScrollBar.GetPos())

		if startIndex != self.questShowingStartIndex:
			self.questShowingStartIndex = startIndex
			self.RefreshInfo()

		
	def RefreshInfo(self):
		questCount = len(constInfo.blackmarket)
		
		aralik = 8
		if questCount < 8:
			aralik = questCount
		
		if questCount > 0:
			
			questRange = range(aralik)
			self.searchResultItems[:] = []
			
			if questCount > 8:
				self.questScrollBar.Show()
			else:
				self.questScrollBar.Hide()

			
			
			basePos = 45
			for i in range(0+self.questShowingStartIndex, aralik+self.questShowingStartIndex):
				resultItem = BlackMarket.SearchResultItem(self, i)
				resultItem.SetPosition(20, basePos+((i-self.questShowingStartIndex)*43))
				resultItem.SetWonText(constInfo.blackmarket[i].split("#")[2])
				resultItem.SetYangText(constInfo.blackmarket[i].split("#")[3])
				resultItem.SetItemImage(constInfo.blackmarket[i].split("#")[1])
				resultItem.Show()
				
				self.searchResultItems.append(resultItem)
			
			self.Children.append(self.searchResultItems)


			
			

	def OnUpdate(self):
		if self.timer <= app.GetTime() and self.timerdone == 0:
			self.RefreshInfo()
			self.RefreshSymbol.Hide()
			self.timerdone = 1
			
	
	def Open(self):	
		self.selectedItemIndex = -1
		self.timer = app.GetTime()+1
		self.timerdone = 0
		self.information = {}
		for i in range(self.itemslot.GetSlotCount()):
			self.itemslot.ClearSlot(i)
			self.itemslot.RefreshSlot()
		
		self.yang = 0
		self.won = 0
		self.gold_text.SetText(localeInfo.NumberToMoneyString(str(self.yang)))
		self.won_text.SetText(str(self.won))
			
		self.SetTop()
		self.SetCenterPosition()
		self.Show()
		self.RefreshSymbol.Show()

		

	
	def OnSearchResultItemSelect(self, index):
		if self.questShowingStartIndex > 0:
			self.selectedItemIndex = index - self.questShowingStartIndex
		else:
			self.selectedItemIndex = index

		map(BlackMarket.SearchResultItem.UnSelect,  self.searchResultItems)
		self.searchResultItems[self.selectedItemIndex].Select()

		

	def Close(self):
		map(BlackMarket.SearchResultItem.Hide, self.searchResultItems)
		self.Hide()


	def __OnCloseButtonClick(self):
		self.Close()

	def OnPressEscapeKey(self):
		self.Close()


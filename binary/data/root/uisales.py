import app
import ui
import uiTooltip
import constInfo
import localeInfo
import uiCommon
import net
import player
import item
import chat

class SalesClass(ui.ScriptWindow):
	class SearchResultItem(ui.Window):

		def __init__(self, parent, index, parent2):
			ui.Window.__init__(self)
			
			self.parent = parent
			self.parent2 = parent2
			self.isLoad = True
			self.isSelected = False
			self.index = index
			self.id = 0
			
			self.SetParent(parent2)
			self.InitItem()

			
		def InitItem(self):
			startX = 18
			yPos = 3
			
			self.tabimage = ui.MakeImageBox(self, "sales/normal.tga", 3, yPos+2)
			self.tabimage.SAFE_SetStringEvent("MOUSE_LEFT_UP",self.__OnSelect)
			self.tabimage.SetTop()
			self.tabimage.Show()
			
			self.title = ui.TextLine()
			self.title.SetParent(self)
			self.title.SetPosition(startX+67-75, yPos+6)
			self.title.SetFontName("Arial:12")
			self.title.Show()
			
			
			self.timer = ui.TextLine()
			self.timer.SetParent(self)
			self.timer.SetPosition(startX+67-75, yPos+18)
			self.timer.SetFontName("Arial:12")
			self.timer.Show()
			

						
			self.SetSize(self.tabimage.GetWidth(), self.tabimage.GetHeight())
			

			
		def SetQuestName(self, name):
			self.title.SetText(name)
			
		def SetID(self, id):
			self.id = int(id)

		def SetTimerText(self, time):
			self.timer.SetText(time)
			
				

		
		
		def __OnSelect(self):
			self.parent.OnSearchResultItemSelect(self.index)

		def Select(self):

			self.isSelected = True
			self.isLoad = True

		def UnSelect(self):
			self.isSelected = False
			self.isLoad = True
			


		def OnUpdate(self):
			sure = int(constInfo.SalesList[int(self.index)]["time"])
			tip = int(constInfo.SalesList[int(self.index)]["type"])

			sure = sure-app.GetGlobalTimeStamp()
			
			
			
			if sure > 0:
				if tip > 0:
					self.title.SetText("Teklif "+str(self.id)+" "+ constInfo.sarirenk+" Teklif henüz baþlamadý! ")
					self.SetTimerText(constInfo.sarirenk + localeInfo.CalcTimeWithLetter(sure))
				else:
					self.title.SetText("Teklif "+str(self.id)+" "+ constInfo.yesilrenk+" Teklif devam ediyor! ")
					self.SetTimerText(constInfo.yesilrenk +localeInfo.CalcTimeWithLetter(sure))
			else:
				if tip > 0:
					sure = sure+(tip*60*60)
					if sure > 0:
						self.title.SetText("Teklif "+str(self.id)+" "+ constInfo.yesilrenk+" Teklif devam ediyor! ")
						self.SetTimerText(constInfo.yesilrenk +localeInfo.CalcTimeWithLetter(sure))
					else:
						self.title.SetText("Teklif "+str(self.id))
						self.SetTimerText(constInfo.kirmizirenk + "Teklifin süresi doldu!")
				else:
					self.title.SetText("Teklif "+str(self.id))
					self.SetTimerText(constInfo.kirmizirenk + "Teklifin süresi doldu!")
			


		def OnRender(self):
			if self.isLoad:
				if self.isSelected:
					self.tabimage.LoadImage("sales/active.tga")
				else:
					self.tabimage.LoadImage("sales/normal.tga")
					
				self.isLoad = False


	def __init__(self):
		ui.ScriptWindow.__init__(self)
		
		self.selectedItemIndex = -1
		self.board = None
		self.RefreshSymbol = None
		self.QuestionDialog = None
		self.secilen = -1
		self.id = -1

		self.searchResultItems = []

		self.itemDataList = []
		self.slotvnum = []
		
		self.timerdone = 0
		self.timer = 0
		
		self.tooltipItem = uiTooltip.ItemToolTip()
		self.tooltipItem.Hide()
		
		self.LoadWindow()
		



	def __del__(self):
		self.Destroy()
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/sales.py")
		except:
			import exception
			exception.Abort("SalesClass.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")
			self.basliktext = GetObject("basliktext")
			self.reward = GetObject("reward")
			self.scroll = self.GetChild("scroll")
			self.buy = self.GetChild("buy")
			self.fiyattext = self.GetChild("fiyattext")
			self.RefreshSymbol = GetObject("RefreshSymbol")
			self.bg2 = GetObject("bg2")
			self.bg1 = GetObject("bg1")
			self.scrollstartindex = 0
			self.buy.SetEvent(ui.__mem_func__(self.BuyEvent))
			self.scroll.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
			
			self.board.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
			# self.SetOnRunMouseWheelEvent(self.OnQuestScroll2)

		except:
			import exception
			exception.Abort("SalesClass.LoadDialog.BindObject")
			
			
		self.reward.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.reward.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		
		
	def OverOutItem(self):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.HideToolTip()
		
		
		
	def OverInItem(self, slotIndex):
		self.tooltipItem.ClearToolTip()
		if int(self.slotvnum[slotIndex]) != 0:
			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(0)
			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append((0,0))
			self.tooltipItem.AddItemData(self.slotvnum[slotIndex],metinSlot, attrSlot)
			self.tooltipItem.Show()
		else:
			self.tooltipItem.HideToolTip()
			
			



	def Destroy(self):
		self.ClearDictionary()
		self.searchResultItems[:] = [] 
		self.itemDataList[:] = [] 
		self.slotvnum[:] = [] 
		self.titleBar = None
		self.scroll = None
		self.RefreshSymbol = None
		self.board = None
		self.scrollstartindex = None
		self.QuestionDialog = None
		self.id = -1
		self.secilen = -1
		self.selectedItemIndex = -1
		self.timerdone = 0
		self.timer = 0
		

		
		
	def OnQuestScroll2(self, len):
		if str(len) == "True":
			self.scroll.OnDown()
		else:
			self.scroll.OnUp()
		
	def OnQuestScroll(self):
		salecount = len(constInfo.SalesList)
		scrollLineCount = max(0, salecount - 8)
		startIndex = int(scrollLineCount * self.scroll.GetPos())

		if startIndex != self.scrollstartindex:
			self.scrollstartindex = startIndex
			self.RefreshInfo()

		
	def RefreshInfo(self):
		salecount = len(constInfo.SalesList)
		self.searchResultItems[:] = []
		
		if salecount > 8:
			self.scroll.Show()
		else:
			self.scroll.Hide()

		count = 8
		
		if len(constInfo.SalesList) < count:
			count = len(constInfo.SalesList)
		
		basePos = 5
		for i in range(0+self.scrollstartindex, count+self.scrollstartindex):
			resultItem = SalesClass.SearchResultItem(self, i, self.bg1)
			resultItem.SetPosition(5, basePos+((i-self.scrollstartindex)*36))
			resultItem.SetID(int(constInfo.SalesList[i]["id"]))
			resultItem.Show()
			
			self.searchResultItems.append(resultItem)
		
		self.Children.append(self.searchResultItems)




	def Open(self):	
		self.selectedItemIndex = -1
		# net.SendChatPacket("/sales_list")
		self.timer = app.GetTime()+0.2
		self.timerdone = 0
		self.scroll.Hide()
		self.bg1.Hide()
		self.bg2.Hide()
		self.RefreshSymbol.Show()
		
		self.Show()
		self.SetCenterPosition()

	
	def BuyEvent(self):
		self.QuestionDialog = None
		
		QuestionDialog = uiCommon.QuestionDialog()
		QuestionDialog.SetText("Satýn almak istiyor musun?")
		QuestionDialog.SetAcceptEvent(lambda arg=True: self.Answer(arg))
		QuestionDialog.SetCancelEvent(lambda arg=False: self.Answer(arg))
		QuestionDialog.Open()
		self.QuestionDialog = QuestionDialog
		
	def Answer(self, answer):

		if not self.QuestionDialog:
			return
			
		if answer == False:
			self.QuestionDialog.Close()
			self.QuestionDialog = None
			return

		net.SendChatPacket("/sales_buy "+str(self.secilen+1))

		self.QuestionDialog.Close()
		self.QuestionDialog = None
		
		
	def OnUpdate(self):
		if self.timer <= app.GetTime() and self.timerdone == 0:
			self.RefreshInfo()
			self.RefreshSymbol.Hide()
			self.bg1.Show()
			self.bg2.Show()
			self.OnSearchResultItemSelect(0+self.scrollstartindex)
			self.timerdone = 1
		
		if self.secilen == -1:
			return
			
		if len(constInfo.SalesList) == 0:
			return
			
			
		if self.secilen-1 > len(constInfo.SalesList):
			return
		
		sure = int(constInfo.SalesList[int(self.secilen)]["time"])
		tip = int(constInfo.SalesList[int(self.secilen)]["type"])
		
		sure = sure - app.GetGlobalTimeStamp()
			
		if (sure > 0):
			if (tip > 0):
				self.basliktext.SetText("Baþlamasýna Kalan Süre : "+localeInfo.CalcTime(sure))
			else:
				self.basliktext.SetText("Kalan Süre : "+localeInfo.CalcTime(sure))
		else:
			if tip > 0:
				sure = sure+(tip*60*60)
				if sure > 0:
					self.basliktext.SetText("Kalan Süre : "+localeInfo.CalcTime(sure))
				else:
					self.basliktext.SetText("Teklifin süresi doldu!")
			else:
				self.basliktext.SetText("Teklifin süresi doldu!")
	
	
	def OnSearchResultItemSelect(self, index):
		if self.scrollstartindex > 0:
			self.selectedItemIndex = index - self.scrollstartindex
		else:
			self.selectedItemIndex = index
		self.secilen = index
		
		map(SalesClass.SearchResultItem.UnSelect,  self.searchResultItems)
		
		if len(constInfo.SalesList) == 0:
			return
		
		listcount = len(constInfo.SalesList[index]["items"][0])
		if listcount == 0:
			return
		
		self.searchResultItems[self.selectedItemIndex].Select()
		self.fiyattext.SetText(str(constInfo.SalesList[index]["normal_price"])+ " EP yerine " +str(constInfo.SalesList[index]["sales_price"])+ " EP")
				
		self.slotlist = []
		self.slotvnum = []
		
		
		for i in range(self.reward.GetSlotCount()):
			if i > listcount and not i in self.slotlist:
				# self.reward.SetSlot(i, 1, 32, 32, petskill.GetEmptySkill())
				self.reward.SetItemSlot(i, 0, 0)
				self.slotvnum.append(0)
			else:
				if i < 5 and i < listcount:
					count = int(constInfo.SalesList[index]["items"][0][i]["count"])
					vnum = int(constInfo.SalesList[index]["items"][0][i]["vnum"])
					item.SelectItem(vnum)
					(itemWidth, itemHeight) = item.GetItemSize()
					if count > 1:
						self.reward.SetItemSlot(0+i, vnum, count)
					else:
						self.reward.SetItemSlot(0+i, vnum)
					self.slotlist.append(0+i)
					if itemHeight > 1:
						self.slotlist.append(0+i+5)
					elif itemHeight > 2:
						self.slotlist.append(0+i+10)
					self.slotvnum.append(vnum)
				else:
					# if not i in self.slotlist:
						# self.reward.SetSlot(i, 1, 32, 32, petskill.GetEmptySkill())
					# else:
						# self.reward.SetItemSlot(i,0, 0)
					self.reward.SetItemSlot(i,0, 0)
						
					self.slotvnum.append(0)
			
			
				
		self.reward.RefreshSlot()
		

	def Close(self):
		map(SalesClass.SearchResultItem.Hide, self.searchResultItems)
		self.Hide()


	def __OnCloseButtonClick(self):
		map(SalesClass.SearchResultItem.Hide, self.searchResultItems)
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()


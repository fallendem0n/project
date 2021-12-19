import ui
import localeInfo
import app
import ime
import uiScriptLocale

class ItemQuestionDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()
		
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.toolTip = uiToolTip.ToolTip()
		
		self.window_type = 0
		self.count = 0
	
		self.dropType = 0
		self.dropCount = 0
		self.dropNumber = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

		self.titleBar = ui.TitleBar()
		self.titleBar.SetParent(self.board)
		self.titleBar.MakeTitleBar(244, "yellow")
		self.titleBar.SetPosition(8, 7)
		self.titleBar.Show()

		self.titleName = ui.TextLine()
		self.titleName.SetParent(self.titleBar)
		self.titleName.SetPosition(0, 4)
		self.titleName.SetWindowHorizontalAlignCenter()
		self.titleName.SetHorizontalAlignCenter()
		self.titleName.Show()

		self.slotList = []
		for i in xrange(3):
			slot = ui.ImageBox()
			slot.LoadImage("d:/ymir work/ui/public/slot_base.sub")
			slot.SetParent(self)
			slot.SetWindowHorizontalAlignCenter()
			self.slotList.append(slot)

	def Open(self, vnum, slot = None, price = None):
		item.SelectItem(vnum)
		xSlotCount, ySlotCount = item.GetItemSize()

		try:
			if self.window_type == "inv":
				metinSlot = [player.GetItemMetinSocket(player.INVENTORY, slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			elif self.window_type == "shop":
				metinSlot = [shop.GetItemMetinSocket(slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		except:
			pass

		if vnum in (50300, 70037):
			self.titleName.SetText("%s %s" % (skill.GetSkillName(metinSlot[0]), item.GetItemName()))
		elif vnum == 70104:
			self.titleName.SetText("%s %s" % (nonplayer.GetMonsterName(metinSlot[0]), item.GetItemName()))
		else:
			self.titleName.SetText(item.GetItemName())

		newHeight = 0	
			
		if price:
			newHeight = 20
		
			itemPrice = ui.TextLine()
			itemPrice.SetPosition(0, 77 + 32*ySlotCount)
			itemPrice.SetWindowHorizontalAlignCenter()
			itemPrice.SetHorizontalAlignCenter()
			itemPrice.SetVerticalAlignCenter()
			itemPrice.SetParent(self.board)
			if str(price).isdigit():
				itemPrice.SetText(localeInfo.NumberToMoneyString(price))
			else:
				itemPrice.SetText(price)
			itemPrice.Show()
			self.itemPrice = itemPrice

		slotGrid = ui.SlotWindow()
		slotGrid.SetParent(self)
		slotGrid.SetPosition(-16, 62)
		slotGrid.SetWindowHorizontalAlignCenter()
		slotGrid.AppendSlot(0, 0, 0, 32*xSlotCount, 32*ySlotCount)
		slotGrid.AddFlag("not_pick")
		slotGrid.Show()
		self.slotGrid = slotGrid

		if self.count > 1 and vnum != 1:
			self.slotGrid.SetItemSlot(0, vnum, self.count)
		else:
			self.slotGrid.SetItemSlot(0, vnum)
				
		self.SetSize(260, 110 + 32*ySlotCount + newHeight)
		self.board.SetSize(260, 110 + 32*ySlotCount + newHeight)
		self.textLine.SetPosition(0, 44)

		for i in xrange(min(3, ySlotCount)):
			self.slotList[i].SetPosition(0, 30 + ySlotCount*32 - i*32)
			if vnum != 1:
				self.slotList[i].OnMouseOverIn = lambda arg = slot: self.OverInItem(arg)
				self.slotList[i].OnMouseOverOut = lambda arg = self.tooltipItem: self.OverOutItem(arg)
			else:
				self.slotList[i].OnMouseOverIn = lambda arg = localeInfo.MONETARY_UNIT0: self.OverInToolTip(arg)
				self.slotList[i].OnMouseOverOut = lambda: self.OverOutToolTip()
			self.slotList[i].Show()

		self.GetChild("accept").SetPosition(-40, 74 + 32*ySlotCount + newHeight)
		self.GetChild("cancel").SetPosition(40, 74 + 32*ySlotCount + newHeight)

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def SetCloseEvent(self, event):
		self.titleBar.SetCloseEvent(event)
		
	def SetMessage(self, text):
		self.textLine.SetText(text)

	def OverInToolTip(self, arg):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(arg, 0xffffff00)
		self.toolTip.Show()
	
	def OverOutToolTip(self):
		self.toolTip.Hide()
		
	def OverInItem(self, slot):
		if self.window_type == "shop":
			self.tooltipItem.SetShopItem(slot)
		elif self.window_type == "inv":
			self.tooltipItem.SetInventoryItem(slot)
		
	def OverOutItem(self, tooltipItem):
		if None != tooltipItem:
			self.tooltipItem.HideToolTip()
			self.tooltipItem.ClearToolTip()
	
	def Close(self):
		self.ClearDictionary()
		self.slotList = []
		self.titleBar = None
		self.titleName = None
		self.itemPrice = None
		self.slotGrid = None
		
		self.toolTip = None
		self.tooltipItem = None
		self.Hide()
		
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		
	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()
		
		return True

class PopupDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.acceptEvent = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")

			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.accceptButton = self.GetChild("accept")
			self.accceptButton.SetEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("PopupDialog.LoadDialog.BindObject")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()
		self.acceptEvent()

	def Destroy(self):
		self.Close()
		self.ClearDictionary()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SetText(self, text):
		self.message.SetText(text)

	def SetAcceptEvent(self, event):
		self.acceptEvent = event

	def SetButtonName(self, name):
		self.accceptButton.SetText(name)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnIMEReturn(self):
		self.Close()
		return True

class InputDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialog.py")

		getObject = self.GetChild
		self.board = getObject("Board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputSlot = getObject("InputSlot")
		self.inputValue = getObject("InputValue")

	def Open(self):
		self.inputValue.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10
		self.SetBoardWidth(max(width + 50, 160))
		self.SetSlotWidth(width)
		self.inputValue.SetMax(length)

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())
		if self.IsRTL():
			self.inputValue.SetPosition(self.inputValue.GetWidth(), 0)

	def SetBoardWidth(self, width):
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.board.SetSize(max(width + 50, 160), self.GetHeight())
		if self.IsRTL():
			self.board.SetPosition(self.board.GetWidth(), 0)
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def GetText(self):
		return self.inputValue.GetText()

class InputDialogWithDescription(InputDialog):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		if localeInfo.IsARABIC() :
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "inputdialogwithdescription.py")
		else:
			pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogwithdescription.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description = getObject("Description")

		except:
			import exception
			exception.Abort("InputDialogWithDescription.LoadBoardDialog.BindObject")

	def SetDescription(self, text):
		self.description.SetText(text)

class InputDialogWithDescription2(InputDialog):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()

	def __del__(self):
		InputDialog.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/inputdialogwithdescription2.py")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")
			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")
			self.description1 = getObject("Description1")
			self.description2 = getObject("Description2")

		except:
			import exception
			exception.Abort("InputDialogWithDescription.LoadBoardDialog.BindObject")

	def SetDescription1(self, text):
		self.description1.SetText(text)

	def SetDescription2(self, text):
		self.description2.SetText(text)

class QuestionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()
		return True

class QuestionDialogItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialogitem.py")
		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.destroyButton = self.GetChild("destroy")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetDestroyEvent(self, event):
		self.destroyButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()
		return True

class QuestionDialog2(QuestionDialog):

	def __init__(self):
		QuestionDialog.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		QuestionDialog.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def SetText1(self, text):
		self.textLine1.SetText(text)

	def SetText2(self, text):
		self.textLine2.SetText(text)

class QuestionDialogWithTimeLimit(QuestionDialog2):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__CreateDialog()
		self.endTime = 0

	def __del__(self):
		QuestionDialog2.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog2.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self, msg, timeout):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

		self.SetText1(msg)
		self.endTime = app.GetTime() + timeout

	def OnUpdate(self):
		leftTime = max(0, self.endTime - app.GetTime())
		self.SetText2(localeInfo.UI_LEFT_TIME % (leftTime))

class MoneyInputDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.moneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_SELLPRICE
		self.__CreateDialog()
		self.SetMaxLength(9)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/moneyinputdialog.py")

		getObject = self.GetChild
		self.board = self.GetChild("board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputValue = getObject("InputValue")
		self.inputValue.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.moneyText = getObject("MoneyValue")
		if app.ENABLE_CHEQUE_SYSTEM:
			self.chequeText = getObject("ChequeValue")
			self.inputChequeValue = getObject("InputValue_Cheque")
			self.inputChequeValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
			self.inputChequeValue.OnMouseLeftButtonDown = ui.__mem_func__(self.__ClickChequeEditLine)
			self.inputValue.OnMouseLeftButtonDown = ui.__mem_func__(self.__ClickValueEditLine)

	def Open(self):
		self.inputValue.SetText("")
		self.inputValue.SetFocus()
		self.__OnValueUpdate()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputValue = None
		self.Hide()
		if app.ENABLE_CHEQUE_SYSTEM:
			self.inputChequeValue = None

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		length = min(9, length)
		self.inputValue.SetMax(length)

	def SetMoneyHeaderText(self, text):
		self.moneyHeaderText = text

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def SetValue(self, value):
		value=str(value)
		self.inputValue.SetText(value)
		self.__OnValueUpdate()
		ime.SetCursorPosition(len(value))


	def GetText(self):
		return self.inputValue.GetText()

	if app.ENABLE_CHEQUE_SYSTEM:
		def SetCheque(self, cheque):
			cheque=str(cheque)
			self.inputChequeValue.SetText(cheque)
			self.__OnValueUpdate()
			ime.SetCursorPosition(len(cheque)+1)

		def GetTextCheque(self):
			return self.inputChequeValue.GetText()

		def __ClickChequeEditLine(self):
			self.inputChequeValue.SetFocus()
			if len(self.inputValue.GetText()) <= 0:
				self.inputValue.SetText(str(0))

		def __ClickValueEditLine(self):
			self.inputValue.SetFocus()
			if len(self.inputChequeValue.GetText()) <= 0:
				self.inputChequeValue.SetText(str(0))

		def GetCheque(self):
			return self.inputChequeValue.GetText()

		def __OnValueUpdate(self):
			if self.inputValue.IsFocus():
				ui.EditLine.OnIMEUpdate(self.inputValue)
			elif self.inputChequeValue.IsFocus():
				ui.EditLine.OnIMEUpdate(self.inputChequeValue)
			else:
				pass

			text = self.inputValue.GetText()
			cheque_text = self.inputChequeValue.GetText()

			money = 0
			cheque = 0
			GOLD_MAX = 2000000000
			CHEQUE_MAX = 1000

			if text and text.isdigit():
				try:
					money = int(text)
					
					if money >= GOLD_MAX:
						money = GOLD_MAX - 1
						self.inputValue.SetText(str(money))
				except ValueError:
					money = 0

			if cheque_text and cheque_text.isdigit():
				try:
					cheque = int(cheque_text)
					
					if cheque >= CHEQUE_MAX:
						cheque = CHEQUE_MAX - 1
						self.inputValue.SetText(str(cheque))
				except ValueError:
					cheque = 0
			self.chequeText.SetText(str(cheque) + " " + localeInfo.CHEQUE_SYSTEM_UNIT_WON)
			self.moneyText.SetText(localeInfo.NumberToGoldNotText(money) + " " + localeInfo.CHEQUE_SYSTEM_UNIT_YANG)
	else:
		def __OnValueUpdate(self):
			ui.EditLine.OnIMEUpdate(self.inputValue)
	
			text = self.inputValue.GetText()
			for i in xrange(len(text)):
				if not text[i].isdigit():
					text=text[0:i]+text[i+1:]
					self.inputValue.SetText(text)
			self.moneyText.SetText(self.moneyHeaderText + localeInfo.NumberToMoneyString(text))


class QuestionDialogRonark(QuestionDialog):

	def __init__(self):
		QuestionDialog.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		QuestionDialog.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialogronark.py")

		self.board = self.GetChild("board")
		self.textLine1 = self.GetChild("message1")
		self.textLine2 = self.GetChild("message2")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")
		self.observer = self.GetChild("observer")
		self.GetChild("TitleBar").SetCloseEvent(self.Close)

	def SetText1(self, text):
		self.textLine1.SetText(text)

	def SetText2(self, text):
		self.textLine2.SetText(text)
		
	def SetObserverEvent(self, event):
		self.observer.SetEvent(event)




class MoneyInputDialogOfflineShop(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.moneyHeaderText = localeInfo.MONEY_INPUT_DIALOG_SELLPRICE
		self.__CreateDialog()
		self.SetMaxLength(14)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/moneyinputdialogofflineshop.py")

		getObject = self.GetChild
		self.board = self.GetChild("board")
		self.acceptButton = getObject("AcceptButton")
		self.cancelButton = getObject("CancelButton")
		self.inputValue = getObject("InputValue")
		#self.inputValue.SetNumberMode()
		self.inputValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.moneyText = getObject("MoneyValue")
		if app.ENABLE_CHEQUE_SYSTEM:
			self.chequeText = getObject("ChequeValue")
			self.inputChequeValue = getObject("InputValue_Cheque")
			self.inputChequeValue.OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
			self.inputChequeValue.OnMouseLeftButtonDown = ui.__mem_func__(self.__ClickChequeEditLine)
			self.inputValue.OnMouseLeftButtonDown = ui.__mem_func__(self.__ClickValueEditLine)
		
	def Open(self):
		self.inputValue.SetText("")
		self.inputValue.SetFocus()
		self.__OnValueUpdate()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputValue = None
		if app.ENABLE_CHEQUE_SYSTEM:
			self.inputChequeValue = None
		self.Hide()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		self.inputValue.SetMax(length)
		self.inputValue.SetUserMax(length)

	def SetMoneyHeaderText(self, text):
		self.moneyHeaderText = text

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def SetValue(self, value):
		value=str(value)
		self.inputValue.SetText(value)
		self.__OnValueUpdate()
		ime.SetCursorPosition(len(value))

	def GetText(self):
		return self.inputValue.GetText()
	
	if app.ENABLE_CHEQUE_SYSTEM:
		def SetCheque(self, cheque):
			cheque=str(cheque)
			self.inputChequeValue.SetText(cheque)
			self.__OnValueUpdate()
			ime.SetCursorPosition(len(cheque)+1)

		def GetTextCheque(self):
			return self.inputChequeValue.GetText()

		def __ClickChequeEditLine(self):
			self.inputChequeValue.SetFocus()
			if len(self.inputValue.GetText()) <= 0:
				self.inputValue.SetText(str(0))

		def __ClickValueEditLine(self):
			self.inputValue.SetFocus()
			if len(self.inputChequeValue.GetText()) <= 0:
				self.inputChequeValue.SetText(str(0))

		def GetCheque(self):
			return self.inputChequeValue.GetText()

		def __OnValueUpdate(self):
			if self.inputValue.IsFocus():
				ui.EditLine.OnIMEUpdate(self.inputValue)
			elif self.inputChequeValue.IsFocus():
				ui.EditLine.OnIMEUpdate(self.inputChequeValue)
			else:
				pass

			text = self.inputValue.GetText()
			cheque_text = self.inputChequeValue.GetText()

			money = 0
			cheque = 0
			GOLD_MAX = 2000000000
			CHEQUE_MAX = 1000

			if text and text.isdigit():
				try:
					money = int(text)
					
					if money >= GOLD_MAX:
						money = GOLD_MAX - 1
						self.inputValue.SetText(str(money))
				except ValueError:
					money = 0

			if cheque_text and cheque_text.isdigit():
				try:
					cheque = int(cheque_text)
					
					if cheque >= CHEQUE_MAX:
						cheque = CHEQUE_MAX - 1
						self.inputValue.SetText(str(cheque))
				except ValueError:
					cheque = 0
			self.chequeText.SetText(str(cheque) + " " + localeInfo.CHEQUE_SYSTEM_UNIT_WON)
			self.moneyText.SetText(localeInfo.NumberToGoldNotText(money) + " " + localeInfo.CHEQUE_SYSTEM_UNIT_YANG)
	else:
		def __OnValueUpdate(self):
			ui.EditLine.OnIMEUpdate(self.inputValue)

			text = self.inputValue.GetText()
			for i in xrange(len(text)):
				if not text[i].isdigit():
					text=text[0:i]+text[i+1:]
					self.inputValue.SetText(text)
			self.moneyText.SetText(self.moneyHeaderText + localeInfo.NumberToMoneyString(text))


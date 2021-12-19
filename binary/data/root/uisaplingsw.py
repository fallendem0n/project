
import app,net,player,chrmgr,systemSetting,chat,background

#/*********************************************/#

import ui
import snd
import localeInfo
import constInfo
import uiPrivateShopBuilder
import interfaceModule
import serverInfo
import os
import uiSelectMusic
import musicInfo
#/*********************************************/#

class OptionDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE SYSTEM OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY SYSTEM OPTION DIALOG"

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("System.OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.changeMusicButton = GetObject("bgm_button")
			self.change2MusicButton = GetObject("bgm_button2")
		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/saplingbotoption.py")
		self.__Load_BindObject()

		self.SetCenterPosition()
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.changeMusicButton.SAFE_SetEvent(self.__OnClickChangeMusicButton)
		self.change2MusicButton.SAFE_SetEvent(self.__OnClick2ChangeMusicButton)

	def __OnClickChangeMusicButton(self):
		self.Hide()
		constInfo.EFSUNBOT = 1

	def __OnClick2ChangeMusicButton(self):
		self.Hide()
		if not constInfo.eigenmod:
			execfile('eigenmods.py',{})
			constInfo.eigenmod = 1
		else:
			chat.AppendChat(1, "Efsunbot zaten aktif")

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def __NotifyChatLine(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, text)

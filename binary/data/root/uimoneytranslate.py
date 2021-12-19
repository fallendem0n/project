import net,chat,player
import ui, uiCommon, localeInfo, pysettings, uiToolTip, grp

class ChequeToGoldWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE ChequeToGoldWindow DIALOG"

	def __Initialize(self):
		self.titleBar = 0
		self.priceTab = []
		self.tooltipInfo = None

	def Destroy(self):
		self.ClearDictionary()
		self.tooltipInfo = None
		self.__Initialize()
		print " -------------------------------------- DESTROY ChequeToGoldWindow DIALOG"

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("System.ChequeToGoldWindow.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.changeMusicButton = GetObject("bgm_button")
			self.background_1 = GetObject("background_1")
			self.background_2 = GetObject("background_2")

			self.InformationButton = self.GetChild("InformationButton")

			self.priceTab = []
			self.priceTab.append(self.GetChild("Price_Tab_01"))
			self.priceTab.append(self.GetChild("Price_Tab_02"))

		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/moneytranslate.py")
		self.__Load_BindObject()
		self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.changeMusicButton.SAFE_SetEvent(self.__OnClickConfirmButton)

		self.priceTab[0].SetEvent(lambda arg=0: self.PricePage(arg))
		self.priceTab[1].SetEvent(lambda arg=1: self.PricePage(arg))
		self.priceTab[0].Down()
		self.pricePageIndex = 0

		self.background_2.Hide()

		self.tlInfo = uiToolTip.ItemToolTip()
		self.tlInfo.Hide()
		self.tooltipInfo = [self.tlInfo]*4
		self.InformationText = ["Döviz Sistemi",
								"Depocu'ya gerek kalmadan",
								"uzaktan döviz iþlemlerini yapabilirsiniz.",
								"",
		]
			
		for i in xrange(4):
			self.tooltipInfo[i].SetFollow(True)
			self.tooltipInfo[i].AlignHorizonalCenter()
			if i == 0:
				TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
				self.tooltipInfo[i].AutoAppendTextLine(self.InformationText[i], TITLE_COLOR)
			else:
				self.tooltipInfo[i].AutoAppendTextLine(self.InformationText[i])
			self.tooltipInfo[i].Hide()
			self.tooltipInfo[i].toolTipWidth += 35

	def PricePage(self, page):
		self.priceTab[self.pricePageIndex].SetUp()
		self.pricePageIndex = page
		self.priceTab[self.pricePageIndex].Down()

		self.background_1.Hide()
		self.background_2.Hide()

		if page == 0:
			self.background_1.Show()
			self.changeMusicButton.SAFE_SetEvent(self.__OnClickConfirmButton)
		elif page == 1:
			self.background_2.Show()
			self.changeMusicButton.SAFE_SetEvent(self.__OnClickConfirmButton2)
		else:
			self.background_1.Hide()
			self.background_2.Hide()

	def __OnClickChangeMusicButton(self):
		self.Hide()

	def __OnClickConfirmButton(self):
		if player.GetElk() >= pysettings.MAXYANG:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "-----------------------------")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffffÝþlem Baþarýsýz. |cffff6060Hesabýndaki yang miktarý maksimum seviyeye ulaþtý.")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffffMevcut yang miktarýn : |cff00ccff"+ localeInfo.NumberToMoneyStringKitmir(player.GetElk()))
			self.Close()
		elif player.GetCheque() < pysettings.MINWON:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "-----------------------------")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffffÝþlem Baþarýsýz. |cffff6060Hesabýndaki won miktarý yeterli deðil.")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cff00ccff Gereken minimum won miktarý = 1")
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffff1 Won Karþýðý Hesabýnýza 100M Yang Eklendi")
			net.SendChatPacket("/use_gold_ticket {0}".format(int(1)))

	def __OnClickConfirmButton2(self):
		if player.GetCheque() == pysettings.MAXWON:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "-----------------------------")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffffÝþlem Baþarýsýz. |cffff6060Hesabýndaki won miktarý maksimum seviyeye ulaþtý.")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffffMevcut won miktarýn : |cff00ccff"+ localeInfo.NumberToMoneyStringIboWon(player.GetCheque()))
			self.Close()
		elif player.GetElk() < pysettings.MINYANG:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "-----------------------------")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffffÝþlem Baþarýsýz. |cffff6060Hesabýndaki yang miktarý yeterli deðil.")
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cff00ccff Gereken minimum yang miktarý = 100.000.000")
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "|cffffffff100M Yang Karþýðý Hesabýnýza 1 Won Eklendi")
			net.SendChatPacket("/use_cheque_ticket {0}".format(int(100000000)))

	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def Show(self):
		ui.ScriptWindow.Show(self)

	def OnUpdate(self):
		for i in xrange(4):
			if self.InformationButton.IsIn():
				self.tooltipInfo[i].Show()
			else:
				self.tooltipInfo[i].Hide()

	def Close(self):
		self.Hide()

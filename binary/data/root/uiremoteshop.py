import ui
import net
import app
import chrmgr

class RemoteShop(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE GAME OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0

	def Destroy(self):
		self.ClearDictionary()
		self.__Initialize()
		print " -------------------------------------- DESTROY GAME OPTION DIALOG"

	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")

			self.market = GetObject("market")
			self.evlilik = GetObject("evlilik")
			self.silah = GetObject("silah")
			self.zirh = GetObject("zirh")
			self.balikci = GetObject("balikci")

			self.market.SAFE_SetEvent(self.butonlar,3)
			self.evlilik.SAFE_SetEvent(self.butonlar,9)
			self.silah.SAFE_SetEvent(self.butonlar,1)
			self.zirh.SAFE_SetEvent(self.butonlar,4)
			self.balikci.SAFE_SetEvent(self.butonlar,2)

		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("UIScript/remoteshop.py")
		self.__Load_BindObject()
		self.SetCenterPosition()
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

	def butonlar(self, npc):
		net.SendChatPacket("/open_range_npc " + str(npc))

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

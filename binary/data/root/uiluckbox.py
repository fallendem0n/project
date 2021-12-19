import ui
import localeInfo
import skill
import net
import item
import chr
import effect
import dbg
import background
import math
import app
import uiTooltip

class LuckBox(ui.ScriptWindow):


	def __init__(self):
		ui.ScriptWindow.__init__(self)
		
		self.board = None
		self.mainitem = 0
		self.count = 0
		self.needed = 0
		self.itemcount = 0
		self.tooltipItem = uiTooltip.ItemToolTip()
		self.tooltipItem.Hide()
		self.LoadWindow()
		



	def __del__(self):
		self.Destroy()
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/luckbox.py")
		except:
			import exception
			exception.Abort("LuckBox.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("board")			
			self.getreward = GetObject("getreward")			
			self.changereward = GetObject("changereward")			
			self.boxslot = GetObject("boxslot")
			self.changerslot = GetObject("changerslot")
			self.rewardslot = GetObject("rewardslot")
			self.counttext = GetObject("count")
			self.itemtext = GetObject("item")


			self.boxslot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem1))
			self.boxslot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.changerslot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem2))
			self.changerslot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.rewardslot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem3))
			self.rewardslot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.board.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
			self.getreward.SetEvent(ui.__mem_func__(self.ClaimReward))
			self.changereward.SetEvent(ui.__mem_func__(self.ChangeRewards))
		except:
			import exception
			exception.Abort("LuckBox.LoadDialog.BindObject")
			
			
	def OverInItem1(self, slotIndex):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetItemToolTip(item.LUCKBOX_VNUM)
		self.tooltipItem.Show()
		
	def OverInItem2(self, slotIndex):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetItemToolTip(item.LUCKBOX_CHANGER)
		self.tooltipItem.Show()
		
	def OverInItem3(self, slotIndex):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.SetItemToolTip(int(self.mainitem))
		self.tooltipItem.Show()
		
		
	def OverOutItem(self):
		self.tooltipItem.ClearToolTip()
		self.tooltipItem.Hide()



	
	def ClaimReward(self):
		net.SendChatPacket("/luckboxgetreward")
		
	def ChangeRewards(self):
		net.SendChatPacket("/luckboxchangereward")
	
	
	def SetBox(self, item, count, need, itemcount):
		self.mainitem = int(item)
		self.count = int(count)
		self.needed = int(need)
		self.itemcount = int(itemcount)
		self.counttext.SetText(localeInfo.LUCKBOX_DESC_COUNT+str(count))
		self.itemtext.SetText(localeInfo.LUCKBOX_DESC_CHANGER_COUNT+str(need))
		self.RefreshSlot()
		

			
			
	def RefreshSlot(self):
		self.boxslot.SetItemSlot(0, item.LUCKBOX_VNUM)
		self.changerslot.SetItemSlot(0, item.LUCKBOX_CHANGER, int(self.needed))
		self.rewardslot.SetItemSlot(0, int(self.mainitem),int(self.itemcount))
	
	
	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		

	def Open(self):			
		self.Show()
		self.RefreshSlot()
		self.SetCenterPosition()


	def Close(self):
		self.Hide()


	def __OnCloseButtonClick(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()


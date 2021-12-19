import net, constInfo, ui, background, time, chat

class Zmiana_Kanalu(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)

	def __del__(self):
		ui.Window.__del__(self)

	def Open(self):
		self.vegas_change = ui.BoardWithTitleBar()
		self.vegas_change.AddFlag("movable")
		self.vegas_change.AddFlag("float")
		self.vegas_change.SetTitleName("Hýzlý Kanal")
		self.vegas_change.SetCloseEvent(self.Close)
		
		x = 0
		
		self.channel_list = []
		
		for ch in xrange(4): #Liczba kana³ów
			channel_button = ui.Button()
			channel_button.SetParent(self.vegas_change) 
			channel_button.SetSize(100, 100)
			channel_button.SetPosition(30, 34 + (20 * x + x))
			channel_button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			channel_button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			channel_button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			channel_button.SetEvent(ui.__mem_func__(self.change_channel), ch)
			
			channel_button.SetText("Kanal " + str(ch+1))
			channel_button.Show()
			
			self.channel_list.append(channel_button)
			x = x + 1
		
		self.vegas_change.SetSize(150, 50 + (20 * x + x)) 
		self.vegas_change.SetCenterPosition()
		self.vegas_change.Show()
		
	def protect_maps(self):
		protect_list = [
			"season99/new_map_ox",
			"maps_dungeon/devils_zone",
			"maps_dungeon/dt_zone",
			"maps_vegas/wedding_zone",
			"maps_dungeon/spider_3",
			"maps_vegas/duel_zone",
		]
		if str(background.GetCurrentMapName()) in protect_list:
			return True
		return False
		
	def change_channel(self, ch):
		if self.protect_maps():
			chat.AppendChat(1, "[Siverp2] Bu haritada kanal deðiþtiremezsin !")
			return	
		elif time.clock() >= constInfo.change_time:
			self.Close()
			net.SetServerInfo("Siverp2 - Kanal %d" % int(ch+1)) # Nazwa pod minimapk¹ po zmianie kana³u
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[Siverp2] Kanal Deðiþtirildi!")
			net.SendChatPacket("/ch %d" % int(ch+1))
			constInfo.change_time = time.clock() + 10 # Czas po którym mo¿na zmieniaæ kana³
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "[Siverp2] Kanalý 5 saniyede bir deðiþtirebilirsiniz!")
		
	def	Close(self):
		self.vegas_change.Hide()
		
	def OnPressExitKey(self):
	
		self.Close()
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True
		
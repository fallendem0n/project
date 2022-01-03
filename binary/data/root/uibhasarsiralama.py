import ui, wndMgr, constInfo

class BossRanking(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Initialize(self):
		self.oyuncuDict = {}
		self.isLoad = False

	def LoadDialog(self):
	
		if self.isLoad:
			return
			
		self.isLoad = True
		self.SetPosition(wndMgr.GetScreenWidth() - 330, 210)

		for i in xrange(10): # issue
			nameText = ui.TextLine()
			nameText.SetParent(self)
			nameText.SetPosition(42, 10 + 22*i)
			nameText.SetHorizontalAlignLeft()
			nameText.Hide()

			raceIMG = ui.ImageBox()
			raceIMG.SetParent(self)
			raceIMG.SetPosition(12, 10 + 22*i)
			raceIMG.Hide()

			empIMG = ui.ImageBox()
			empIMG.SetParent(self)
			empIMG.SetPosition(132, 10 + 22*i)
			empIMG.Hide()

			hpText = ui.TextLine()
			hpText.SetParent(self)
			hpText.SetPosition(175, 11 + 22*i)
			hpText.SetHorizontalAlignLeft()
			hpText.Hide()
			
			hpGauge = ui.Gauge()
			hpGauge.SetParent(self)
			hpGauge.SetPosition(-210, 15 + 22*i)
			hpGauge.MakeGauge(80, "red")
			hpGauge.SetWindowHorizontalAlignRight()
			hpGauge.Hide()

			self.oyuncuDict.update({ int(i) : {} })
			self.oyuncuDict[i]["NAME"] = nameText
			self.oyuncuDict[i]["RACEIMG"] = raceIMG
			self.oyuncuDict[i]["EMPIMG"] = empIMG
			self.oyuncuDict[i]["HP_TEXT"] = hpText
			self.oyuncuDict[i]["HP"] = hpGauge
			
		self.SetSize(320, 35)

		
	def UpdateInfo(self):
		for i in range(len(constInfo.BOOS_DAMAGE_RANKING)):
			self.oyuncuDict[i]["NAME"].SetText("%s [Lv.%d]" % (constInfo.BOOS_DAMAGE_RANKING[i]["name"], constInfo.BOOS_DAMAGE_RANKING[i]["level"]))
			self.oyuncuDict[i]["NAME"].Show()

			self.oyuncuDict[i]["RACEIMG"].LoadImage("larry/boss_ranking/%d.tga" % (constInfo.BOOS_DAMAGE_RANKING[i]["race"]))
			self.oyuncuDict[i]["RACEIMG"].Show()

			self.oyuncuDict[i]["EMPIMG"].LoadImage("larry/boss_ranking/empire/%d.tga" % (constInfo.BOOS_DAMAGE_RANKING[i]["empire"]))
			self.oyuncuDict[i]["EMPIMG"].Show()

			self.oyuncuDict[i]["HP_TEXT"].SetText("%%%d" % (constInfo.BOOS_DAMAGE_RANKING[i]["damage"]))
			self.oyuncuDict[i]["HP_TEXT"].Show()

			self.oyuncuDict[i]["HP"].SetPercentage(constInfo.BOOS_DAMAGE_RANKING[i]["damage"], 100)
			self.oyuncuDict[i]["HP"].Show()

	def OnUpdate(self):
		self.SetSize(320, int(len(constInfo.BOOS_DAMAGE_RANKING)*35))
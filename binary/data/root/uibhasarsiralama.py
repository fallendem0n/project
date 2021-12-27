import ui, wndMgr, chat

class BossRanking(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Initialize(self):
		self.oyuncuDict = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}}
		self.isLoad = False

	def LoadDialog(self):
	
		if self.isLoad:
			return
			
		self.isLoad = True
		self.SetPosition(wndMgr.GetScreenWidth() - 330, 210)

		for i in xrange(5):
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

			self.oyuncuDict[i]["NAME"] = nameText
			self.oyuncuDict[i]["RACEIMG"] = raceIMG
			self.oyuncuDict[i]["EMPIMG"] = empIMG
			self.oyuncuDict[i]["HP_TEXT"] = hpText
			self.oyuncuDict[i]["HP"] = hpGauge
			
		self.SetSize(320, 150)

		
	def UpdateInfo(self, list, race, name, level, empire, damage):
		self.oyuncuDict[list]["NAME"].SetText("%s [Lv.%d]" % (str(name), int(level)))
		self.oyuncuDict[list]["NAME"].Show()

		self.oyuncuDict[list]["RACEIMG"].LoadImage("larry/boss_ranking/%d.tga" % int(race))
		self.oyuncuDict[list]["RACEIMG"].Show()

		self.oyuncuDict[list]["EMPIMG"].LoadImage("larry/boss_ranking/empire/%d.tga" % int(empire))
		self.oyuncuDict[list]["EMPIMG"].Show()

		self.oyuncuDict[list]["HP_TEXT"].SetText("%%%d" % float(damage))
		self.oyuncuDict[list]["HP_TEXT"].Show()
		# if int(poison) > 0:
			# self.oyuncuDict[list]["HP"].SetGaugeColor("lime")
		self.oyuncuDict[list]["HP"].SetPercentage(float(damage), 100)
		self.oyuncuDict[list]["HP"].Show()
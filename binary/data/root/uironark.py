import ui
import wndMgr
import guild

class RonarkWarScoreBoard(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Initialize(self):
		self.maxcount = 0
		self.observer = 0
		self.enemyDataDict = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}}
		self.isLoad = False

	def LoadDialog(self):
	
		if self.isLoad:
			return
			
		self.isLoad = True
		self.SetPosition(wndMgr.GetScreenWidth() - 330, 210)
		
		self.Observer = ui.TextLine()
		self.Observer.SetParent(self)
		self.Observer.SetPosition(157, 3)
		self.Observer.SetText("Seyirci: %d" % int(self.observer))
		self.Observer.SetWindowHorizontalAlignCenter()
		self.Observer.SetHorizontalAlignCenter()
		self.Observer.Show()
		
		self.img = ui.ImageBox()
		self.img.LoadImage("d:/ymir work/ui/seperator.tga")
		self.img.SetParent(self)
		self.img.SetPosition(60, -1)
		self.img.Show()
		
		self.imgs = ui.ImageBox()
		self.imgs.LoadImage("d:/ymir work/ui/seperator.tga")
		self.imgs.SetParent(self)
		self.imgs.SetPosition(60, 19)
		self.imgs.Show()
		
		self.sinir = ui.TextLine()
		self.sinir.SetParent(self)
		self.sinir.SetPosition(157, 24)
		self.sinir.SetText("Giriþ Sýnýrý: %d" % int(self.maxcount))
		self.sinir.SetWindowHorizontalAlignCenter()
		self.sinir.SetHorizontalAlignCenter()
		self.sinir.Show()

		for i in xrange(5):
			mark = ui.MarkBox()
			mark.SetParent(self)
			mark.SetIndex(0)
			mark.SetPosition(22, 55 + 22*i)
			mark.Hide()
			scoreText = ui.TextLine()
			scoreText.SetParent(self)
			scoreText.SetPosition(42, 55 + 22*i)
			scoreText.SetHorizontalAlignLeft()
			scoreText.Hide()
			
			hpText = ui.TextLine()
			hpText.SetParent(self)
			hpText.SetPosition(175, 56 + 22*i)
			hpText.SetHorizontalAlignLeft()
			hpText.Hide()
			
			hpGauge = ui.Gauge()
			hpGauge.SetParent(self)
			hpGauge.SetPosition(-210, 60 + 22*i)
			hpGauge.MakeGauge(80, "blue")
			hpGauge.SetWindowHorizontalAlignRight()
			hpGauge.Hide()

			self.enemyDataDict[i]["MARK"] = mark
			self.enemyDataDict[i]["TEXT"] = scoreText
			self.enemyDataDict[i]["HP_TEXT"] = hpText
			self.enemyDataDict[i]["HP"] = hpGauge
			
		self.SetSize(320, 183)

		
	def UpdateInfo(self, list, id, name, damage, member, maxcount, observer):
		self.Observer.SetText("Seyirci: %d" % int(observer))
		self.sinir.SetText("Giriþ Sýnýrý: %d" % int(maxcount))

		self.enemyDataDict[list]["MARK"].SetIndex(int(id))
		self.enemyDataDict[list]["MARK"].Show()

		self.enemyDataDict[list]["TEXT"].SetText("%s (Katýlým: %d)" % (str(name), int(member)))
		self.enemyDataDict[list]["TEXT"].Show()

		self.enemyDataDict[list]["HP_TEXT"].SetText("%%%d" % float(damage))
		self.enemyDataDict[list]["HP_TEXT"].Show()
		
		self.enemyDataDict[list]["HP"].SetPercentage(float(damage), 100)
		self.enemyDataDict[list]["HP"].Show()
		
			

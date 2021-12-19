# -*- coding: utf-8 -*-
import os
import app
import dbg
import item
import chat
import net
import localeInfo
import ime
import time
import ui
import uiCommon
import uiToolTip
import colorInfo
import player
import snd
import grp
import mouseModule
import wndMgr
import skill
import uiScriptLocale
SKILLS=[1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 122, 123, 121, 124, 125, 129, 130, 131, 137, 138, 139, 140, 31, 32, 33, 34, 35, 46, 47, 48, 49, 50, 61, 62, 63, 64, 65, 66, 76, 77, 78, 79, 80, 81,91, 92, 93, 94, 95, 96, 106, 107, 108, 109, 110, 111]
SKILL_BOOKS=  []
ITEM_LIST=item.GetNames()
SKILL_BOOK_NAMES={
	50300:localeInfo.TOOLTIP_SKILLBOOK_NAME,
	70037:localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME,
	# 70055:localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME,
}

for skillIndex in SKILLS:
	for vnum,bookName in SKILL_BOOK_NAMES.iteritems():
		skillName = skill.GetSkillName(skillIndex)
		if not skillName:
			continue
		SKILL_BOOKS.append({"vnum":vnum,"name":skillName + " " + bookName,"skill":skillIndex})



class ShopSearch(ui.BoardWithTitleBar):

	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.UI={}
		self.search_vnum=0
		self.search_book=0
		self.last=0
		self.pop=None
		self.__Load()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
	def __Load(self):
		self.SetSize(300, 100)		
		self.SetTitleName(uiScriptLocale.SHOP_SEARCH_TITLE)
		self.SetCloseEvent(self.Close)
		
		self.UI["priceText"] = ui.MakeText(self, uiScriptLocale.SHOP_SEARCH_PRICE,15, 25, None)
		self.UI["priceEdit"]=Edit2(self,"0",45,175,30,25,1,3,16)
		self.UI["priceEdit"].OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdateYang)
		
		
		self.UI["clear_button"] = ui.MakeButton(self,40, 30,"","d:/ymir work/ui/public/","middle_Button_01.sub","middle_Button_02.sub","middle_Button_03.sub")
		self.UI["clear_button"].SetText(uiScriptLocale.SHOP_SEARCH_CLEAR)
		self.UI["clear_button"].SetEvent(lambda : self.ClearTarget())
		self.UI["clear_button"].Show()
		
		self.UI["search_button"] = ui.MakeButton(self,105, 30,"","d:/ymir work/ui/public/","middle_Button_01.sub","middle_Button_02.sub","middle_Button_03.sub")
		self.UI["search_button"].SetText(uiScriptLocale.SHOP_SEARCH_BUTTON)
		self.UI["search_button"].SetEvent(lambda : self.Search())
		self.UI["search_button"].Show()
		
		
		self.UI["list_names"] = DropDown(self)
		self.UI["list_names"].OnChange=self.OnChange
		self.UI["list_names"].SetPosition(15,60)
		self.UI["list_names"].Hide()
		
		self.UI["nameText"] = ui.MakeText(self,uiScriptLocale.SHOP_SEARCH_ENTER_ITEM_NAME,15, 30, None)
		
		self.UI["nameEdit"]=Edit2(self,"",15,45,200,25,FALSE,6,30)
		self.UI["nameEdit"].OnIMEUpdate = ui.__mem_func__(self.__OnValueUpdate)
		self.UI["nameEdit"].SetReturnEvent(ui.__mem_func__(self.__OnHideList))
		self.UI["nameEdit"].SetEscapeEvent(ui.__mem_func__(self.__OnHideList))
				
		self.AddFlag("movable")
		self.AddFlag("float")
		self.SetCenterPosition()
		self.UI["nameText"].SetWindowHorizontalAlignLeft()
		self.UI["search_button"].SetWindowVerticalAlignBottom()
		self.UI["search_button"].SetWindowHorizontalAlignCenter()
		self.UI["priceText"].SetWindowVerticalAlignBottom()
		self.UI["priceText"].SetWindowHorizontalAlignLeft()
		self.UI["clear_button"].SetWindowVerticalAlignBottom()
		self.UI["clear_button"].SetWindowHorizontalAlignCenter()
		self.UI["priceEdit"].imageSlot.SetPosition(45,self.GetHeight()-27)
		self.Hide()
		
	def ClearTarget(self):
		net.SendChatPacket("/search_shop 0 0 0")
		self.search_book=0
		self.search_vnum=0
		self.UI["nameEdit"].SetText("")
		self.UI["priceEdit"].SetText("0")
		self.__OnHideList()
		
	def Search(self):
		price=self.UI["priceEdit"].GetText()
		if len(price):
			price=int(filter(str.isdigit, price))
		else:
			price=0
		if self.search_vnum == 0:
			self.PopupMessage(uiScriptLocale.SHOP_SEARCH_EMPTY_ITEM_NAME)
			return
		net.SendChatPacket("/search_shop {0} {1} {2}".format(self.search_vnum,price,self.search_book))
		
	def PopupMessage(self,text):
		pop = uiCommon.PopupDialog()
		pop.SetText(text)
		pop.SetAcceptEvent(self.__OnClosePopupDialog)
		pop.Open()
		self.pop = pop
		self.pop.SetTop()
		
	def __OnClosePopupDialog(self):
		if self.pop != None:
			if self.pop.IsShow():
				self.pop.Hide()
		self.pop = None
	
	def OnChange(self):
		self.search_vnum=self.UI["list_names"].DropList.GetSelectedItem().value
		self.search_book=self.UI["list_names"].DropList.GetSelectedItem().skill
		name=""
		if not self.search_book:
			for it in ITEM_LIST:
				if int(it["vnum"]) == self.search_vnum:
					name=it["name"]
					break
		else:
			for book in SKILL_BOOKS:
				if int(book["vnum"]) == self.search_vnum and int(book["skill"]) == self.search_book:
					name=book["name"]
					break
					
		self.UI["nameEdit"].SetText(str(name))
		self.UI["list_names"].Clear()
		self.UI["list_names"].Hide()
		ime.SetCursorPosition(len(name)+1)
		
	def __OnValueUpdateYang(self):
		ui.EditLine.OnIMEUpdate(self.UI["priceEdit"])
		text=self.UI["priceEdit"].GetText()
		if len(text):
			self.UI["priceEdit"].SetText((int(filter(str.isdigit, text))))
	def __OnValueUpdate(self):
		ui.EditLine.OnIMEUpdate(self.UI["nameEdit"])
		val=self.UI["nameEdit"].GetText()
		if len(val)>0:
			self.UI["list_names"].Clear()
			f=0
			n=[]
			for it in ITEM_LIST:
				vnum,name=it["vnum"],it["name"]
				if f==10:
					break
				if vnum in SKILL_BOOK_NAMES.keys():
					continue
				if len(name)>=len(val) and name[:len(val)].lower() == val.lower():
					self.UI["list_names"].AppendItem(name,vnum)
					f+=1
			if f==0:
				for book in SKILL_BOOKS:
					if f==10:
						break
					vnum,name,skill=book["vnum"],book["name"],book["skill"]
					if len(name)>=len(val) and name[:len(val)].lower() == val.lower():
						self.UI["list_names"].AppendItem(name,vnum,skill)
						f+=1
			
			
			if f>0:
				if self.UI["list_names"].dropped==0:
					self.UI["list_names"].Clear()
					self.UI["list_names"].ExpandMe()
				self.UI["list_names"].Show()
				return
		self.__OnHideList()
	def __OnHideList(self):
		self.UI["list_names"].dropped=0
		self.UI["list_names"].Clear()
		self.UI["list_names"].Hide()
		
	def OnPressEscapeKey(self):
		if self.UI["list_names"].dropped:
			self.UI["list_names"].dropped=0
			self.UI["list_names"].Clear()
			self.UI["list_names"].Hide()
		else:
			self.Close()
	def Show(self):
		ui.BoardWithTitleBar.Show(self)
		self.SetCenterPosition()
		self.SetTop()
	def Close(self):
		self.search_book=0
		self.search_vnum=0
		self.__OnHideList()
		self.Hide()
		return TRUE
		

class DropDown(ui.Window):
	dropped  = 0
	dropstat = 0
	width = 0
	height = 0
	maxh = 30
	OnChange = None
	class Item(ui.Window):
		TEMPORARY_PLACE = 0
		width = 0
		height = 0
		def __init__(self,parent, text,value=0,skill=0):
			ui.Window.__init__(self)
			self.textBox=ui.MakeTextLine(self)
			self.textBox.SetText(text)
			self.value = int(value)
			self.skill = int(skill)

		def __del__(self):
			ui.Window.__del__(self)

		def SetParent(self, parent):
			ui.Window.SetParent(self, parent)
			self.parent=parent

		def OnMouseLeftButtonDown(self):
			self.parent.SelectItem(self)

		def SetSize(self,w,h):
			ui.Window.SetSize(self,w,h)
			self.width = w
			self.height = h
		def OnUpdate(self):	
			if self.IsIn():
				self.isOver = True
			else:
				self.isOver = False
		def OnRender(self):
			xRender, yRender = self.GetGlobalPosition()
			yRender -= self.TEMPORARY_PLACE
			widthRender = self.width
			heightRender = self.height + self.TEMPORARY_PLACE*2
			grp.SetColor(ui.BACKGROUND_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)
			grp.SetColor(ui.DARK_COLOR)
			grp.RenderLine(xRender, yRender, widthRender, 0)
			grp.RenderLine(xRender, yRender, 0, heightRender)
			grp.SetColor(ui.BRIGHT_COLOR)
			grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
			grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

			if self.isOver:
				grp.SetColor(ui.HALF_WHITE_COLOR)
				grp.RenderBar(xRender + 2, yRender + 3, self.width - 3, heightRender - 5)

	
	def __init__(self,parent):
		ui.Window.__init__(self,"TOP_MOST")
		self.down = 1
		self.parent=parent
	
		
		self.DropList = ui.ListBoxEx()
		self.DropList.SetParent(self)
		self.DropList.itemHeight = 20
		self.DropList.itemWidth = 220
		self.DropList.itemStep = 18
		self.DropList.SetPosition(0,0)
		self.DropList.SetSize(200,2) 
		self.DropList.SetSelectEvent(self.SetTitle)
		self.DropList.SetViewItemCount(0)
		self.DropList.Show()
		self.selected = self.DropList.GetSelectedItem()
		
		self.SetSize(220,95)
	
	def __del__(self): 
		ui.Window.__del__(self)
		
	def AppendItem(self,text,value=0,skill=0):  
		self.DropList.AppendItem(self.Item(self,text,value,skill))
	
	def OnPressEscapeKey(self):		
		self.Hide()
		self.Clear()
				
	def SetTitle(self,item):
		self.dropped = 0
		self.selected = item
		if self.OnChange:
			self.OnChange()
		self.Clear()		
		
	def SetSize(self,w,h):
		ui.Window.SetSize(self,w,h+10)
		self.width = w
		self.height = h
		self.DropList.SetSize(w,h)

	def Clear(self):
		for x in self.DropList.itemList:
			x.Hide()
		self.DropList.RemoveAllItems()

	def ExpandMe(self):
		if self.dropped == 1:
			self.dropped = 0
		else:
			self.dropped = 1
			
	def OnUpdate(self):
		(w,h) = self.parent.GetLocalPosition()
		self.maxh =self.DropList.itemStep*len(self.DropList.itemList)
		self.SetPosition(w+15,h+65)
		if self.dropped == 0 or not self.parent.IsShow() or len(self.DropList.itemList)==0:
			self.SetSize(self.GetWidth(),0)
			self.DropList.SetViewItemCount(0)
			self.Hide()
		elif self.dropped == 1:
			self.Show()
			self.SetTop()
			height = self.maxh+5 if int(self.maxh/self.DropList.itemStep) <2 else self.maxh
			self.SetSize(self.GetWidth(),height)
			self.DropList.SetViewItemCount(self.maxh/self.DropList.itemStep)


			
class Edit2(ui.EditLine):
	def __init__(self,parent,text,x,y,width,height,number=FALSE,slot=2,max = 12):
		ui.EditLine.__init__(self)
		self.imageSlot=ui.MakeImageBox(parent, "d:/ymir work/ui/public/Parameter_Slot_0"+str(slot)+".sub", x,y)
		self.SetText(text)
		self.main = text
		self.SetEscapeEvent(self.OnPressEscapeKey)
		self.SetMax(max)
		self.SetUserMax(max)
		self.SetParent(self.imageSlot)
		if number:
			self.SetNumberMode()
		
		self.SetSize(width,height)
		self.SetPosition(5,2)
		self.Show()
	def GetText(self):
		res = ui.EditLine.GetText(self)
		if res == "":
			return ""
		else:
			return res
	def OnPressEscapeKey(self):
		pass
	def __del__(self):
		ui.EditLine.__del__(self)
	#def OnSetFocus(self):
		#ui.EditLine.OnSetFocus(self)
		#if ui.EditLine.GetText(self) == self.main:
	#		self.SetText("")
	#def OnKillFocus(self):
	#	ui.EditLine.OnKillFocus(self)
	#	if ui.EditLine.GetText(self) == "":
	#		self.SetText(self.main)

	
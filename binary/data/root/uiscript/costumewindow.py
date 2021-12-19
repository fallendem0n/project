import uiScriptLocale
import item
import app

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",
	"x" : SCREEN_WIDTH - 175 - 186,
	"y" : SCREEN_HEIGHT - 37 - 565,
	"style" : ("movable", "float",),
	"width" : 181,
	"height" : 238,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 181,
			"height" : 238,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 6,
					"y" : 6,
					"width" : 181 - 12,
					"color" : "yellow",
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-2, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "all_align":"center" },
					),
				},
				
				{
					"name" : "Costume_Base",
					"type" : "image",
					"x" : 11,
					"y" : 35,
					"image" : "invpage3.tga",
					"children" :
					(
						{
							"name" : "CostumeSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 181-22,
							"height" : 188+35,
							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":60, "y":75, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":60, "y": 38, "width":32, "height":32},


											# {"index":COSTUME_START_INDEX+0, "x":62, "y":45, "width":32, "height":64},#¸ö
											# {"index":COSTUME_START_INDEX+1, "x":62, "y": 9, "width":32, "height":32},#¸Ó¸®
											# {"index":COSTUME_START_INDEX+2, "x":13, "y":126, "width":32, "height":32},#¸¶¿îÆ®
											# {"index":COSTUME_START_INDEX+3, "x":62, "y":126, "width":32, "height":32},#¾Ç¼¼¼­¸®
											# {"index":item.SPECIAL_FIRE_RING, "x":13, "y":126+32, "width":32, "height":32},#¹«±â
											# {"index":item.SPECIAL_ICE_RING, "x":62, "y":126+32, "width":32, "height":32},#¹«±â
											
										{"index":item.SPECIAL_FIRE_RING, 	"x":110,	"y":63, "width":32, "height":32},#Ateş yüzüğü
										{"index":item.SPECIAL_ICE_RING, 	"x":110,	"y":24, "width":32, "height":32},#Buz yüzüğü
										{"index":COSTUME_START_INDEX+3, "x":110, "y":97, "width":32, "height":32},##Ölümcül güzün yüzüğü
										{"index":COSTUME_START_INDEX+2, "x":110, "y":135, "width":32, "height":32},#3Binek

									#	{"index":item.EQUIPMENT_6, "x":110, "y":100, "width":32, "height":32},
										# {"index":item.EQUIPMENT_3, "x":110, "y":24, "width":32, "height":32},
							),
						},
					),
				},

			),
		},
	),
}
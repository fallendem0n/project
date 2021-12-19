import uiScriptLocale
import item
import app
import localeInfo

LOCALE_PATH = "d:/ymir work/ui/privatesearch/"

BOARD_WIDTH = 340
window = {
	"name" : "luckbox",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : 200,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : 200,
				
			"title" : uiScriptLocale.LUCKBOX_TITLE,
			
			"children" :
			(

				{
					"name" : "bg",
					"type" : "thinboard_circle",
					"x" : 133-115,
					"y" : 36,
					
					"width" : 300,
					"height" : 145,
				},
				
				{
					"name" : "img1",
					"type" : "image",

					"x" : 70,
					"y" : 50,

					"image" : "luckbox/redslot.tga",
					
					"children" :
					(
					
						{
							"name" : "boxslot",
							"type" : "slot",


							"x" : 4,
							"y" : 4,
							
							"width" : 32,
							"height" : 32,
							
							"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32,},),
						},					
					),
				},
				
				{
					"name" : "arrow",
					"type" : "image",


					"x" : 120,
					"y" : 65,


					"image" : LOCALE_PATH + "private_last_next_btn_01.sub",
				},
				
				{
					"name" : "img2",
					"type" : "image",

					"x" : 140,
					"y" : 50,

					"image" : "luckbox/yellowslot.tga",
					
					"children" :
					(
					
						{
							"name" : "rewardslot",
							"type" : "slot",


							"x" : 4,
							"y" : 4,
							
							"width" : 32,
							"height" : 32,
							
							"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32,},),
						},					
					),
				},
				
				{
					"name" : "img3",
					"type" : "image",

					"x" : 60,
					"y" : 120,

					"image" : "luckbox/greenslot.tga",
					
					"children" :
					(
					
						{
							"name" : "changerslot",
							"type" : "slot",


							"x" : 4,
							"y" : 4,
							
							"width" : 32,
							"height" : 32,
							
							"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32,},),
						},					
					),
				},
				
				
				{
					"name" : "count_slot",
					"type" : "image",

					"x" : 120,
					"y" : 120,

					"image" : "luckbox/inputslot1.tga",
					
					"children" :
					(
					
						{
							"name" : "count",
							"type" : "text",


							"x" : 4,
							"y" : 4,
							
							"text": uiScriptLocale.LUCKBOX_REMAIN
						},					
					),
				},
				
				{
					"name" : "item_slot",
					"type" : "image",

					"x" : 120,
					"y" : 140,

					"image" : "luckbox/inputslot1.tga",
					
					"children" :
					(
					
						{
							"name" : "item",
							"type" : "text",


							"x" : 4,
							"y" : 4,
							
							"text": uiScriptLocale.LUCKBOX_REMAIN
						},					
					),
				},
				
				{
					"name" : "getreward",
					"type" : "button",
					"x" : 190,
					"y" : 50,
					
					"default_image" : "d:/ymir work/ui/game/12zi/reward/btn_green_default.sub",
					"over_image" : "d:/ymir work/ui/game/12zi/reward/btn_green_over.sub",
					"down_image" : "d:/ymir work/ui/game/12zi/reward/btn_green_down.sub",
					"tooltip_text" : uiScriptLocale.LUCKBOX_GET_REWARD,
				},
				
				{
					"name" : "changereward",
					"type" : "button",
					"x" : 190,
					"y" : 75,
					
					"default_image" : "d:/ymir work/ui/game/12zi/reward/btn_yellow_default.sub",
					"over_image" : "d:/ymir work/ui/game/12zi/reward/btn_yellow_over.sub",
					"down_image" : "d:/ymir work/ui/game/12zi/reward/btn_yellow_down.sub",
					"tooltip_text" : uiScriptLocale.LUCKBOX_CHANGE_REWARD,
				},
				
				{
					"name" : "sep",
					"type" : "text",
					"x" : 50,
					"y" : 90,
					"text" : "________________________________________",
				},

			),
		},
	),
}

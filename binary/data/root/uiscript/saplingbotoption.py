import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
ROOT_PATH2 = "yusufwork/switchbot/"

TEMPORARY_X = +13
TEXT_TEMPORARY_X = -10
BUTTON_TEMPORARY_X = 5
PVP_X = -10

BOARD_W = 287
BOARD_H = 293

window = {
	"name" : "SystemOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width"	: BOARD_W,
	"height" : BOARD_H,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width"	: BOARD_W,
			"height" : BOARD_H,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARD_W - 15,
					"color" : "gray",

					"children" :
					(
						{ 
						"name":"titlename", "type":"text", "x":0, "y":3, 
						"horizontal_align":"center", "text_horizontal_align":"center",
						"text" : "Çoklu Efsun Botu Sistemi",
						 },
					),
				},
				{
					"name" : "arka",
					"type" : "image",
					"x" : 286 - 52,
					"y" : 7,

					"image" : "d:/ymir work/ui/game/mark/kose_arka.tga",
					"children" :
					(
						{
							"name" : "InformationButton",
							"type" : "button",

							"x" : 4,
							"y" : 4,

							"default_image" : "d:/ymir work/ui/game/mark/question_mark_1.tga",
							"over_image" : "d:/ymir work/ui/game/mark/question_mark_2.tga",
							"down_image" : "d:/ymir work/ui/game/mark/question_mark_3.tga",
						},
					),
				},
				{
					"name" : "backGround",
					"type" : "expanded_image",
					
					"x" : 10,
					"y" : 29+5,
					
					"image" : ROOT_PATH2+"gui_bg.png",
				},
				{
					"name" : "bgm_button",
					"type" : "button",

					"x" : 175,
					"y" : 236,

					"text" : "Norm. Efsun Botu",
					"text_color" : 0xff00ccff,

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
				{
					"name" : "bgm_button2",
					"type" : "button",

					"x" : 175,
					"y" : 170,

					"text" : "Yeþ. Efsun Botu",
					"text_color" : 0xff00ff00,

					"default_image" : ROOT_PATH + "Large_Button_01.sub",
					"over_image" : ROOT_PATH + "Large_Button_02.sub",
					"down_image" : ROOT_PATH + "Large_Button_03.sub",
				},
			),
		},
	),
}

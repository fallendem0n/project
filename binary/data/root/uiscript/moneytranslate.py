import uiScriptLocale

BUTTON_PATH = "yusufwork/bio/"
IMAGE_PATH = "yusufwork/moneytranslate/"

MAIN_WIDTH = 273 + 14
MAIN_HEIGHT = 253 + 39

window = {
	"name" : "ChequeToGoldWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : MAIN_WIDTH,
	"height" : MAIN_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : MAIN_WIDTH,
			"height" : MAIN_HEIGHT,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : MAIN_WIDTH - 15,
					"color" : "gray",

					"children" :
					(
						{ 
						"name":"titlename", "type":"text", "x":0, "y":3, 
						"horizontal_align":"center", "text_horizontal_align":"center",
						"text" : "Döviz Ýþlemleri",
						 },
					),
				},
				{
					"name" : "arka",
					"type" : "image",
					"x" : MAIN_WIDTH - 53,
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
					"name" : "background_1", "type" : "image",
					"image" : IMAGE_PATH + "background_1.png",
					"x" : 7,
					"y" : 33,
					"children" :
					(
						{
							"name" : "cheque_text",
							"type" : "text",
							"x" : 160,
							"y" : 130,
							"text" : "1",
						},
						{
							"name" : "yang_text",
							"type" : "text",
							"x" : 160,
							"y" : 174,
							"text" : "100.000.000",
						},
					),
				},
				{
					"name" : "background_2", "type" : "image",
					"image" : IMAGE_PATH + "background_2.png",
					"x" : 7,
					"y" : 33,
					"children" :
					(
						{
							"name" : "cheque_text",
							"type" : "text",
							"x" : 160,
							"y" : 174,
							"text" : "1",
						},
						{
							"name" : "yang_text",
							"type" : "text",
							"x" : 160,
							"y" : 130,
							"text" : "100.000.000",
						},
					),
				},
				{
					"name" : "bgm_button",
					"type" : "button",

					"x" : 110,
					"y" : 244,

					"text" : "Dönüþtür",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				{
					"name" : "Price_Tab_01",
					"type" : "radio_button",
					"x" : 27,
					"y" : 121,
					"default_image" : IMAGE_PATH + "translate_1.png",
					"over_image" : IMAGE_PATH + "translate_2.png",
					"down_image" : IMAGE_PATH + "translate_3.png",

					"children" :
						(
							{
								"name" : "01_Print",
								"type" : "text",
								"x" : -1,
								"y" : -3,
								"all_align" : "center",
								"text" : "Won - Yang",
							},
						),
				},
				{
					"name" : "Price_Tab_02",
					"type" : "radio_button",
					"x" : 146,
					"y" : 121,

					"default_image" : IMAGE_PATH + "translate_1.png",
					"over_image" : IMAGE_PATH + "translate_2.png",
					"down_image" : IMAGE_PATH + "translate_3.png",

					"children" :
						(
							{
								"name" : "02_Print",
								"type" : "text",
								"x" : -1,
								"y" : -3,
								"all_align" : "center",
								"text" : "Yang - Won",
							},
						),
				},
			),
		},
	),
}

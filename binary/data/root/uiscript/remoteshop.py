import uiScriptLocale

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 165,
	"height" : 24*9,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 180,
			"height" : 24*9,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 10,
					"y" : 8,

					"width" : 160,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : uiScriptLocale.REMOTE_SHOP_TITLE,
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "market",
					"type" : "button",

					"x" : 15,
					"y" : 35+5,
					"text" : "Market",
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "evlilik",
					"type" : "button",

					"x" : 15,
					"y" : 35*2+5,
					"text" : "Evlilik Magazasi",
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "silah",
					"type" : "button",

					"x" : 15,
					"y" : 35*3+5,
					"text" : "Silah Saticisi",
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "zirh",
					"type" : "button",

					"x" : 15,
					"y" : 35*4+5,
					"text" : "Zirh Saticisi",
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "balikci",
					"type" : "button",

					"x" : 15,
					"y" : 35*5+5,
					"text" : "Balikci",
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
			),
		},
	),
}

import uiScriptLocale

window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 300,
	"height" : 25*11+8,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 300,
			"height" : 25*11+8,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 284,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : "Uzaktan Market", 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},
				
				{
					"name" : "bilgitext",
					"type" : "text",

					"x" : 35,
					"y" : 245,

					"text" : "Npc Açmak Ýçin Ýstediðiniz NPC'nin Resmine Týklayabilirsiniz.",

				},
				
				{
					"name" : "market",
					"type" : "button",

					"x" : 5,
					"y" : 35,

					"default_image" : "d:/ymir work/uzaknpc/market.tga",
					"over_image" : "d:/ymir work/uzaknpc/market.tga",
					"down_image" : "d:/ymir work/uzaknpc/market.tga",
				},				
				
				{
					"name" : "zirhci",
					"type" : "button",

					"x" : 205,
					"y" : 35,

					"default_image" : "d:/ymir work/uzaknpc/zirhci.tga",
					"over_image" : "d:/ymir work/uzaknpc/zirhci.tga",
					"down_image" : "d:/ymir work/uzaknpc/zirhci.tga",
				},	
				
				
				{
					"name" : "silahci",
					"type" : "button",

					"x" : 105,
					"y" : 35,

					"default_image" : "d:/ymir work/uzaknpc/silahci.tga",
					"over_image" : "d:/ymir work/uzaknpc/silahci.tga",
					"down_image" : "d:/ymir work/uzaknpc/silahci.tga",
				},				
				
				{
					"name" : "seyyar",
					"type" : "button",

					"x" : 105,
					"y" : 135,

					"default_image" : "d:/ymir work/uzaknpc/seyyar.tga",
					"over_image" : "d:/ymir work/uzaknpc/seyyar.tga",
					"down_image" : "d:/ymir work/uzaknpc/seyyar.tga",
				},	
				
				{
					"name" : "olay",
					"type" : "button",

					"x" : 5,
					"y" : 135,

					"default_image" : "d:/ymir work/uzaknpc/olay.tga",
					"over_image" : "d:/ymir work/uzaknpc/olay.tga",
					"down_image" : "d:/ymir work/uzaknpc/olay.tga",
				},				
				
				{
					"name" : "balikci",
					"type" : "button",

					"x" : 205,
					"y" : 135,

					"default_image" : "d:/ymir work/uzaknpc/balik.tga",
					"over_image" : "d:/ymir work/uzaknpc/balik.tga",
					"down_image" : "d:/ymir work/uzaknpc/balik.tga",
				},		
			),
		},
	),
}

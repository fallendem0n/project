import uiScriptLocale

window = {
	"name" : "OfflineShopBuilder",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 185+30,
	"height" : 417+17,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 185+30,
			"height" : 417+17,
			
			"title" : "Toplu Nesne ��lemleri",

			"children" :
			(				

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 12,
					"y" : 34+5,

					"start_index" : 0,
					"x_count" : 6,
					"y_count" : 10,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				## Ok
				{
					"name" : "OkButton",
					"type" : "button",

					"x" : 21+12-4,
					"y" : 356 + 12,

					"width" : 61,
					"height" : 21,

					"text" : "@ Sil",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 21+12-4,
					"y" : 356 + 42,

					"width" : 61,
					"height" : 21,

					"text" : "S�f�rla",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "SatButton",
					"type" : "button",

					"x" : 104+14,
					"y" : 356 + 12,

					"width" : 61,
					"height" : 21,

					"text" : "$ Sat",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "VazgecButton",
					"type" : "button",

					"x" : 104+14,
					"y" : 356 + 42,

					"width" : 61,
					"height" : 21,

					"text" : "�ptal",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "bilgialkardes",
					"type" : "button",
					
					"x" : 170,
					"y" : 8,
					
					"default_image" : "d:/ymir work/ui/public/1.tga",
					"over_image" : "d:/ymir work/ui/public/2.tga",
					"down_image" : "d:/ymir work/ui/public/2.tga",
				},
			),
		},
	),
}
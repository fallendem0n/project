import uiScriptLocale

BOARD_WIDTH = 150+45*3
BOARD_HEIGHT = 200+32*2+40
SLOT_POS_X = 10+3
SLOT_POS_Y = 15
SLOT_BAR_POS_X = 76
SLOT_BAR_POS_Y = 105
PUBLIC_PATCH = "d:/ymir work/biyalog_system/biyolog/"

window = {
	"name" : "BiyologWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : BOARD_WIDTH-13,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":BOARD_WIDTH/2, "y":3, "text": "Biyolog Sistemi", "text_horizontal_align":"center" },
					),
				},
				## Item Slots 01
				{
					"name" : "BlackBoard",
					"type" : "thinboard",
					"x" : 13, "y" : 32, "width" : BOARD_WIDTH-28, "height" : BOARD_HEIGHT-67,
				},
				{
					"name" : "itemSlotImage01", "type" : "image",
					"x" : 49+SLOT_POS_X, "y" : 35+SLOT_POS_Y,
					"image" : PUBLIC_PATCH+"slot_base_01.tga",
				},
				{
					"name" : "itemSlotImage02", "type" : "image",
					"x" : 108+SLOT_POS_X, "y" : 35+SLOT_POS_Y,
					"image" : PUBLIC_PATCH+"slot_base_01.tga",
				},
				{
					"name" : "itemSlotImage03", "type" : "image",
					"x" : 167+SLOT_POS_X, "y" : 35+SLOT_POS_Y,
					"image" : PUBLIC_PATCH+"slot_base_01.tga",
				},
				{
					"name" : "itemSlot01", "type" : "grid_table", "x" : 54+SLOT_POS_X, "y" : 40+SLOT_POS_Y, "start_index" : 0,
					"x_count" : 3, "y_count" : 1, "x_step" : 32, "y_step" : 32, "x_blank" : 4+13+10, "y_blank" : 4, "horizontal_align" : "center",
				},
				## Arrows
				{
					"name" : "Image01", "type" : "image",
					"x" : 93+SLOT_POS_X, "y" : 50+SLOT_POS_Y,
					"image" : PUBLIC_PATCH+"right_arrow.tga",
				},
				{
					"name" : "Image02", "type" : "image",
					"x" : 93+59+SLOT_POS_X, "y" : 50+SLOT_POS_Y,
					"image" : PUBLIC_PATCH+"right_arrow.tga",
				},
				## Slot Bar
				{
					"name" : "slotBar01", "type" : "slotbar", "x" : SLOT_BAR_POS_X, "y" : SLOT_BAR_POS_Y+(16+5)*0,
					"width" : 55, "height": 16,
					"children" :
					(
						{ "name" : "GivenCount", "type" : "text", "text_horizontal_align":"center", "x" : 55/2, "y" : 3, "text" : "5", },
					),
				},
				{ "name" : "text011", "type" : "text", "fontname" : "Tahoma:30", "x" : SLOT_BAR_POS_X+61, "y" : SLOT_BAR_POS_Y-9, "text" : "-", },
				{
					"name" : "slotBar01", "type" : "slotbar", "x" : SLOT_BAR_POS_X+75, "y" : SLOT_BAR_POS_Y+(16+5)*0,
					"width" : 55, "height": 16,
					"children" :
					(
						{ "name" : "NeedCount", "type" : "text", "text_horizontal_align":"center", "x" : 55/2, "y" : 3, "text" : "10", },
					),
				},
				{
					"name" : "slotBar02", "type" : "slotbar", "x" : SLOT_BAR_POS_X, "y" : SLOT_BAR_POS_Y+(16+5)*1,
					"width" : 130, "height": 16,
					"children" :
					(
						{ "name" : "LeftTime", "type" : "text", "text_horizontal_align":"center", "x" : 130/2, "y" : 3, "text" : uiScriptLocale.BIYOLOG_STATE, },
					),
				},
				## Bonuses Tab
				{
					"name" : "tab01",
					"type" : "image",
					"x" : 80,
					"y" : 155,
					"image" : PUBLIC_PATCH+"tab_01.tga",
					"children" :
					(
						{ "name" : "text", "type" : "text", "text_horizontal_align":"center", "x" : 60, "y" : 5/2, "text" : uiScriptLocale.BIYOLOG_BONUSES, "color":0xFFFEE3AE },
					),
				},
				## Line
				{
					"name" : "line01", "type" : "line",
					"x" : 40, "y" : BOARD_HEIGHT-60-32*2-15, "width" : 200, "height" : 0, "color" : 0xff777777,
				},
				## Item Slots 02
				{
					"name" : "itemSlotImage04", "type" : "image",
					"x" : BOARD_WIDTH-72, "y" : BOARD_HEIGHT-134+46,
					"image" : PUBLIC_PATCH+"slot_base_02.tga",
				},
				{
					"name" : "itemSlotImage05", "type" : "image",
					"x" : 210, "y" : BOARD_HEIGHT-86,
					"image" : PUBLIC_PATCH+"slot_base_03.tga",
				},
				{
					"name" : "itemSlot02", "type" : "grid_table", "x" : BOARD_WIDTH-72, "y" : BOARD_HEIGHT-134, "start_index" : 0,
					"x_count" : 1, "y_count" : 2, "x_step" : 32, "y_step" : 32, "x_blank" : 4, "y_blank" : 4+10, "horizontal_align" : "center",
				},
				## Buttons
				{
					"name" : "GiveButton", "type" : "button",
					"x" : 52, "y" : BOARD_HEIGHT-33, "text" : uiScriptLocale.BIYOLOG_BUTTON_01,
					"default_image" : "d:/ymir work/ui/Public/xlarge_button_01.sub",
					"over_image" 	: "d:/ymir work/ui/Public/xlarge_button_02.sub",
					"down_image" 	: "d:/ymir work/ui/Public/xlarge_button_03.sub",
				},
				{
					"name" : "GiftButton", "type" : "button",
					"x" : 52, "y" : BOARD_HEIGHT-33, "text" : uiScriptLocale.BIYOLOG_BUTTON_03,
					"default_image" : "d:/ymir work/ui/Public/xlarge_button_01.sub",
					"over_image" 	: "d:/ymir work/ui/Public/xlarge_button_02.sub",
					"down_image" 	: "d:/ymir work/ui/Public/xlarge_button_03.sub",
				},
			),
		},
	),
}
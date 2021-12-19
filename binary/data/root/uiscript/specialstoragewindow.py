import uiScriptLocale

ROOT_PATH = "d:/ymir work/special_inventory/"

window = {
	"name" : "SpecialStorageWindow",
	"x" : SCREEN_WIDTH - 176 - 176,
	"y" : SCREEN_HEIGHT - 37 - 565,
	"style" : ("movable", "float",),

	"width" : 176,
	"height" : 430,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 176,
			"height" : 430,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 161,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":4, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 8,
					"y" : 35,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},
				
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 10,
					"y" : 292+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,
					
					"children" :
					[
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					],
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					#"x" : 10 + 78,
					"x" : 10 + 39,
					"y" : 292+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
					
					"children" :
					[
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					],
				},
				
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 10 + 39 + 39,
					"y" : 292+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,
					
					"children" :
					[
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					],
				},
				
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 10 + 39 + 39 + 39,
					"y" : 292+32,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,
					
					"children" :
					[
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "IV",
						},
					],
				},
				{
					"name" : "BlackBoard",
					"type" : "thinboard_circle",
					"x" : 7,
					"y" : 350,
					"width" : 162,
					"height" : 42,
				},
				{
					"name" : "Category_Tab_01",
					"type" : "radio_button",

					"x" : 20,
					"y" : 295+32+30.5,

					"default_image" : ROOT_PATH+"refine1.tga",
					"over_image" : ROOT_PATH+"refine2.tga",
					"down_image" : ROOT_PATH+"refine3.tga",
				},
					
				{
					"name" : "Category_Tab_02",
					"type" : "radio_button",

					"x" : 20+52,
					"y" : 295+32+30.5,

					"default_image" : ROOT_PATH+"book1.tga",
					"over_image" : ROOT_PATH+"book2.tga",
					"down_image" : ROOT_PATH+"book3.tga",
				},
				
				{
					"name" : "Category_Tab_03",
					"type" : "radio_button",

					"x" : 20+104,
					"y" : 295+32+30.5,

					"default_image" : ROOT_PATH+"stone1.tga",
					"over_image" : ROOT_PATH+"stone2.tga",
					"down_image" : ROOT_PATH+"stone3.tga",
				},
				{
					"name" : "InventoryMode_On",
					"type" : "radio_button",
					"x" : 25,
					"y" : 397,
					"default_image" : ROOT_PATH + "onbutton00.sub",
					"over_image" : ROOT_PATH + "onbutton01.sub",
					"down_image" : ROOT_PATH + "onbutton02.sub",
				},
				{
					"name" : "InventoryMode_Off",
					"type" : "radio_button",
					"x" : 95,
					"y" : 397,
					"default_image" : ROOT_PATH + "offbutton00.sub",
					"over_image" : ROOT_PATH + "offbutton01.sub",
					"down_image" : ROOT_PATH + "offbutton02.sub",
				},
			),
		},
	),
}
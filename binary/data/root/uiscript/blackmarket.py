import uiScriptLocale
import item
import app
import localeInfo

LOCALE_PATH = "d:/ymir work/ui/privatesearch/"
GOLD_COLOR	= 0xFFFEE3AE

BOARD_WIDTH = 280+250
BOARD_HEIGTH = 460-40
window = {
	"name" : "piyasabilgi",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGTH,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGTH,
				
			"title" : "Piyasa Limit",
			
			"children" :
			(
				
				{
					"name" : "ilkkisim",
					"type" : "thinboard_circle",
					"x" : 15,
					"y" : 32,
					"width" : 230,
					"height" : 410-40,
					
				},
				{
					"name" : "info_ScrollBar",
					"type" : "scrollbar",

					"x" : 250,
					"y" : 38,
					"size" : 36 * 10 + 5 * 9-40,
				},
				
				{
					"name" : "itemboard",
					"type" : "thinboard_circle",
					"x" : 270,
					"y" : 32,
					"width" : 245,
					"height" : 310,
					"children" :
					(
						{
							"name" : "itemslot",
							"type" : "grid_table",
							"image" : "d:/ymir work/ui/Public/Slot_Base.sub",
							"x" : 10,
							"y" : 10,
							"start_index" : 0,
							"x_count" : 7,
							"y_count" : 9,
							"x_step" : 32,
							"y_step" : 32,
						},
					),
				},
				
				{
					"name" : "infoboard",
					"type" : "thinboard_circle",
					"x" : 270,
					"y" : 32+310,
					"width" : 245,
					"height" : 100-40,
					"children" :
					(
						{
							"name" : "info_text",
							"type" : "text",
							"x" : 0,
							"y" : 8,
							
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",
							
							"text" : "Toplam Tutar",
						},
						
						{
							"name" : "won_icon",
							"type" : "image",
							# "x" : 10+25+5,
							"x" : 25+5-20,
							"y" : 33,
							
							"image" : "d:/ymir work/ui/game/windows/cheque_icon.sub",
						},
						
						{
							"name" : "won_slot",
							"type" : "image",
							# "x" : 30+25+5,
							"x" : 25+5,
							"y" : 30,
							
							"image" : "d:/ymir work/ui/public/cheque_slot.sub",
							
							"children" :
							(
								{
									"name" : "won_text",
									"type" : "text",
									"x" : 2,
									"y" : 2,
									
									
									"text" : "0",
								},
							),
						},
						
						{
							"name" : "gold_icon",
							"type" : "image",
							# "x" : 10+25+30+30,
							"x" : 25+30+30-25,
							"y" : 33,
							
							"image" : "d:/ymir work/ui/game/windows/money_icon.sub",
						},
						
						{
							"name" : "gold_slot",
							"type" : "image",
							# "x" : 30+25+30+30,
							"x" : 25+30+30-5,
							"y" : 30,
							
							"image" : "d:/ymir work/ui/public/gold_slot.sub",
							
							"children" :
							(
								{
									"name" : "gold_text",
									"type" : "text",
									"x" : 2,
									"y" : 2,
									
									
									"text" : "0",
								},
							),
						},
						
						{
							"name" : "submit",
							"type" : "button",

							"x" : 30+25+30+90,
							"y" : 30,


							"text" : "Sat",

							"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
						},
						
					),
				},
				
				{
					"name" : "RefreshSymbol",
					"type" : "ani_image",

					"x" : 15, "y" : 32,

					"images": (
						"blackmarket/loading/loading_image0.png",
						"blackmarket/loading/loading_image1.png",
						"blackmarket/loading/loading_image2.png",
						"blackmarket/loading/loading_image3.png",
						"blackmarket/loading/loading_image4.png",
						"blackmarket/loading/loading_image5.png",
						"blackmarket/loading/loading_image6.png",
						"blackmarket/loading/loading_image7.png",
						"blackmarket/loading/loading_image8.png",
						"blackmarket/loading/loading_image9.png",
						"blackmarket/loading/loading_image10.png",
						"blackmarket/loading/loading_image11.png",
						"blackmarket/loading/loading_image12.png",
						"blackmarket/loading/loading_image13.png",
						"blackmarket/loading/loading_image14.png",
						"blackmarket/loading/loading_image15.png",
						"blackmarket/loading/loading_image16.png",
						"blackmarket/loading/loading_image17.png",
					),
				},
			
			),
		},
	),
}

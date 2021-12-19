import uiScriptLocale, constInfo


X=10
Y=20
EK_X=0
EK_Y=25
BUTTON_DIR = "button_1128/"
Button1_IMG_1= BUTTON_DIR+"pazar_sistemi_1.png"
Button1_IMG_2= BUTTON_DIR+"pazar_sistemi_2.png"
Button1_IMG_3= BUTTON_DIR+"pazar_sistemi_3.png"

Button2_IMG_1 = BUTTON_DIR+"efsun_bot_1.png"
Button2_IMG_2 = BUTTON_DIR+"efsun_bot_2.png"
Button2_IMG_3 = BUTTON_DIR+"efsun_bot_3.png"

Button3_IMG_1 = BUTTON_DIR+"patron_takip_1.png"
Button3_IMG_2 = BUTTON_DIR+"patron_takip_2.png"
Button3_IMG_3 = BUTTON_DIR+"patron_takip_3.png"

Button4_IMG_1 = BUTTON_DIR+"biyolog.png"
Button4_IMG_2 = BUTTON_DIR+"biyolog2.png"
Button4_IMG_3 = BUTTON_DIR+"biyolog3.png"

Button5_IMG_1 = BUTTON_DIR+"itemsil.png"
Button5_IMG_2 = BUTTON_DIR+"itemsil2.png"
Button5_IMG_3 = BUTTON_DIR+"itemsil3.png"

Button6_IMG_1 = BUTTON_DIR+"doviz_1.png"
Button6_IMG_2 = BUTTON_DIR+"doviz_2.png"
Button6_IMG_3 = BUTTON_DIR+"doviz_3.png"


window = {
	"name" : "SystemsWindow",

	"x" : SCREEN_WIDTH - 328, #176
	"y" : SCREEN_HEIGHT - 416, #37
	
	"width" : 57, #148
	"height" : 496, #139

	"type" : "window",

	"children" :
	(
		{
			"name" : "SystemsWindowLayer",

			"x" : -15,
			"y" : 0,

			"width" : 257,
			"height" : 496,

			"children" :
			(
				{
					"name" : "SystemsWindowBoard",
					"type" : "window",
					"style" : ("attach", "float"),

					"x" : 40,
					"y" : 0,

					"width" : 148 - 9991-800,
					"height" : 496,

					"children" :
					(
						{"name":"Button1","type":"button","x":X,"y":Y+1,"default_image":Button1_IMG_1,"over_image":Button1_IMG_2,"down_image":Button1_IMG_3, "tooltip_x": -7, "tooltip_y": -14},
						{"name":"Button2","type":"button","x":X,"y":Y+EK_Y + (EK_Y*0),"default_image":Button2_IMG_1,"over_image":Button2_IMG_2,"down_image":Button2_IMG_3, "tooltip_x": 0, "tooltip_y": -14},
						{"name":"Button3","type":"button","x":X,"y":Y+EK_Y + (EK_Y*1),"default_image":Button3_IMG_1,"over_image":Button3_IMG_2,"down_image":Button3_IMG_3, "tooltip_x": 0, "tooltip_y": -14},
						{"name":"Button4","type":"button","x":X,"y":Y+EK_Y + (EK_Y*2),"default_image":Button4_IMG_1,"over_image":Button4_IMG_2,"down_image":Button4_IMG_3, "tooltip_x": 0, "tooltip_y": -14},
						{"name":"Button5","type":"button","x":X,"y":Y+EK_Y + (EK_Y*3),"default_image":Button5_IMG_1,"over_image":Button5_IMG_2,"down_image":Button5_IMG_3, "tooltip_x": 0, "tooltip_y": -14},
						{"name":"Button6","type":"button","x":X,"y":Y+EK_Y + (EK_Y*4),"default_image":Button6_IMG_1,"over_image":Button6_IMG_2,"down_image":Button6_IMG_3, "tooltip_x": 0, "tooltip_y": -14},
						),
				},
			)
		},
	),
}

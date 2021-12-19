import uiScriptLocale
astek2fingo = "yusufwork/depobutton/"
window = {
	"name" : "PasswordDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 288,
	"height" : 269,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 288,
			"height" : 269,

			"children" :
			(

				#내용
				{
					"name" : "Desc1",
					"type" : "text",

					"x" : 288/2,
					"y" : 30,

					"text" : uiScriptLocale.PASSWORD_DESC_1,
					"text_horizontal_align":"center"
				},
				#내용2
				{
					"name" : "Desc2",
					"type" : "text",

					"x" : 288/2,
					"y" : 42,

					"text" : uiScriptLocale.PASSWORD_DESC_2,
					"text_horizontal_align":"center"
				},
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,
 
					"width" : 288 - 15,
					"color" : "gray",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",

							"x" : (288 - 15) /2,
							"y" : 3,

							"text" : uiScriptLocale.PASSWORD_TITLE,
							"text_horizontal_align":"center"
						},
					),
				},
				{
					"name" : "arkaplan",
					"type" : "image",
					"image" : astek2fingo + "depo_arka.png",
					"x" : 3,
					"y" : 30,
				},
				## Password Slot
				{
					"name" : "password_slot",
					"type" : "window",

					"x" : 163,
					"y" : 126,
					#"horizontal_align" : "center",
					"width" : 60, "height" : 21,
					#"image" : "d:/ymir work/ui/public/Parameter_Slot_02.sub",

					"children" :
					(
						{
							"name" : "password_value",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 60,
							"height" : 18,

							"input_limit" : 6,
							"secret_flag" : 1,
						},
					),
				},
				{
					"name" : "normal_button",
					"type" : "radio_button",
					
					"x" : 10,
					"y" : 203,
					
					#"text" : "Depo",
							
					"default_image" : astek2fingo + "depoac1.png",
					"over_image" : astek2fingo + "depoac2.png",
					"down_image" : astek2fingo + "depoac3.png",					
				},
				{
					"name" : "nesne_button",
					"type" : "radio_button",
					
					"x" : 156,
					"y" : 203,
					
					#"text" : "N.Market",
					
					"default_image" : astek2fingo + "nesneac1.png",
					"over_image" : astek2fingo + "nesneac2.png",
					"down_image" : astek2fingo + "nesneac3.png",					
				},
				{
					"name" : "Desc3",
					"type" : "text",

					"x" : 250/2,
					"y" : 80+24,

					#"text" : uiScriptLocale.PASSWORD_DESC_3,
					"text_horizontal_align":"center"
				},
				{
					"name" : "Desc4",
					"type" : "text",

					"x" : 250/2,
					"y" : 92+24,

					#"text" : uiScriptLocale.PASSWORD_DESC_4,
					"text_horizontal_align":"center"
				},
				{
					"name" : "Desc5",
					"type" : "text",

					"x" : 250/2,
					"y" : 104+24,

					#"text" : uiScriptLocale.PASSWORD_DESC_5,
					"text_horizontal_align":"center"
				},
				## Button
				{
					"name" : "accept_button",
					"type" : "button",

					"x" : 250/2 - 61 - 5,
					"y" : 120+24,

					# "text" : uiScriptLocale.OK,

					# "default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 250/2 + 5,
					"y" : 120+24,

					# "text" : uiScriptLocale.CANCEL,

					# "default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				## EnvanterInfo
				{
					"name" : "arka",
					"type" : "image",

					"x" : 236,
					"y" : 7,

					"image" : "d:/ymir work/ui/game/mark/kose_arka.tga",
					"children" :
					(
						## EnvanterInfo
						{
							"name" : "MalzemeDeposuInfo",
							"type" : "button",

							"x" : 4,
							"y" : 4,

							"default_image" : "d:/ymir work/ui/game/mark/question_mark_1.tga",
							"over_image" : "d:/ymir work/ui/game/mark/question_mark_2.tga",
							"down_image" : "d:/ymir work/ui/game/mark/question_mark_3.tga",
						},
					),

				},
			),
		},
	),
}

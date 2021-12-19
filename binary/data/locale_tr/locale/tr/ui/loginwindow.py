import uiScriptLocale
import uiScriptLocale
import gameInfo


LOCALE_PATH = uiScriptLocale.LOGIN_PATH
SERVER_BOARD_HEIGHT = 220 + 180 - 70
SERVER_BOARD_HEIGHT2 = 220 + 180 - 70 - 120
SERVER_LIST_HEIGHT = 171 + 180 - 70
SERVER_BOARD_WEIGHT = 375 
window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(

		## Arka Planlar
		{
			"name" : "bg1", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1024.0, "y_scale" : float(SCREEN_HEIGHT) / 768.0,
			#"image" : gameInfo.CONFIG_YOL + "images/empire_chunjo.sub",
			"image" : "locale/tr/ui/serverlist.sub",
		},
		{
			"name" : "bg2", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			#"image" : "locale/tr/ui/login.sub",
			"image" : "locale/tr/ui/login.sub",
		},

		## VirtualKeyboard
		{
			'name' : 'VirtualKeyboard',
			'type' : 'thinboard',
			'x' : (SCREEN_WIDTH - 564) / 2,
			'y' : SCREEN_HEIGHT - 310,
			'width' : 564,
			'height' : 254,
			'children' : 
			(
				{
					'name' : 'key_at',
					'type' : 'toggle_button',
					'x' : 40,
					'y' : 186,
					'default_image' : 'locale/tr/ui/vkey/key_at.tga',
					'down_image' : 'locale/tr/ui/vkey/key_at_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_at_over.tga',
				},
				{
					'name' : 'key_backspace',
					'type' : 'button',
					'x' : 498,
					'y' : 186,
					'default_image' : 'locale/tr/ui/vkey/key_backspace.tga',
					'down_image' : 'locale/tr/ui/vkey/key_backspace_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_backspace_over.tga',
				},
				{
					'name' : 'key_enter',
					'type' : 'button',
					'x' : 439,
					'y' : 186,
					'default_image' : 'locale/tr/ui/vkey/key_enter.tga',
					'down_image' : 'locale/tr/ui/vkey/key_enter_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_enter_over.tga',
				},
				{
					'name' : 'key_shift',
					'type' : 'toggle_button',
					'x' : 86,
					'y' : 186,
					'default_image' : 'locale/tr/ui/vkey/key_shift.tga',
					'down_image' : 'locale/tr/ui/vkey/key_shift_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_shift_over.tga',
				},
				{
					'name' : 'key_space',
					'type' : 'button',
					'x' : 145,
					'y' : 186,
					'default_image' : 'locale/tr/ui/vkey/key_space.tga',
					'down_image' : 'locale/tr/ui/vkey/key_space_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_space_over.tga',
				},
				{
					'name' : 'key_1',
					'type' : 'button',
					'x' : 40,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_2',
					'type' : 'button',
					'x' : 80,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_3',
					'type' : 'button',
					'x' : 120,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_4',
					'type' : 'button',
					'x' : 160,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_5',
					'type' : 'button',
					'x' : 200,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_6',
					'type' : 'button',
					'x' : 240,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_7',
					'type' : 'button',
					'x' : 280,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_8',
					'type' : 'button',
					'x' : 320,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_9',
					'type' : 'button',
					'x' : 360,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_10',
					'type' : 'button',
					'x' : 400,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_11',
					'type' : 'button',
					'x' : 440,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_12',
					'type' : 'button',
					'x' : 480,
					'y' : 24,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_13',
					'type' : 'button',
					'x' : 40,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_14',
					'type' : 'button',
					'x' : 80,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_15',
					'type' : 'button',
					'x' : 120,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_16',
					'type' : 'button',
					'x' : 160,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_17',
					'type' : 'button',
					'x' : 200,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_18',
					'type' : 'button',
					'x' : 240,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_19',
					'type' : 'button',
					'x' : 280,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_20',
					'type' : 'button',
					'x' : 320,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_21',
					'type' : 'button',
					'x' : 360,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_22',
					'type' : 'button',
					'x' : 400,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_23',
					'type' : 'button',
					'x' : 440,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_24',
					'type' : 'button',
					'x' : 480,
					'y' : 63,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_25',
					'type' : 'button',
					'x' : 60,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_26',
					'type' : 'button',
					'x' : 100,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_27',
					'type' : 'button',
					'x' : 140,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_28',
					'type' : 'button',
					'x' : 180,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_29',
					'type' : 'button',
					'x' : 220,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_30',
					'type' : 'button',
					'x' : 260,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_31',
					'type' : 'button',
					'x' : 300,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_32',
					'type' : 'button',
					'x' : 340,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_33',
					'type' : 'button',
					'x' : 380,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_34',
					'type' : 'button',
					'x' : 420,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_35',
					'type' : 'button',
					'x' : 460,
					'y' : 104,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_36',
					'type' : 'button',
					'x' : 60,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_37',
					'type' : 'button',
					'x' : 100,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_38',
					'type' : 'button',
					'x' : 140,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_39',
					'type' : 'button',
					'x' : 180,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_40',
					'type' : 'button',
					'x' : 220,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_41',
					'type' : 'button',
					'x' : 260,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_42',
					'type' : 'button',
					'x' : 300,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_43',
					'type' : 'button',
					'x' : 340,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_44',
					'type' : 'button',
					'x' : 380,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_45',
					'type' : 'button',
					'x' : 420,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
				{
					'name' : 'key_46',
					'type' : 'button',
					'x' : 460,
					'y' : 144,
					'default_image' : 'locale/tr/ui/vkey/key_normal.tga',
					'down_image' : 'locale/tr/ui/vkey/key_normal_dn.tga',
					'over_image' : 'locale/tr/ui/vkey/key_normal_over.tga',
				},
			)
		},

		## Kanal Ekraný
		{
			"name" : "ConnectBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 420) / 2 + 13,
			"y" : (SCREEN_HEIGHT - 560 - 35) + 122,
			"width" : 420,
			"height" : 30,

			"children" :
			(
				{
					"name" : "ConnectName",
					"type" : "text",

					"x" : 15,
					"y" : 0,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"text" : uiScriptLocale.LOGIN_DEFAULT_SERVERADDR,
				},
				{
					"name" : "SelectConnectButton",
					"type" : "button",

					"x" : 360,
					"y" : 0,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_BUTTON,
				},
				{
					"name" : "OtoKlavyeButton",
					"type" : "button",

					"x" : 310,
					"y" : 0,
					"vertical_align" : "center",

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : "Klavye",
				},
			),
		},

		## Login Ekraný
		{
			"name" : "LoginBoard",
			"type" : "image",

			"x" : (SCREEN_WIDTH - 420) / 2 + 300 + 150 + 20 + 8 - 150 - 40 + 40 + 70 + 80 - 250 - 130 - 50 - 35,
			"y" : (SCREEN_HEIGHT - 660 - 35) + 256,

			"image" : LOCALE_PATH + "loginwindow.sub",

			"children" :
			(
				{
					"name" : "ID_EditLine",
					"type" : "editline",

					"x" : 77,
					"y" : 16,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				{
					"name" : "Password_EditLine",
					"type" : "editline",

					"x" : 77,
					"y" : 43,

					"width" : 120,
					"height" : 18,

					"input_limit" : 16,
					"secret_flag" : 1,
					"enable_codepage" : 0,

					"r" : 1.0,
					"g" : 1.0,
					"b" : 1.0,
					"a" : 1.0,
				},
				
				{
					"name" : "idButton",
					"type" : "button",

					"x" : 77+90+10,
					"y" : 16,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",

					"tooltip_text" : uiScriptLocale.LOGIN_IDSILEBILIRSIN,
				},
				
				{
					"name" : "sifreButton",
					"type" : "button",

					"x" : 77+90+10,
					"y" : 43,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",

					"tooltip_text" : uiScriptLocale.LOGIN_SIFRESILEBILIRSIN,
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x" : 12,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",

					"text" : uiScriptLocale.LOGIN_CONNECT,
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x" : 138,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",

					"text" : uiScriptLocale.LOGIN_EXIT,
				},
				{
					"name" : "KaydetConnectButton",
					"type" : "button",

					"x" : 75,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",

					"text" : "Kaydet",
				},
			),
		},
		
		## Kayýtlý Hesaplar
		{
			"name" : "KayitBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - -5) / 2 + 13,
			"y" : (SCREEN_HEIGHT - 660 - 35) + 256,
			"width" : 208,
			"height" : 97,

			"children" :
			(
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 100,
					"y" : 15,
					'text': 'Kayýtlý Hesaplarýn',
					'text_horizontal_align': 'center'
				},
				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 185,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 184,
					"height" : 0,
					"color" : 0xff111111,
				},
				{
					"name" : "K1Button",
					"type" : "button",

					"x" : 15,
					"y" : 40,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_BOS,
				},
				
				{
					"name" : "K2Button",
					"type" : "button",

					"x" : 109,
					"y" : 40,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_BOS,
				},
				
				{
					"name" : "K3Button",
					"type" : "button",

					"x" : 15,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_BOS,
				},
				
				{
					"name" : "K4Button",
					"type" : "button",

					"x" : 109,
					"y" : 65,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

					"text" : uiScriptLocale.LOGIN_BOS,
				},
				
				{
					"name" : "S1Button",
					"type" : "button",

					"x" : 85,
					"y" : 43,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",

					"tooltip_text" : "Slot-1'i silebilirsiniz.",
				},
				
				{
					"name" : "S2Button",
					"type" : "button",

					"x" : 179,
					"y" : 43,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",

					"tooltip_text" : "Slot-2'yi silebilirsiniz.",
				},
				
				{
					"name" : "S3Button",
					"type" : "button",

					"x" : 85,
					"y" : 68,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",

					"tooltip_text" : "3.Slotu silebilirsiniz.",
				},
				
				{
					"name" : "S4Button",
					"type" : "button",

					"x" : 179,
					"y" : 68,

					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",

					"tooltip_text" : "4.Slotu silebilirsiniz.",
				},
				
			),
				
		},
		## Kanal Seçme Ekraný
		{
			"name" : "ServerBoard",
			"type" : "thinboard",

			"x" : 122,
			"y" : 222,
			"width" : 255,
			"height" : 212,
			"horizontal_align" : "center",

			"children" :
			(

				## Title
				{
					"name" : "Title",
					"type" : "text",

					"x" : 0,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text" : uiScriptLocale.LOGIN_SELECT_TITLE,
				},

				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 234,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 235,
					"height" : 0,
					"color" : 0xff111111,
				},

				## Vertical
				{
					"name" : "VerticalLine1",
					"type" : "line",

					"x" : 126,
					"y" : 38,
					"width" : 0,
					"height" : 170,
					"color" : 0xff777777,
				},
				{
					"name" : "VerticalLine2",
					"type" : "line",

					"x" : 127,
					"y" : 38,
					"width" : 0,
					"height" : 170,
					"color" : 0xff111111,
				},

				## ListBox
				{
					"name" : "ServerList",
					"type" : "listbox2",

					"x" : 10,
					"y" : 40,
					"width" : 112,
					"height" : SERVER_LIST_HEIGHT,
					"row_count" : 18,
					"item_align" : 0,
				},
				{
					"name" : "ChannelList",
					"type" : "listbox",

					"x" : 132,
					"y" : 40,
					"width" : 112,
					"height" : SERVER_LIST_HEIGHT,

					"item_align" : 0,
				},

				## Buttons
				{
					"name" : "ServerSelectButton",
					"type" : "button",

					"x" : 197,
					"y" : 186,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : "Giriþ",
				},
				{
					"name" : "ServerExitButton",
					"type" : "button",

					"x" : 147,
					"y" : 186,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",

					"text" : uiScriptLocale.LOGIN_SELECT_EXIT,
				},
		## Kanal Ekraný
		{
			"name" : "Show",
			"type" : "thinboard",

			"x" : -242,
			"y" : 0,
			"width" : 218,
			"height" : 212,
			"horizontal_align" : "center",

			"children" :
			(
				## Title
				{
					"name" : "Title",
					"type" : "text",

					"x" : 0,
					"y" : 12,
					"horizontal_align" : "center",
					"text_horizontal_align" : "center",
					"text" : "Duyuru",
				},

				## Horizontal
				{
					"name" : "HorizontalLine1",
					"type" : "line",

					"x" : 10,
					"y" : 34,
					"width" : 196,
					"height" : 0,
					"color" : 0xff777777,
				},
				{
					"name" : "HorizontalLine2",
					"type" : "line",

					"x" : 10,
					"y" : 35,
					"width" : 198,
					"height" : 0,
					"color" : 0xff111111,
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 40,
					'text': 'Hesap bilgileriniz size özeldir. Hiç bir',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 50,
					'text': 'oyun yöneticisi sizden hesap bilgilerinizi',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 60,
					'text': 'istemez. Böyle durumla karþýlaþýrsanýz',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 70,
					'text': 'kesinlikle hesap bilgisi vermeyiniz.Aksi',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 80,
					'text': 'halde hesabýnýz baþka kiþilerin eline',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 90,
					'text': 'geçmiþ olacaktýr. Bu durumdan kesinlikle',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 100,
					'text': 'yöneticilerimiz sorumlu tutulmayacaktýr.',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 110,
					'text': 'Hesap bilgilerinizi www.siverp2.com',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 120,
					'text': 'sitesine girdiðinizden adres çubuðunu',
				},
				{	
					'name': 'Warning',
					'type': 'text',
					"x" : 10,
					"y" : 130,
					'text': 'kontrol ederek emin olunuz.',
				},
			),

		},

			),

		},

	),
}

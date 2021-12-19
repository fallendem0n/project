import app
import localeInfo

WINDOW_WIDTH	= 423
WINDOW_HEIGHT	= 480

try:
	ENABLE_WOLFMAN_CHARACTER = app.ENABLE_WOLFMAN_CHARACTER
except:
	ENABLE_WOLFMAN_CHARACTER = 0

try:
	ENABLE_CHEQUE_SYSTEM = 1
except:
	ENABLE_CHEQUE_SYSTEM = 1




SEARCH_AND_FILTER_BACKGROUND = "offlineshop/searchfilter/base_image_lycan.png"
SAFEBOX_WITHDRAW_BUTTON	= "offlineshop/safebox/withdrawyang_%s.png"

if ENABLE_WOLFMAN_CHARACTER:
	SEARCH_AND_FILTER_BACKGROUND = "offlineshop/searchfilter/base_image_lycan.png"

if ENABLE_CHEQUE_SYSTEM:
	SAFEBOX_WITHDRAW_BUTTON = "offlineshop/safebox/withdrawyang_%s_cheque.png"




if ENABLE_CHEQUE_SYSTEM:
	SAFEBOX_CHILDREN = (
		{
			"name" : "BackGroundSafebox01",
			"type" : "thinboard_circle",

			"x" : 9,
			"y" : 46,

			"width" : 398,
			"height" : 55,
			"children" :
			(
				{
					"name" : "BarItem",
					"type" : "expanded_image",
					"style" : ("attach",),

					"x" : 0,
					"y" : 5,
					"image" : "d:/ymir work/ui/minigame/fish_event/fish_special_slot.sub",
					
					"children" :
					(
						{
							"name" : "BarItemSlot",
							"type" : "image",

							"x" : 7,
							"y" : 7,
							"width" : 32,
							"height" : 32,

							"image" : "icon/item/money.tga",
						},
						{
							"name" : "titleimage1",
							"type" : "image",

							"x" : 44,
							"y" : 3,

							"image" : "d:/ymir work/ui/pet/feed_button/feed_button_default.sub",
							"children" :
							(
								{
									"name" : "yazi1",
									"type" : "text",
									"text" : "Yang",
									"x" : 0, "y" : -1,
									"all_align" : "center",
								},
								{
									"name" : "item1countbar",
									"type" : "slotbar",
									"x" : 1,
									"y" : 20,
									"width" : 115,
									"height" : 18,
									"children" :
									(
										{
											"name" : "ShopSafeboxValuteText",
											"type" : "text",

											"x" : 0,
											"y" : -2,

											"all_align" : "center",
											"text" : "000000",
										},
									),
								},
							),
						},
					),
				},
########################################################################################################################################################
				{
					"name" : "SuItem",
					"type" : "expanded_image",
					"style" : ("attach",),

					"x" : 165,
					"y" : 5,
					"image" : "d:/ymir work/ui/minigame/fish_event/fish_special_slot.sub",
					
					"children" :
					(
						{
							"name" : "SuItemSlot",
							"type" : "image",

							"x" : 7,
							"y" : 7,
							"width" : 32,
							"height" : 32,

							"image" : "icon/item/80020.tga",
						},
						{
							"name" : "titleimage2",
							"type" : "image",

							"x" : 44,
							"y" : 3,

							"image" : "d:/ymir work/ui/pet/feed_button/feed_button_default.sub",
							"children" :
							(
								{
									"name" : "yazi1",
									"type" : "text",
									"text" : "Won",
									"x" : 0, "y" : -1,
									"all_align" : "center",
								},
								{
									"name" : "item2countbar",
									"type" : "slotbar",
									"x" : 1,
									"y" : 20,
									"width" : 115,
									"height" : 18,
									"children" :
									(
										{
											"name" : "ShopSafeboxValuteTextCheque",
											"type" : "text",

											"x" : 0,
											"y" : -2,

											"all_align" : "center",
											"text" : "000000",
										},
									),
								},
							),
						},
					),
				},


				{
					"name" : "ShopSafeboxWithdrawYangButton",
					"type" : "button",

					"x" : 335,
					"y" : 18,
					"text" : "Aktar",
					"fontsize" : "LARGE",

					"default_image" : "yusufwork/stop_switch_hover.png",
					"over_image" : "yusufwork/stop_switch_norm.png",
					"down_image" : "yusufwork/stop_switch_down.png",
				},
			),
		},
		{
			"name" : "GridBackground",
			"type" : "thinboard_circle",

			"x" : 9,
			"y" : 46 + 55 + 10,

			"width" : 398,
			"height" : 325,
		},
	)

else:
	SAFEBOX_CHILDREN = (
		# {
			# "name": "BackgroundShopSafeboxPage",
			# "type": "image",

			# "x": 0, "y": 0,

			# "image": "offlineshop/safebox/safebox_base_image.png",
		# },
		{
			"name" : "ShopSafeboxWithdrawYangButton",
			"type" : "button",

			"x" : 447-205 - 100,
			"y" : 16-4,

			"default_image" :  SAFEBOX_WITHDRAW_BUTTON%"default",
			"over_image" 	:  SAFEBOX_WITHDRAW_BUTTON%"over",
			"down_image" 	:  SAFEBOX_WITHDRAW_BUTTON%"down",
		},

		{
			"name" : "ShopSafeboxValuteText",
			"type" : "text",

			"x" : 468-154 - 100,
			"y" : 22-8,

			"text_horizontal_align" : "center",
			"text" : "000000",
		},
	)






window = {

	"name" : "OfflineshopBoard",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2  - WINDOW_WIDTH/2,
	"y" : SCREEN_HEIGHT/2  - WINDOW_HEIGHT/2,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "MainBoard",
			"type" : "dragonboard",
			
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,
			
			"width" 	: WINDOW_WIDTH,
			"height" 	: WINDOW_HEIGHT,
			
			"children" : 
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					
					"x" : 8,
					"y" : 7,
					
					"width"  : WINDOW_WIDTH - 16,
					"color"  : "red",
					
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"Offline Shop", "all_align":"center" },
					),
				},





				#MyShop_noShop
				{
					"name" : "MyShopBoardNoShop",
					"type" : "window",
					
                    "width" :  622,  "height" :  567,

                    "x" : 3, "y" : 28,
					
					"children":
					(

						{
							"name" : "BackGroundCreate",
							"type" : "thinboard_circle",

							"x" : 9,
							"y" : 46,

							"width"     : 398,
							"height"     : 55,
							"children" :
							(
								{
									"name" : "Day",
									"type" : "text",
									"text" : "Gün : ",
									"x" : 5,
									"y" : 5,
									"fontsize" : "LARGE",
								},
								{
									"name" : "Clock",
									"type" : "text",
									"text" : "Saat : ",
									"x" : 5,
									"y" : 30,
									"fontsize" : "LARGE",
								},
								{
									"name" : "Days_Slotbar",
									"type" : "slotbar",
									"width" : 22,
									"height" : 18,
									"x" : 50+37 -11, "y" : 5,
								},
								{
									"name" : "DaysCountText",
									"type" : "text",
									
									"text" : "0",
									"text_horizontal_align" : "center",
									"x" : 50 + 37, "y" :5,
									"fontsize" : "LARGE",
								},

								{
									"name" : "IncreaseDaysButton",
									"type" : "button",
									

									"x" :50 + 37 + 23,
									"y" : 4,

											"default_image" : "offlineshop/button_scroll_right.tga",
											"over_image"     : "offlineshop/button_scroll_right_hover.tga",
											"down_image"     : "offlineshop/button_scroll_right_active.tga",
								},
								
								
								{
									"name" : "DecreaseDaysButton",
									"type" : "button",
									
									"x" : 50,
									"y" : 4,
									
											"default_image" : "offlineshop/button_scroll_left.tga",
											"over_image"     : "offlineshop/button_scroll_left_hover.tga",
											"down_image"     : "offlineshop/button_scroll_left_active.tga",
								},
								{
									"name" : "Hours_Slotbar",
									"type" : "slotbar",
									"width" : 22,
									"height" : 18,
									"x" : 50+37 -11, "y" : 30,
								},
								{
									"name" : "HoursCountText",
									"type" : "text",
									
									"text" : "0",
									"text_horizontal_align" : "center",
									"x" : 50 + 37, "y" : 30,
									"fontsize" : "LARGE",
								},
								{
									"name" : "IncreaseHoursButton",
									"type" : "button",
									
									"x" : 50 +37 + 23,
									"y" : 29,
									
											"default_image" : "offlineshop/button_scroll_right.tga",
											"over_image"     : "offlineshop/button_scroll_right_hover.tga",
											"down_image"     : "offlineshop/button_scroll_right_active.tga",
								},
								
								
								{
									"name" : "DecreaseHoursButton",
									"type" : "button",
									
									"x" : 50,
									"y" : 29,
									
											"default_image" : "offlineshop/button_scroll_left.tga",
											"over_image"     : "offlineshop/button_scroll_left_hover.tga",
											"down_image"     : "offlineshop/button_scroll_left_active.tga",
								},
								{
									"name" : "Nameslotbar",
									"type" : "slotbar",
									"width" : 200,
									"height" : 20,
									"x" : 160, "y" : 24,
									"children" :
									(
										{
											"name" : "ShopNameInfo",
											"type" : "text",
											"text" : "<- Pazar Ýsmi Belirle -> ",
											"all_align" : "center",
											"x" : 0,
											"y" : -21,
											"fontsize" : "LARGE",
										},
										{
											"name" : "ShopNameInput",
											"type" : "editline",
											
											"width" : 187 , "height" : 15 ,
											
											"input_limit" : 35,
											"x" : 3, "y" : 2,
										},
									),
								},

							),
						},

						{
							"name" : "GridBackground",
							"type" : "thinboard_circle",

							"x" : 9,
							"y" : 46 + 55 + 10,

							"width" : 398,
							"height" : 325,
						},

						#next button
						{
							"name" : "CreateShopButton",
							"type" : "button",
							
							"x" : 300+80,
							"y" : 72,
							
                                    "default_image" : "yusufwork/checkbutton.dds",
                                    "over_image" : "yusufwork/checkbutton_over.dds",
                                    "down_image" : "yusufwork/checkbutton_down.dds",

                                    "tooltip_text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CREATE_TEXT,
						}
					),
				},




				#MyShop_Owner
				{
					"name" : "MyShopBoard",
					"type" : "window",
					
                    "width" :  622,  "height" :  567,

                    "x" : 3, "y" : 28,
					
					"children":
					(

						
                        {
                            "name" : "arkaboard_2",
                            "type" : "thinboard_circle",
                            "x" : 55,
                            "y" : 55,
                            "width" : 300,
                            "height" : 40,
                            "children":
                            (
                                {
                                    "name" : "MyShopShopTitle",
                                    "type" : "text",
                                    
                                    "x" : 53, "y" : 5,
                                    
                                    "text" : "title",
                                    "text_horizontal_align" : "center",
                                },
						
                                {
                                    "name" : "MyShopEditTitleButton",
                                    "type" : "button",
                                    
                                    "x" : 110, "y" : 8,
                                    
                                    "tooltip_text"	: localeInfo.OFFLINESHOP_EDIT_SHOPNAME_TOOLTIP,
                                    
                                    "default_image" : "offlineshop/myshop/editname_default.png",
                                    "over_image" 	: "offlineshop/myshop/editname_over.png",
                                    "down_image" 	: "offlineshop/myshop/editname_down.png",
                                },
                                
                                {
                                    "name": "LargeGuildMarkSlot",
                                    "type": "image",
                                    "x":258,
                                    "y": 4,
                                    "image": "offlineshop/clock.png",
                                    "children":
                                    (
                                        {
                                            "name" : "MyShopShopDuration",
                                            "type" : "text",
                                            
                                            "x" : -50, "y" : 0,
                                            
                                            "text" : "99 days",
                                            "text_horizontal_align" : "center",
                                        },
                                    ),

                                },
                            ),
                        },

						{
							"name" : "MyShopCloseButton",
							"type" : "button",
							
							"x": 160, "y": 105,
							
							"default_image" : "offlineshop/shopsearchp2p/small_btn.dds",
							"over_image" 	: "offlineshop/shopsearchp2p/small_btn_over.dds",
							"down_image" 	: "offlineshop/shopsearchp2p/small_btn_down.dds",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CLOSE_SHOP_TEXT,
							"tooltip_text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CLOSE_SHOP_TEXT,
						},

					),
				},



				#shoplist_open
				{
					"name" : "ListOfShop_OpenShop",
					"type" : "window",
					
					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,
					
					"children":
					(
						# {
							# "name" : "BackgroundShopListOpen",
							# "type" : "image",
							
							# "x" : 0, "y" : 0,
							
							# "image" : "offlineshop/shoplist/base_image_open.png",
						# },
						{
							"name" : "OpenShopShopOwnerButton",
							"type" : "button",

							"x" : 420, "y" : 5,

							"default_image" : "offlineshop/input.tga",
							"over_image" : "offlineshop/input.tga",
							"down_image" : "offlineshop/input.tga",

							"text" : "title",
							"text_horizontal_align" : "center",
							"r": 0.525,
							"g": 0.475,
							"b": 0.451
						},
						{
							"name" : "OpenShopBackToListButton",
							"type" : "button",
							
							"x" : 15, "y" : 5,
							
							"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CLOSE_SHOP_TEXT,
						},
						{
							"name" : "OpenShopShopTitle",
							"type" : "text",
							
							"x" : 328, "y" : 6,

							"text_horizontal_align" : "center",
							"text" : "title",
						},
						
						{
							"name" : "OpenShopShopDuration",
							"type" : "text",
							
							"x" : 328, "y" : 27,

							"text_horizontal_align" : "center",
							"text" : "99 days",
						},
					),
				},


				#shoplist_list
				{
					"name" : "ListOfShop_List",
					"type" : "window",
					
					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,
					# "children":
					# (
						# {
							# "name" : "BackgroundShopList",
							# "type" : "image",
							
							# "x" : 0, "y" : 0,
							
							#"image" : "offlineshop/shoplist/base_image_list.png",
						# },
					# ),
				},



				#searchhistory
				{
					"name" : "SearchHistoryBoard",
					"type" : "window",
					
					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,
					# "children":
					# (
						# {
							# "name" : "BackgroundSearchHistory",
							# "type" : "image",
							
							# "x" : 0, "y" : 0,
							
							# "image" : "offlineshop/searchhistory/base_image.png",
						# },
					# ),
				},


				#mypatterns
				{
					"name" : "MyPatternsBoard",
					"type" : "window",
					
					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,
					# "children":
					# (
						# {
							# "name" : "BackgroundMyPatterns",
							# "type" : "image",
							
							# "x" : 0, "y" : 0,
							
							# "image" : "offlineshop/mypatterns/base_image.png",
						# },
					# ),
				},




				#searchfilter
				{
					"name" : "SearchFilterBoard",
					"type" : "window",
					
                    "width" :  450,  "height" :  480,

                    "x" : 3, "y" : 28,
					"children":
					(

                        {
                            "name" : "SearchFilterBoardChild01",
                            "type" : "thinboard_circle",

                            "x" : 9,
                            "y" : 46,

                            "width"     : 398,
                            "height"     : 55
                        },

                        {
                            "name" : "SearchFilterBoardChild07",
                            "type" : "thinboard_circle",

                            "x" : 9,
                            "y" : 46 + 59,

                            "width"     : 398,
                            "height"     : 340,
                        },
                        {
                            "name" : "SearchFilterItemNameInputContainer",
                            "type" : "slotbar",
							"width" : 398 - 126,
							"height" : 20,
                            "x" : 13, "y" : 31 + 41,

                            "children" :
                            (
                                {
                                    "name" : "searchinfo",
                                    "type" : "text",

                                    "x" : 1, "y" : -20,
									"text" : "<- Satýn almak istediðiniz eþyanýn adýný yazarak aramayý baþlatabilirsiniz ->",
									"fontsize" : "LARGE",
                                },
                                {
                                    "name" : "SearchFilterItemNameInput",
                                    "type" : "editline",

                                    "width" : 398 - 126, "height" : 20,

                                    "input_limit" : 24,
                                    "x" : 5, "y" : 3,
                                },
                            )
                        },

                        # {
                            # "name" : "SearchFilterItemNameInputContainer",
                            # "type" : "image",

                            # "x" : 13, "y" : 31 + 43 + 21,

                            # "image" : "offlineshop/yarramiye.tga"
                        # },

                        # {
                            # "name" : "SearchFilterTypeContainer",
                            # "type" : "image",

                            # "x" : 13, "y" : 29 + 43+75*2,

                            # "image" : "offlineshop/yarramiye.tga"
                        # },

                        # {
                            # "name" : "SearchFilterSubtypeContainer",
                            # "type" : "image",

                            # "x" : 13, "y" : 50 + 45+75*2,

                            # "image" : "offlineshop/yarramiye.tga"
                        # },
						{
							"name" : "SearchFilterItemLevelStart",
							"type" : "editline",
							
							"width" : 43, "height" : 14,
							
							"input_limit" : 3,
							"only_number" : 1,
							"x" : 363, "y" : 32,
						},
						
						
						
						{
							"name" : "SearchFilterItemLevelEnd",
							"type" : "editline",
							
							"width" : 43, "height" : 14,
							
							"input_limit" : 3,
							"only_number" : 1,
							"x" : 363, "y" : 52,
						},
						
						
						{
							"name" : "SearchFilterItemYangMin",
							"type" : "editline",
							
							"width" : 130, "height" : 15,
							
							"input_limit" : len("999999999999999999"),
							"only_number" : 1,
							"x" : 258, "y" : 103,
						},
						
						
						
						{
							"name" : "SearchFilterItemYangMax",
							"type" : "editline",
							
							"width" : 130, "height" : 15,
							
							"input_limit" : len("999999999999999999"),
							"only_number" : 1,
							"x" : 258, "y" : 127,
						},
						
						
						
						
						
						{
							"name" : "SearchFilterResetFilterButton",
							"type" : "button",
							
							"x" : 400, "y" : 482,
							
							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_RESET_FILTER_TEXT,
						},
						
						
						
						{
							"name" : "SearchFilterSavePatternButton",
							"type" : "button",
							
							"x" : 139, "y" : 482,
							
							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_SAVE_AS_PATTERN_TEXT,
						},
						
						
						{
							"name" : "SearchFilterStartSearch",
							"type" : "button",
							
							"x" : 300, "y" : 73,
							
                            "default_image" : "yusufwork/apply_norm.tga",
                            "over_image" : "yusufwork/apply_hover.tga",
                            "down_image" : "yusufwork/apply_down.tga",

							# "text" : localeInfo.OFFLINESHOP_SCRIPTFILE_START_SEARCH_TEXT,
						},
						
						{
							"name" : "SearchFilterAttributeButton1",
							"type" : "button",
							
							"x" : 406, "y" : 35,
							
							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},
						
						
						
						{
							"name" : "SearchFilterAttributeButton2",
							"type" : "button",
							
							"x" : 406, "y" : 35+22,
							
							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},
						
						
						
						{
							"name" : "SearchFilterAttributeButton3",
							"type" : "button",
							
							"x" : 406, "y" : 35+22*2,
							
							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},
						
						
						{
							"name" : "SearchFilterAttributeButton4",
							"type" : "button",
							
							"x" : 406, "y" : 35+22*3,
							
							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},
						
						
						{
							"name" : "SearchFilterAttributeButton5",
							"type" : "button",
							
							"x" : 406, "y" : 35+22*4,
							
							"default_image" : "offlineshop/searchfilter/attribute_default.png",
							"over_image" 	: "offlineshop/searchfilter/attribute_over.png",
							"down_image" 	: "offlineshop/searchfilter/attribute_down.png",
						},
						{
							"name" : "ContainerScrollBar",
							"type" : "slimscrollbar",

							"x" : 599 - 205,
							"y" : 46 + 59,
							"size" : 340,
						},
					),
				},



				#safebox
				{
					"name": "ShopSafeboxPage",
					"type": "window",

                    "width" :  622,  "height" :  567,

                    "x" : 3, "y" : 28,
					"children":
					(
						SAFEBOX_CHILDREN
					),
				},




				#my offers
				{
					"name": "MyOffersPage",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,

					# "children":
					# (
						# {
							# "name": "BackgroundMyOffersPage",
							# "type": "image",

							# "x": 0, "y": 0,

							# "image": "offlineshop/myoffers/base_image.png",
						# },
					# ),
				},




				# my auction
				{
					"name": "MyAuction",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,

					"children":
					(
						# {
							# "name": "BackgroundMyAuctionPage",
							# "type": "image",

							# "x": 0, "y": 0,

							# "image": "offlineshop/myauction/base_image.png",
						# },

						{
							"name" : "MyAuction_OwnerName",
							"type" : "text",

							"x" : 235+67, "y" : 100-70,
							"text_horizontal_align" : "center",
							"text" : " noname ",
						},

						{
							"name" : "MyAuction_Duration",
							"type" : "text",

							"x" : 235+67, "y" : 145-91,
							"text_horizontal_align" : "center",
							"text" : " noname ",
						},

						{
							"name" : "MyAuction_BestOffer",
							"type" : "text",

							"x" : 235+67, "y" : 197-123,
							"text_horizontal_align" : "center",
							"text" : " noname ",
						},

						{
							"name": "MyAuction_MinRaise",
							"type": "text",

							"x": 235+67, "y": 243-147,
							"text_horizontal_align": "center",
							"text": " noname ",
						},
					),
				},




				# open acution
				{
					"name": "OpenAuction",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,

					"children":
					(
						#{
							# "name": "BackgroundOpenAuctionPage",
							# "type": "image",

							# "x": 0, "y": 0,

							# "image": "offlineshop/openauction/base_image.png",
						# },

						{
							"name": "OpenAuctionBackToListButton",
							"type": "button",

							"x": 15, "y": 5,

							"default_image": "d:/ymir work/ui/public/middle_button_01.sub",
							"over_image": "d:/ymir work/ui/public/middle_button_02.sub",
							"down_image": "d:/ymir work/ui/public/middle_button_03.sub",

							"text": localeInfo.OFFLINESHOP_SCRIPTFILE_CLOSE_AUCTION_TEXT,
						},

						{
							"name": "OpenAuction_OwnerName",
							"type": "text",

							"x" : 235+67, "y" : 100-70,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

						{
							"name": "OpenAuction_Duration",
							"type": "text",

							"x" : 235+67, "y" : 145-91,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

						{
							"name": "OpenAuction_BestOffer",
							"type": "text",

							"x": 235+67, "y": 197-123,
							"text_horizontal_align": "center",
							"text": " noname ",
						},

						{
							"name": "OpenAuction_MinRaise",
							"type": "text",

							"x": 235+67, "y": 243-147,
							"text_horizontal_align": "center",
							"text": " noname ",
						},
					),
				},




				# acutionlist
				{
					"name": "AuctionList",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,

					# "children":
					# (
						# {
							# "name": "BackgroundAuctionListPage",
							# "type": "image",

							# "x": 0, "y": 0,

							# "image": "offlineshop/auctionlist/base_image.png",
						# },
					# ),
				},



				#create auction
				{
					"name": "CreateAuction",
					"type": "window",

					"width" :  622,  "height" :  544,

					"x" : 3, "y" : 78,

					"children":
					(
						# {
							# "name": "BackgroundCreateAuctionPage",
							# "type": "image",

							# "x": 0, "y": 0,

							# "image": "offlineshop/createauction/base_image.png",
						# },
						{
							"name": "CreateAuctionDaysInput",
							"type": "text",

							"width": 23, "height": 17,

							"text_horizontal_align" : "center",
							"text" : "0",
							"x": 299, "y": 181,
						},
						{
							"name": "CreateAuctionStartingPriceInput",
							"type": "editline",

							"width": 122, "height": 15,

							"input_limit": 10,
							"only_number": 1,
							"x": 272, "y": 210,
						},

						{
							"name": "CreateAuctionDecreaseDaysButton",
							"type": "button",

							"x": 325,
							"y": 183,

                                    "default_image" : "offlineshop/button_scroll_right.tga",
                                    "over_image"     : "offlineshop/button_scroll_right_hover.tga",
                                    "down_image"     : "offlineshop/button_scroll_right_active.tga",
						},


						{
							"name" : "CreateAuctionIncreaseDaysButton",
							"type" : "button",

							"x" : 267-2,
							"y" : 183,

                                    "default_image" : "offlineshop/button_scroll_left.tga",
                                    "over_image"     : "offlineshop/button_scroll_left_hover.tga",
                                    "down_image"     : "offlineshop/button_scroll_left_active.tga",
						},

						{
							"name" : "CreateAuctionCreateAuctionButton",
							"type" : "button",

							"x" : 211+98, "y" : 267-33,

                                    "default_image" : "offlineshop/button.tga",
                                    "over_image" : "offlineshop/button_hover.tga",
                                    "down_image" : "offlineshop/button_active.tga",

							"text" : localeInfo.OFFLINESHOP_SCRIPTFILE_CREATE_TEXT,
						}
					),
				},

				{
					"name" : "Menu",
					"type" : "window",
					
					"x" : 13,
					"y" : 34,

					"width" : 417 - 26,
					"height" : 40,

					"children":
					(
					
						# Back Button
						{
							"name": "SearchFilterButton",
							"type": "button",

							"x": 417 - 26 - (45*2), "y": 10,

							"tooltip_text" : "Eþya Arama",

							"default_image" : "offlineshop/shopsearchp2p/4.png",
							"over_image" : "offlineshop/shopsearchp2p/4.png",
							"down_image" : "offlineshop/shopsearchp2p/4.png",
							
						},
						
						{
							"name": "MyShopButton",
							"type": "button",

							"x": 417 - 26 - (45*3), "y": 10,

							"tooltip_text" : "Pazar",

							"default_image" : "offlineshop/shopsearchp2p/2.png",
							"over_image" : "offlineshop/shopsearchp2p/2_1.png",
							"down_image" : "offlineshop/shopsearchp2p/2_2.png",
						},

						{
							"name": "ListOfShopButton",
							"type": "button",

							"x": 90, "y": 10,

							"tooltip_text" : "Pazar Listesi",

							"default_image" : "offlineshop/shopsearchp2p/pazarliste.png",
							"over_image" : "offlineshop/shopsearchp2p/pazarliste2.png",
							"down_image" : "offlineshop/shopsearchp2p/pazarliste3.png",
						},
						
						{
							"name": "ShopSafeboxButton",
							"type": "button",

							"x": 417 - 26 - 45, "y": 10,

							"tooltip_text" : "Depo",

							"default_image" : "offlineshop/shopsearchp2p/3.png",
							"over_image" : "offlineshop/shopsearchp2p/3_1.png",
							"down_image" : "offlineshop/shopsearchp2p/3_2.png",
						},
						

						{
							"name": "SearchHistoryButton",
							"type": "button",

							"x": 170, "y": 10,

							"tooltip_text" : "Arama Geçmisi",

							"default_image" : "offlineshop/shopsearchp2p/gecmis.png",
							"over_image" : "offlineshop/shopsearchp2p/gecmis2.png",
							"down_image" : "offlineshop/shopsearchp2p/gecmis3.png",
						},

						{
							"name": "MyPatternsButton",
							"type": "button",

							"x": 210, "y": 10,

							"tooltip_text" : "Kayýtlý Aramalar",

							"default_image" : "offlineshop/shopsearchp2p/kaydet.png",
							"over_image" : "offlineshop/shopsearchp2p/kaydet2.png",
							"down_image" : "offlineshop/shopsearchp2p/kaydet3.png",
						},

					
						
					),
				},

			),
		},
	),
}














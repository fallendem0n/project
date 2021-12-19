import localeInfo


window = {
	"name" : "RemoveItemWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH / 2 - 170,
	"y" : SCREEN_HEIGHT / 2 - 133,

	"width" : 339,
	# "height" : 25*11+8,
	"height" : 222 + 45,


	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			# "width" : 300 + 140 + 10 + 20 + 148,
			"width" : 339,
			"height" : 222 + 45,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 5,
					"y" : 6,

					"width" : 339-12,
					"color" : "gray",

					"children" :
					(
						{ "name":"titlename", "type":"text", "x":0, "y":3, 
						"text" : "Siverp2 - Toplu Item Silme", 
						"horizontal_align":"center", "text_horizontal_align":"center" },
					),
				},

				{
					"name" : "itemslot",
					"type" : "grid_table",
					"x" : 8,
					"y" : 30,
					"start_index" : 0,
					"x_count" : 10,
					"y_count" : 6,
					"x_step" : 32,
					"y_step" : 32,
					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},

				{
					"name" : "ItemSilmeButonu",
					"type" : "button",

					"x" : 96,
					"y" : 222 + 10,

					"text": "Itemleri Sil",

					"default_image" : "d:/ymir work/ui/kygnbuton/offical_button.tga",
					"over_image" : "d:/ymir work/ui/kygnbuton/offical_button_bastim.tga",
					"down_image" : "d:/ymir work/ui/kygnbuton/offical_button.tga",
				},

			),
		},
	),
}

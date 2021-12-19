# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
-Extract Extern.rar in ".\Srcs\"
-Open ".\Srcs\Extern\cryptopp\cryptlib.sln" and compile it
-Open ".\Srcs\Client\Metin2Client.sln" and compile it

@\Srcs\Extern\cryptopp is compiler-version based and should recompile with MT target option
>maybe without /GL and /LTCG should be fine too

* Configuration
@#PYTHON2 2.7
>in ".\Srcs\Extern\Python2"

@#GRANNY2 amongst 24/27/28/29 (granny2.4 by default)
>easy switch in ".\Srcs\Extern\include\granny.h" amongst granny2.4, 2.7, 2.8, 2.9, 2.11

@#GENERAL MACROS
#define __OBSOLETE__					//useless and pointless code removed
#define __UNIMPLEMENTED__				//drafts of new things to be implemented

@\Srcs\Client\UserInterface\Locale_inc.h for ymir system implementations
>>default
#define LOCALE_SERVICE_EUROPE			//locale you want for locale.cpp
#define ENABLE_COSTUME_SYSTEM			//costume system	[@warme666]
#define ENABLE_ENERGY_SYSTEM			//energy system	[@warme666]
#define ENABLE_DRAGON_SOUL_SYSTEM		//dss system	[@warme666]
#define ENABLE_NEW_EQUIPMENT_SYSTEM		//belt system	[@warme666]
>>new macros
#define ENABLE_PACK_GET_CHECK			//enable py|pyc|txt check on pack.Get
#define ENABLE_CANSEEHIDDENTHING_FOR_GM	//enable gm to see invisible characters (both normal semi-transparent and gm invisibility)
#define ENABLE_PROTOSTRUCT_AUTODETECT	// if enabled, all the item_proto/mob_proto official structures (2007~2016) are automatically detected and supported without recompiling
>
#define ENABLE_PLAYER_PER_ACCOUNT5		//enable 5 characters per account	[@warme666]
#define ENABLE_LEVEL_IN_TRADE			//for localeInfo.EXCHANGE_TITLE with level
#define ENABLE_TEXT_LEVEL_REFRESH		//enable text tail level refresh when levelup
#define ENABLE_DICE_SYSTEM				//enable dice system: if the mob is king or boss and you're in party, the dropped item is randomly rolled	[@warme666]
#define ENABLE_EXTEND_INVEN_SYSTEM		//enable 4 inventory pages	[@warme666]
#define ENABLE_LVL115_ARMOR_EFFECT		//enable sparkle effect for 115 armors
#define ENABLE_USE_COSTUME_ATTR			//enable the items reset costume and enchant costume
#define ENABLE_SLOT_WINDOW_EX			//it will fix the refresh of the activated and cooltimed slots in the skill page (V) (except when switching to the equitation tab and vice versa)
#define WJ_SHOW_MOB_INFO				//enable mob info update for showing the mob lvl and the asterisk in name if aggro (ENABLE_SHOW_MOBAIFLAG and ENABLE_SHOW_MOBLEVEL)
>from gamelib
#define ENABLE_WOLFMAN_CHARACTER		//enable wolfman features	[@warme666]
>from eterlib
#define ENABLE_SEQUENCE_SYSTEM			// enable sequence system	[@warme666]

#define ENABLE_MAGIC_REDUCTION_SYSTEM	// enable resist magic reduction bonus	[@warme666]
#define ENABLE_MOUNT_COSTUME_SYSTEM		// enable mount costume slot	[@warme666]
#define ENABLE_WEAPON_COSTUME_SYSTEM	// enable weapon costume system	[@warme666]

@\Srcs\Client\GameLib\ActorInstanceAttach.cpp
#define AUTODETECT_LYCAN_RODNPICK_BONE	// adjust fishrod/pickaxe attached bone for lycan to equip_right instead of equip_right_weapon

@\Srcs\Client\GameLib\ActorInstanceCollisionDetection.cpp
#define ENABLE_PETS_WITHOUT_COLLISIONS		// disable collisions for pets
#define ENABLE_SHOPS_WITHOUT_COLLISIONS		// disable collisions for shops
#define ENABLE_MOUNTS_WITHOUT_COLLISIONS	// disable collisions for mounts

@\Srcs\Client\EterLib\error.cpp
#define ENABLE_CRASH_MINIDUMP			// it will generate a debuggable client\logs\metin2client_{version}_{date}.dmp file instead of "??????"

@\Srcs\Client\EterPack\EterPack.cpp
#define ENABLE_CRC32_CHECK				//mine: enable/disable crc32 check for type2

@\Srcs\Client\UserInterface\PythonMiniMap.cpp
#define ENABLE_NEW_ATLAS_MARK_INFO		//read the new locale/<lan>/map/<mapname>_point.txt structure (files used for offline minimap npc rendering)

@\Srcs\Client\UserInterface\PythonPlayer.cpp
#define ENABLE_NO_PICKUP_LIMIT		//if enabled, there will be no 0.5s of delay when picking up items with keyboard (\\z)

@\Srcs\Client\UserInterface\UserInterface.cpp
#define ENABLE_PYLIB_CHECK				//check python lib files to prevent exploit before load them
#define ENABLE_MILES_CHECK				//check miles files to prevent mss32.dll exploit before load them

@\Srcs\Client\UserInterface\InstanceBase.cpp
#define ENABLE_SIMPLE_REFINED_EFFECT_CHECK		// enable simple refine effect check (+7 blue, +8 green, +9 red) for any weapon/armor
#define USE_WEAPON_COSTUME_WITH_EFFECT			// enable refine effect for weapon costume
#define USE_BODY_COSTUME_WITH_EFFECT			// enable refine effect for body costume

@\Srcs\Client\UserInterface\PythonBackground.cpp
#define ENABLE_ATLASINFO_FROM_ROOT		//read atlasinfo.txt from root instead of locale

@\Srcs\Client\GameLib\GameLibDefines.h
>moved all to Locale_inc.h

@\Srcs\Client\GameLib\RaceDataFile.cpp
#define ENABLE_SKIN_EXTENDED			//extended source/targetskin[2-9] inside .msm

@\Srcs\Client\GameLib\ItemData.cpp
#define ENABLE_LOAD_ALTER_ITEMICON		//load a default item icon if the one inside the item_list.txt is missing

@\Srcs\Client\UserInterface\InstanceBase.cpp
#define ENABLE_NO_MOUNT_CHECK			//enable attack and skill from all horses/mounts

@\Srcs\Tools\DumpProto\dump_proto\dump_proto.cpp
#define ENABLE_ADDONTYPE_AUTODETECT				//it autodetects the addontype field from already known vnums (compatibility 100%)

* Dependencies
@\Srcs\Extern.rar
>it contains all is needed

* Database configuration
* How to run tests
* Deployment instructions
-Debug and Release are for UserInterface.sln
-MfcDebug and MfcRelease are for WorldEditor.sln

### Contribution guidelines ###

* Writing tests
* Code review
#@@Globally
@warme601: use release as advanced distribute with syserr.txt and so on
@warme666: those features requires the same feature server-sidely otherwise you'll get random issues. (packets not correctly handled)
@warme667: on ScriptLib/StdAfx.h; AT has been unset before loading python include
@warme668: trivial errors will be treated as mere warnings (sys_err -> sys_log) (TraceError -> Tracenf)

#@@Client

#@/UserInterface
@fixme001: on Packet.h; for do_view_equip (WEAR_MAX_NUM: server 32, client 11) now equal (32 both sides)
@fixme006: on PythonNetworkStreamModule.cpp, PythonNetworkStreamPhaseGame.cpp; "SEQUENCE mismatch 0xaf != 0x64 header 254" fix
			This happens due to a bug on the TODO_RECV_SYMBOL phase when calling the __SendSymbolCRCList.
			That function will connect via MarkServer_Login and iterate m_kVec_dwGuildID to send sub-"HEADER_CG_SYMBOL_CRC" packets.
			If m_kVec_dwGuildID is 0, the server will never receive packets after logged in the MarkServer, and the connection won't be closed.
			When a connection is established, a ping_event will be triggered every 60 seconds.
			When the time will come, a ping packet will be send to the client, and the client will reply back with a pong one.
			In this case, the secondary marklogin connection would be asynchronous, and the packet sequence for the pong mismatched too.
			After the sequence error occurs, the marklogin connection will be finally closed.

			In few words, everytime someone logs in the server (after character selection),
			the syserr will get once the mismatch error after 60 seconds.
			The fix is to not establish a marklogin connection for TODO_RECV_SYMBOL if the m_kVec_dwGuildID is 0.
@fixme007: on Packet.h, PythonNetworkStream.cpp, PythonNetworkStreamPhaseGame.cpp; added unknown header 213 (2 bytes)
@fixme009: on PythonPlayerModule.cpp; player.GetItemLink wasn't considering 6-7 bonuses enough
			they could have been seen as 1-5 bonuses if the item didn't have 1-5 bonuses
@fixme010: on PythonCharacterManager.cpp; ymir forgot .m_dwVID in the format argument (c_rkCreateData -> c_rkCreateData.m_dwVID)
@fixme013: on PythonPlayerModule.cpp; player.IsValuableItem was selecting a wrong item.cell
@fixme014: on PythonPlayerInput.cpp; if you (mouse) click a monster without having arrows, the automatic attack will go in loop (clicking on ground again will fix, but moving with WASD will be bad)
@fixme016: on PythonShop.cpp; ShopEx data weren't cleared if normal shops were open
@fixme022: on PythonItem.cpp; GetCloseItem distance calculation failed during float conversion (faraway items got distance 2 making them unpickable)

#@/GameLib
@fixme015: on MapOutdoorLoad.cpp; regen.txt was loaded from launcher even though it's used only by the WorldEditor
@fixme021: on RaceManager.cpp; new npclist.txt autodetects season shape.msm automatically

#@/EterLib
@fixme002: on GrpImageTexture.cpp, GrpImage.cpp; to show the name of the failed mapped .dds load
@fixme005: on SkyBox.cpp; the bottom pic was not shown
@fixme008: on IME.cpp; Ctrl+V crash when pasting images&co (no checks whether the handle was NULL or not)
@fixme011: on IME.cpp; non-printing/control characters were printed in the (chat) input (the ones you get when you press Ctrl+<key> in game)
@fixme012: on TextTag.cpp; on arabic locales, the [HyperText code] (alias Prism code) could be edited pressing <Backspace>

#@/MilesLib
@warme001: AIL_startup responsible to load *.asi *.flt *.m3d *.mix
@warme002: comments to be cleaned if necessary

#@/PRTerrainLib
@fixme003: on TextureSet.cpp; a new texture was added where the last was put
@fixme004: on TextureSet.cpp; a new textureset index was -1 instead of 0

#@/ScriptLib
@fixme020: on Resource.cpp; .png textures weren't listed


#@@Tools
#@/DumpProto
@fixme201: on ItemCSVReader.cpp; race splitted with | instead of ,

#@/Metin2PackMaker
@fixme301: on Main.cpp; The path ignored is always "d:/ymir work/sound/" instead of the chosen one
@fixme302: on Main.cpp; The directory ignored is always "CVS" instead of the chosen one


* Other guidelines
@\Srcs\Client\EterBase\Filename.h pseudo-fix to "successfully" compile
>needs rewriting (or simply fixing)

@\Srcs\Client\ScriptLib\PythonUtils.cpp with pseudo-long fix
#define PyLong_AsLong PyLong_AsLongLong
#define PyLong_AsUnsignedLong PyLong_AsUnsignedLongLong
>just this so it'll be 8 bytes instead of 4 for tuples
>an another way is just to change every color function with Py_xUnsigned instead of its Signed


### Who do I talk to? ###

* Repo owner or admin
martysama0134

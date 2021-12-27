#ifndef __INC_METIN2_COMMON_DEFINES_H__
#define __INC_METIN2_COMMON_DEFINES_H__
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////// ### Générales ### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define ENABLE_D_NJGUILD												// GameForce Lonca Eklentisi
#define ENABLE_FULL_NOTICE												// Full Notice Sistemi
#define ENABLE_NEWSTUFF													// Yeni Komut Eklentisi
#define ENABLE_PORT_SECURITY											// Port Güvenlik Eklentisi
#define ENABLE_BELT_INVENTORY_EX										// Kemer Envanteri
#define ENABLE_CMD_WARP_IN_DUNGEON										// Zindan Giriþ Komutu Eklentisi
#define ENABLE_COLLECT_QUEST_SYSTEM										// Uzaktan Biyalog Sistemi
#define ENABLE_SPECIAL_STORAGE											// Özel K Envanteri
#define WJ_ELDER_ATTRIBUTE_SYSTEM										// Kadim Efsun Küresi
#define ENABLE_UZAKMARKET_SYSTEM										// Uzaktan Market Sistemi
#define ENABLE_EXTRA_SLOT_SYSTEM										// Shop NPC ExtraSayfa
#define ENABLE_BASLANGIC_SYSTEM											// Baþlangýç özel efsunlar
#define ENABLE_TARGET_INFORMATION_SYSTEM								// Mop Drop Ýnfo Sistemi
#define ENABLE_QUICK_CHANNEL_SYSTEM										// Channel Switch System
#define ENABLE_BOSS_MANAGER_SYSTEM										// Boss tracking system
#define WJ_TARGET_HP_SYSTEM												// Hedef Oyuncu HP Göster
#define ENABLE_SHOW_CHEST_DROP											// Sandýk Ýç Görü Sistemi
#define ENABLE_PM_ALL_SEND_SYSTEM										// Toplu Pm Yollama Sistemi
#define ENABLE_EXTENDING_COSTUME_TIME									// Kostüm Süre Uzatma
#define ENABLE_ITEM_YOKET_SYSTEM										// Ýtem YokET Sistemi
#define ENABLE_RING_OF_SECRETS											// EXP Block System
#define KYGN_ITEM_REMOVE												// Toplu Ýtem Silme Eklentisi
#define ENABLE_UNLIMITED_SYSTEM											// Sýnýrsýz ok sistemi
#define ENABLE_SORT_INVEN												// Envanter Düzenle
#define OPEN_COMMAND_OFFLINESHOP										// Oyun Ýçi Pazar Aç Komutu "azar_ac"
#define ENABLE_ADDSTONE_FAILURE											// Taþ Basma Oraný
#define ENABLE_REMOTE_SHOP_SYSTEM									// Uzaktan NPC
#define LUCK_BOX									//sans kutusu
#define NEW_PVM_APPLYS													// yeni efsun

#define ICE_FIRE_RING
#define ENABLE_SWITCHBOT //switchbot
#define BLACKMARKET
#define PRICE_TYPE
#define SHOP_STOK
#define RELOAD_SHOP
#define ENABLE_RONARK_SYSTEM
#define ENABLE_AUTO_EVENT_SYSTEM
#define ENABLE_GUILD_LEADER
#define ENABLE_BOSS_HASAR_SIRALAMA
#define SEBNEM_EFEKT
#define NEW_SALES_SYSTEM


#define __ENABLE_NEW_OFFLINESHOP__
#ifdef __ENABLE_NEW_OFFLINESHOP__
	#define ENABLE_NEW_SHOP_IN_CITIES
	#define __ENABLE_LARGE_DYNAMIC_PACKET__
	#define ENABLE_OFFLINESHOP_DEBUG
	#define ENABLE_CHEQUE_SYSTEM
	#ifdef ENABLE_OFFLINESHOP_DEBUG
		#ifdef __WIN32__
			#define OFFSHOP_DEBUG(fmt , ...) sys_log(0,"%s:%d >> " fmt , __FUNCTION__ , __LINE__, __VA_ARGS__)
		#else
			#define OFFSHOP_DEBUG(fmt , args...) sys_log(0,"%s:%d >> " fmt , __FUNCTION__ , __LINE__, ##args)
		#endif
	#else
		#define OFFSHOP_DEBUG(...)   
	#endif
#endif


#define ENABLE_BLEND_AFFECT


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////// ### Deaktif System ### ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// #define ENABLE_OFFLINESHOP_MESSAGE_SYSTEM								// Offline Shop Mesaj Gonderme Sistemi
// #define ENABLE_ITEM_ATTR_COSTUME											// Kostüm Efsun Sistemi
// #define ENABLE_QUEST_CATEGORY											// Quest Kategori Sistemi
// #define FULL_YANG														// Enable support for yang type long long
// #define SHOP_DISTANCE													// Show shops in pos distance like WoM2
// #define SHOP_ONLY_ALLOWED_INDEX											// Enable limiting for other map index which is not defined in player.shop_limit
// #define SHOP_HIDE_NAME													// Enable hidding shop npc names like "Player's shop"
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////// ### Systèmes ### ////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#define ENABLE_ACCE_SYSTEM												// Acce Kuþak Sistemi
#define ENABLE_HIGHLIGHT_NEW_ITEM										// Yeni Ýtem Efekti Eklentisi
#define ENABLE_PLAYER_PER_ACCOUNT5										// 5 Karakter Eklentisi
#define ENABLE_DICE_SYSTEM												// Zar Sistemi
#define ENABLE_EXTEND_INVEN_SYSTEM										// 4 Envanter Sistemi
#define ENABLE_MOUNT_COSTUME_SYSTEM										// Binek Kostüm Sistemi
#define ENABLE_WEAPON_COSTUME_SYSTEM									// Silah Kostüm Sistemi
#define SHOP_SEARCH														// Ýtem Arama Sistemi
#define SHOP_SEARCH_PRICE_MIN											// Price in gui is a minimum eq. price >= item_price if is commented price in gui is a maximum
#define ENABLE_CHANNEL_SWITCH_SYSTEM									// Kanal Degistirme Modulu

/////////////////////////////////////////////////
// ### Offline Shop ### //
/////////////////////////////////////////////////
#define OFFLINE_SHOP								// Offline shops system
#define GIFT_SYSTEM									// gift system enable
#define SHOP_TIME_REFRESH 1*60						// time for cycle checking older shops
#define SHOP_BLOCK_GAME99							// Blocking create shops on channel 99
#define SHOP_AUTO_CLOSE								// Enable auto closing shop after sell last item
#define SHOP_GM_PRIVILEGES GM_IMPLEMENTOR			// Minimum GM privileges to using Shop GM Panel
/////////////////////////////////////////////////
// ### Won Sistemi ### //
/////////////////////////////////////////////////
#define ENABLE_CHEQUE_SYSTEM
#if defined(OFFLINE_SHOP) && defined(ENABLE_CHEQUE_SYSTEM)
#define ENABLE_OFFLINE_SHOP_USE_CHEQUE
#else
#define ENABLE_SHOP_USE_CHEQUE
#endif
/////////////////////////////////////////////////
// ### Wolfman ### //
/////////////////////////////////////////////////
#define ENABLE_WOLFMAN_CHARACTER					// Lycan Eklentisi Baþlangýç
#ifdef ENABLE_WOLFMAN_CHARACTER						// Lycan Karakteri
#define USE_MOB_BLEEDING_AS_POISON					// Lycan Mob Bleeding Eklentisi
#define USE_MOB_CLAW_AS_DAGGER						// Lycan Mob Claw Eklentisi
// #define USE_ITEM_BLEEDING_AS_POISON				// Lycan Ýtem Use Bleeding Eklentisi
// #define USE_ITEM_CLAW_AS_DAGGER					// Lycan Ýtem Use Claw Eklentisi
#define USE_WOLFMAN_STONES							// Lycan Taþ Eklentisi
#define USE_WOLFMAN_BOOKS							// Lycan Beceri Kitap Eklentisi
#endif												// Lycan Eklentisi Bitiþ
/////////////////////////////////////////////////
// ### Fix ### //
/////////////////////////////////////////////////
#define ENABLE_CHECK_GHOSTMODE_HACK					// Görünmezlik Hatasý Fix
#define ENABLE_QUEST_WINDOW_DAMAGE_SYSTEM			// Quest Penceresi Açýkken Damage Engeli
#define ENABLE_BOOKS_STACKFIX						// Beceri Kitap Hata Fix
#define ENABLE_FIX_READ_ETC_DROP_ITEM_FILE_BY_VNUM  // Etc Ýtem Drop Fix
#define __ENABLE_KILL_EVENT_FIX__					// if you want to fix the 0 exp problem about the when kill lua event (recommended)
#define DISABLE_STOP_RIDING_WHEN_DIE				// Oyuncu Öldükten Sonra At Ölmez veya Gitmez
/////////////////////////////////////////////////
// ### Disabled System ### //
/////////////////////////////////////////////////
// #define ENABLE_SEQUENCE_SYSTEM					// Sequence Sistemi
// #define ENABLE_GLOBAL_GIFT						// GM Hediye Sistemi
#define ENABLE_MAGIC_REDUCTION_SYSTEM				// Magic Reduction Sistemi Baþlangýç
#ifdef ENABLE_MAGIC_REDUCTION_SYSTEM				// Magic Reduction Sistemi
// #define USE_MAGIC_REDUCTION_STONES				// Magic Reduction Taþ Eklentisi
#endif												// Magic Reduction Sistemi Bitiþ
/////////////////////////////////////////////////
// #define URIEL_ANTI_CHEAT
/////////////////////////////////////////////////

enum eCommonDefines {
	MAP_ALLOW_LIMIT = 32, // 32 default
};

#endif


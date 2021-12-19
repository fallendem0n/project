@/Server/common/service.h
>
#define ENABLE_D_NJGUILD			//	d.new_jump_all fonksiyonunun aktif eder. Basit şekilde lonca ile birlikte zindan yapılmasını sağlar.
#define ENABLE_QUEST_CATEGORY		//	Quest kategori sistemini aktif eder.
#define ENABLE_NEWSTUFF				//	Yeni quest fonksiyonları, config ayarları vs.
#define ENABLE_FULL_NOTICE			//	Oyuncunun kafasının üzerinde büyük yazı ile duyuru geçme sistemi.
#define ENABLE_PORT_SECURITY		//	db_port, p2p_port ve uzaktan admin paneli(socket) üzerinden yapılan exploitleri engeller.
#define ENABLE_BELT_INVENTORY_EX	//	Kemer eşyalarını kemer envanterine atar ve bilinmeyen kemer pozisyonlarının oluşmasını engeller.
#define ENABLE_CMD_WARP_IN_DUNGEON	//	/warp oyuncu komutu oyuncu zindanda bile olsa çalışacaktır.
#define ENABLE_USE_COSTUME_ATTR		//	Kostüm efsunlamayı aktif eder.
#define ENABLE_ITEM_ATTR_COSTUME	//	Saç kostümü, zırh kostümü ve silah kostümü için item_attr ve item_attr_rare tablosunu aktif eder.
>lycan
#define ENABLE_WOLFMAN_CHARACTER	// Lycan karakterini ve fonksiyonlarını aktif eder.
#define MAP_ALLOW_LIMIT <int>		// Bir core'da maksimum kaç kanal olacabileceğini belirler.(Standart:32)
#define USE_MOB_BLEEDING_AS_POISON	// Aktif edildiğinde mob_proto'daki bleeding alanı çalışmayacaktır. Bu oran poison'dan alınacaktır.
#define USE_MOB_CLAW_AS_DAGGER		// Aktif edildiğinde mob_proto'daki claw alanı çalışmayacaktır. Bu oran dagger'dan alınacaktır.
#define USE_ITEM_BLEEDING_AS_POISON	// Aktif edildiğinde zehir etkisi azaltma, kanamayı da azaltacaktır.
#define USE_ITEM_CLAW_AS_DAGGER		// Aktif edildiğinde bıçaklara karşı savunma, pençeye karşı da işleyecektir.
#define USE_WOLFMAN_STONES			// Aktif edildiğinde metinlerden lycan taşları düşecektir.
#define USE_WOLFMAN_BOOKS			// Aktif edildiğinde lycan kitapları düşecektir.
>systems
#define ENABLE_PLAYER_PER_ACCOUNT5	// Aktif edildiğinde her hesapta 4 karakter yerine 5 karakter bulunabilecek.
#define ENABLE_DICE_SYSTEM			// Zar sistemi, boss kesildiğinde eşyalar partidekilere rastgele dağıtılacaktır.
#define ENABLE_EXTEND_INVEN_SYSTEM	// Envanterin 4 sayfasını aktif eder.
#define ENABLE_MOUNT_COSTUME_SYSTEM		// Binek slotun aktif eder.
#define ENABLE_WEAPON_COSTUME_SYSTEM	// Silah kostümü slotunu aktif eder.
>magic reduction stone
#define ENABLE_MAGIC_REDUCTION_SYSTEM	// Büyü bozma taşlarını aktif eder.
#define USE_MAGIC_REDUCTION_STONES	//	Büyü bozma taşları metinlerden düşer.

@/Src/Server/db/src/ClientManager.h
#define ENABLE_PROTO_FROM_DB		//	db klasöründeki "PROTO_FROM_DB = 1" yaparsanız protoları veritabanından okur. "MIRROR2DB = 1" yaparsanız txt'yi aynı zamanda veritabanına yansıtır.

@/Src/Server/db/src/ClientManager.cpp
#define ENABLE_DEFAULT_PRIV			//	Veritabanındaki common.priv_settings tablosundan drop ayarı yapmanıza olanak sağlar.
#define ENABLE_ITEMAWARD_REFRESH	//	item_award tablosu için her 5 saniyede bir yenileme querysi oluşturur.

@/Src/Server/db/src/ClientManagerBoot.cpp
#define ENABLE_AUTODETECT_VNUMRANGE	//	Protolar db'den yüklendiğinde simya eşyalarının vnum aralığını otomatik algılar.

@/Srcs/Server/game/src/stdafx.h
#define ENABLE_LIMIT_TIME			//	Oyunu süreli yapma sistemini aktif eder.(Bu süre bittiğinde oyun açılmaz. Süreli lisanslar için kullanabilirsiniz.)

@/Srcs/Server/game/src/guild.h
#define ENABLE_NEWGUILDMAKE			//	pc.make_guild0'ı aktif eder ve CInputMain::AnswerMakeGuild fonksiyonunu devre dışı bırakır.

@/Srcs/Server/game/src/horse_rider.h
#define ENABLE_INFINITE_HORSE_HEALTH_STAMINA	// At hiçbir zaman ölmez ve staminası her zaman full olur.

@/Srcs/Server/game/src/quest.h
#define ENABLE_QUEST_DIE_EVENT		// Questler için die trigger ekler.

@/Srcs/Server/game/src/config.cpp
#define ENABLE_CMD_PLAYER			// CMD içerisinden player komutunu aktif eder.(CMD dosyasından 'item player' gibi tanımlama yapabilirsiniz.)
#define ENABLE_EXPTABLE_FROMDB		// Exp tablosunu veritabanından okur.(common.exp_table)
#define ENABLE_AUTODETECT_INTERNAL_IP	// Açık ip adresi yoksa yerel ip adresini otomatik algılar.
#define ENABLE_GENERAL_CMD			// Aktif edildiğinde cmd'yi "locale/%s/conf/GENERAL_CMD", "locale/%s/conf/GENERAL_CMD_CHANNEL_%d", veya "locale/%s/conf/GENERAL_CMD_CHANNEL_%d_HOSTNAME_%s" dan okur.
#define ENABLE_GENERAL_CONFIG		// Aktif edildiğinde config'i "locale/%s/conf/GENERAL_CONFIG", "locale/%s/conf/GENERAL_CONFIG_CHANNEL_%d", veya "locale/%s/conf/GENERAL_CONFIG_CHANNEL_%d_HOSTNAME_%s" dan okur.
									// GENERAL_CONFIG'de tüm ayarlar geçerlidik ancak HOSTNAME, CHANNEL, PLAYER_SQL, COMMON_SQL, LOG_SQL, PORT, P2P_PORT, MAP_ALLOW, AUTH_SERVER, TEEN_ADDR, TEEN_PORT geçerli değildir.

@/Srcs/Server/game/src/char_resist.cpp
#define ENABLE_IMMUNE_PERC			// Bağışıklıkların %100 yerine %90 işlemesini sağlar. Bazı oyuncular bunu bug olarak nitelendirebilir :)

@/Srcs/Server/game/src/item.cpp
#define ENABLE_IMMUNE_FIX			// Bağışıklık bugunu giderir. Kalkan çıkarmanıza gerek kalmaz.

@/Srcs/Server/game/src/db.cpp
#define ENABLE_SPAMDB_REFRESH			//Her 10 dakikada bir common.spam_db'den spamdb yenilenmesini sağlar.

@/Srcs/Server/game/src/questlua.cpp
#define ENABLE_TRANSLATE_LUA			// translate.lua yüklenmesini aktif eder.
#define ENABLE_QUESTLIB_EXTRA_LUA		// questlib_extra.lua yüklenmesini aktif eder.

@/Srcs/Server/game/src/questlua_pc.cpp
#define ENABLE_LOCALECHECK_CHANGENAME	// Locale olarak eu seçildiğinde ad değiştirilemediğini kontrol etmeyi etkinleştirir.
#define ENABLE_PC_OPENSHOP				// pc.open_shop0(idshop) aktif eder ancak satma ve satın alma henüz çalışmıyor.

@/Srcs/Server/game/src/shop.cpp
#define ENABLE_SHOP_BLACKLIST		// Büyülü bakır ve Kutsama küresinin pazarda satılmasını engeller. 

@/Srcs/Server/game/src/cmd.cpp
#define ENABLE_BLOCK_CMD_SHORTCUT	// Aktif edildiğinde oyun içi komutlar kısaltılamaz. Örnek vermek gerekirse /i yazarak eşya çağıramazsınız. /item yazmalısınız.

@/Srcs/Server/game/src/cmd_gm.cpp
#define ENABLE_STATPLUS_NOLIMIT			// Statü limitini kaldırır. 90dan fazla statü verilebilir.
#define ENABLE_SET_STATE_WITH_TARGET	// Set_state komutu hedef ile birlikte kullanılabilir.
#define ENABLE_CMD_IPURGE_EX			// /ipurge komutuyla envanterin sadece belirli bölgelerini temizleyebilirsiniz. (inv/equip/ds/belt/all)

@/Srcs/Server/game/src/char_skill.cpp
#define ENABLE_FORCE2MASTERSKILL	// Skiller 17 olduğunda her zaman master olur.
#define ENABLE_MOUNTSKILL_CHECK		// Bineklerin skill kullanmasını kontrol eder. Kapatıldığında tüm binekler skill kullanabilir.
#define ENABLE_NULLIFYAFFECT_LIMIT	// Büyü çözme skilli kendisinden 9 levelden fazla fark olan oyunculara işlemez.(5 level karakterle 120 level karaktere büyü çözme atılmaz.)
#define ENABLE_MASTER_SKILLBOOK_NO_STEPS	// Aktif edildiğinde her kitap master seviyesini 1 arttıracaktır.(10 kitap Grand)

@/Srcs/Server/game/src/char_item.cpp
#define ENABLE_FIREWORK_STUN		//enable stun affect when using firework items
#define ENABLE_ADDSTONE_FAILURE		//enable add stone failure
#define ENABLE_EFFECT_EXTRAPOT		//enable extrapot effects when using green/purple potions
#define ENABLE_BOOKS_STACKFIX		//enable stackable books instead of remove all the pile

@/Srcs/Server/game/src/char_battle.cpp
#define ENABLE_NEWEXP_CALCULATION	//recalculate exp rate so you won't get random negative exp/marriage points
#define ENABLE_EFFECT_PENETRATE		//enable penetrate effect when performing a penetration

@/Srcs/Server/game/src/char.h
#define NEW_ICEDAMAGE_SYSTEM		// Nemere zindanı için yeni bir sistem.
#define ENABLE_ANTI_CMD_FLOOD		// Oyuncular her saniye 10 komut çağırabilir. Daha fazlasında oyundan atılır.
#define ENABLE_OPEN_SHOP_WITH_ARMOR	// Aktif edildiğinde zırh ile pazar açılabilir.

@/Srcs/Server/game/src/char.cpp
#define ENABLE_GOHOME_IF_MAP_NOT_ALLOWED	// Haritaya giriş kapalıysa karakter köye geri döner.

@/Srcs/Server/game/src/input_db.cpp
#define ENABLE_GOHOME_IF_MAP_NOT_EXIST			// Harita yoksa karakter köye geri döner.

@/Srcs/Server/game/src/mining.cpp
#define ENABLE_PICKAXE_RENEWAL		// Kazma geliştirilirken başarısız olduğunda 1.kademeye düşmek yerine ustalık puanlarının %10unu kaybeder. 

@/Srcs/Server/game/src/fishing.cpp
#define ENABLE_FISHINGROD_RENEWAL	// Olta geliştirilirken başarısız olduğunda 1.kademeye düşmek yerine ustalık puanlarının %10unu kaybeder. 

@/Srcs/Server/game/src/questmanager.cpp
#define ENABLE_PARTYKILL			// PartyKill'i tekrar aktif eder.

@/Srcs/Server/game/src/input_auth.cpp
#define ENABLE_ACCOUNT_W_SPECIALCHARS	// Hesap adı için özel karakterleri aktif eder.(Oyun içi isim değil.)

@/Srcs/Server/game/src/input_main.cpp
#define ENABLE_CHAT_SPAMLIMIT			// Oyuncular 5 saniyede 4 mesaj yazabilir. 10 defa tekrar edildiğinde oyundan atılır.
#define ENABLE_WHISPER_CHAT_SPAMLIMIT	// Mesaj limitini 5 saniyede 10 mesaj olarak sınırlar. Aşıldığında oyundan atılır.
#define ENABLE_CHAT_LOGGING				// Oyun içi sohbet logunu aktif eder.
#define ENABLE_CHECK_GHOSTMODE			// Karakter öldüğünde hareket etmesini engeller.
@/Srcs/Server/game/src/input_login.cpp
#define USE_LYCAN_CREATE_POSITION		// Aktif edildiğinde lycan kendi haritasında başlar.


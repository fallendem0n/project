@fingo01: Arkadaş listesinden bir oyuncuyu sildiğinizde diğer oyuncunun arkadaş listesinde bulunulması hatası giderildi.
@fingo02: At/binek binildiğinde ateş hayaleti kapanır.
@fingo03: Lens Gösterimi Fix
@fingo04: Otomatik ataktaki okçu ninja fix
@fingo05: Pazara vurulma hatası giderildi.
@fingo06: set align de derece hesaplaması hatası çözümlendi.
@fingo07: Karakter becerileri sıfırlandığında eski beceri grubuna ait güçlendirmelerin temizlenmemesi problemi giderildi.
@fingo08: Bineklerin geriye atması hatası giderili.
@fingo09: Bossların yere düşmesi hatası giderildi.
@fingo10: Büyülü Silah ve Hava Kılıcı skillerinin silahsız kullanılması engellendi.
@fingo11: Client taraflı bir memory leak giderildi. Burada bulunan continue ifadesi alt satırda bulunan obje temizlenme işlemini engellemekteydi.
@fingo13: Cube Result'ın taşması sorunu giderildi.
@fingo14: Blend fonksiyonunda üst üste binmesi durumunda elde edilen obje silinmediği için oluşan memory leak giderilmiştir.
@fingo15: Son seviyeye ulaşıldığında tecrübe elde edilemeyeceği için beceri kitabı okunulamaması hatası giderildi.
@fingo16: pc.select fonksiyonunda ch değeri tanımlandıktan sonra hiçbir kontrol olmadan kullanılıyordu. Bununla ilgili hata çözümü uygulandı.
@fingo17: Yeşil ve mor pot aktifken tekrar kullanılması engellendi.
@fingo18: Görünmez moddan çıktıktan sonra efektlerin gözükmemesi hatası giderildi.
@fingo19: Partideyken bayrak değiştirme hatası giderildi.
@fingo20: Sys_err daki type değerinin değişkenler arasında bulunmaması hatası giderildi.
@fingo21: pPc'nin olmaması durumunda oluşan çökme hatası giderildi.
@fingo22: İstiflenen taşlar kullanıldığında tamamının silinmesi hatası giderildi.
@fingo23: Karakter yaratılırken karakter adının uzunluğa ait sunucu taraflı bir kontrol bulunmadığı için istenilen uzunlukta karakter ismi yapılabiliyordu. Bu hata çözümlendi.
@fingo24: Cesaret pelerinin %50 şansla çalışması durumu kaldırıldı ve menzili 2 katına çıkartıldı.
@fingo25: CHARACTER_NAME_MAX_LEN 24->64 yapıldı. Mob_names'de 24den daha fazla karaktere sahip canavar ve npclerin isminin yarım gözükmesi için çözüm olacaktır.
@fingo26: Kostüm takılıyken cinsiyet değiştirme fix. --- fix kaldırıldı. alternatif çözüm uygulanacak.
@fingo27: GetQuestFlag fonksiyonunda pPc değerinin bulunmaması durumunda yaşanan çökme hatası giderildi.
@fingo28: Savaş ilanındaki savaş tipi değerin negatif olması nedeniyle oluşan çökme giderildi.
@fingo29: intrologin odak hatası giderilddi.
@fingo30: Skybox bulut kırpma hatası giderildid.
@fingo31: Depo'da oluşan memory leak hatası giderildi.
@fingo32: Ejderha Atışı işlememesi hatası çözümlendi.
@fingo33: Ejderha Kükremesi işlememesi hatası çözümlendi.
@fingo34: Canavar sayısı olarak oyuncu olmayanların değil canavar ve metin taşlarının sayısına göre hesaplanması çözümü uygulandı.
@fingo35: d.notice fonksiyonunda Desc olmayan oyunculara gönderilmesi hatası giderildi.
@fingo36: ITEM_NAME_MAX_LEN 24->64 yapıldı. Item_names'de 24den daha fazla karaktere sahip eşyaların isminin yarım gözükmesi için çözüm olacaktır.
@fingo37: Party fonksiyonlarının tamamında bulunan kontrol bulunmadan değişkenin kullanılması hatası giderildi.
@fingo38: pkOldGrid objesi kullanıldıktan sonra bellekten silinmiyordu. Bununla ilgili hata çözümü uygulandı.
@fingo39: Monarşi sistemindeki tablo ile QUERY'nin uyuşmaması sorunu giderildi.
@fingo40: 5300->30000 Default değer değiştirildi.
@fingo41: 600->3600 Default değer değiştirildi.
@fingo42: Level atlayınca pot verme kapatıldı.
@fingo43: Cesaret pelerini sınırsız yapıldı.
@fingo44: Pack yükleme sistemi baştan sona düzenlendi. Pack isimleri client üzerinden alınacaktır. Debug modda D:/Ymir Work klasörü yüklenecek ancak Release ve Distribute modda yüklenmeyecektir.(Debug modda pack kilitlemeden düzenleme yapılabilir. Debug olmayan modda ise loading ekranı daha kısa sürecektir.)
@fingo45: /costume ve /hair komutunda efsunun FN_Point_string de bulunmamasından dolayı oluşan çökme sorunu giderildi.
@fingo46: Karakter öldüğünde eğer çevrede zehir etkisinde olan bir canavar varsa karakterin kalkmasına izin vermemekte. Bunun için bir çözüm uygulandı.
@fingo47: ShopEx Memoryleak fix.
@fingo48: Maksimum level 250ye yükseltildi. config.cpp(gPlayerMaxLevel=250) yada kanal ayarlarından(max_level:250) düzenleyebilirsiniz.
@fingo49: utils.h üzerindeki str_to_number fonksiyonları düzenlendi. unsigned long long için gerekli fonksiyon eklendi.
@fingo50: Test server aktifken herkesin GM olması ve GM logosu gözükmesi sağlandı.
@fingo51: get_leader_vid çalıştığı sırada party yoksa core düşmesine sebep olan hata giderildi.
@fingo52: oyuncu isminde büyük-küçük harfler bulunmasından dolayı karakter üzerinde komutların çalışmaması sorunu giderildi.
@fingo53: İzleyici modundayken veya sersemleme etkisindeyken saldırı işlemesi engellendi.
@fingo54: RemoveGoodAffect'e ateş hayaleti eklendi. Skill sıfırlandığında ateş hayaleti silinecek.
@fingo55: Exp ve Gold için çarpan eklendi. Service.h dan düzenleyebilirsiniz.
@fingo56: pDungeon oluşmaması durumunda core düşmesine sebep olan hata giderildi.
@fingo57: Artık binekler, karaktere ata sahip olsa da olmasa da saldırı yapabilir.
@fingo58: 0 yang eşya alınmaması hatası fixlendi.
@fingo59: Cmd fonksiyonlarında kullanılan one_argument, two_argument'e ilave olarak 3,4,5,6 arguments alternatifleri eklendi. Şuanlık bir kullanım alanı yok ama ihtiyaç olacaktır.
@fingo60: Pet, binek, pazarlar düşman olarak gözükmeyecek.
@fingo61: Simyanın 30 leveldeki görevden önce açılabilmesi için pack ayarı değiştirildi.
@fingo62: Core düşmesi yaşanmaması için kontrol eklendi.
@fingo63: AutoGiveItem'da eşyaların kaybolmaması için koyulan engeldeki hesaplama hatası giderilerek eşya kaybolması sorununun önüne geçildi.
@fingo64: Kamera hareket ettirilince görünmezlerin görünür olması hata çözümü.
@fingo65: At üzerindeki şamanın saldırı işlememe hata çözümü.
@fingo66: Char.cpp ve Char_item.cpp de bulunan hatalı ';' lar düzeltildi.
@fingo67: Proto okunurken size değerinin 0 olması nedeniyle core vermesi sorunu giderildi.
@fingo68: Eşya bulunmaması durumunda oluşabilecek core düşmesi sorunu giderildi.
@fingo69: Bu fonksiyonun GM'leri kapsamaması gerekiyor.
@fingo70: Bu quest fonksiyonunda name veya arg değerlerinin bulunmaması durumunda oluşabilecek core düşmesi engellendi.
@fingo71: Bu quest fonksiyonunda ch değerinin bulunmaması durumunda oluşabilecek core düşmesi engellendi.
@fingo72: Simya 1 levelde görevsiz olarak aktif hale getirildi.
@fingo73: At üzerinde bulunanlara yapılan menzilli saldırılar için bir fix.
@fingo74: Lalaker memoryleak fix.
@fingo75: Duyguları kullanırken silah gizlenmesi.
@fingo77: Blend tablosu eklenen şebnemde uygulanan etkinin bulunmaması durumunda oluşan çökme sorunu giderildi.
@fingo78: Pazar açarken paketin silinmesi kaldırıldı.
@fingo79: Hata mesajı detaylandırıldı.
@fingo80: Kuşak eşyalarının aralığı 85000-86000 aralığı olarak sınırlandırıldı.
@fingo81: battle.cpp de hesaplama hatası nedeniyle oluşabilecek veri kaybı engellendi.
@fingo82: m_pkMobData bulunmaması durumunda kanal kapanmayacak.
@fingo83: "IsPolymorphed" sorgusu kaldırılarak dönüşüm hatası çözümlendi.
@fingo84: Zayıf internet bağlantısı olanlarda yada eski model bilgisayar kullananların binekteyken yaşanan lag nedeniyle oyundan atılması hatasının çözümü.
@fingo85: Güvenli alanda saldırı yapma, canavarın hedef alması ve üzerine gelmesi gibi sorunlar giderildi.
@fingo86: LovePoint aynı olduğu halde tekrar tekrar yenilenmesi hatası giderildi.
@fingo87: Query atılamaması durumunda oluşan sorgu çekirdek düşmesine sebebiyet verdiği için kontrol edildi.
@fingo88: Potansiyel yang bug fix.
@fingo89: NPC ye eşya satarken yanlış fiyat göstermesi fix.
@fingo90: ServerTimer iptal edilirken silinmemesi fix.
@fingo91: Serbest alan oyuncular ancak Barış modunda olmayanlara saldırabilirler.


@fingo001: Karakter ekranı otomatik yenilenmeme fixlendi.
@fingo002: Sürekli updatepacket göndermek yerine tek bir pakete bağlandı.
@fingo003: Oyunu kapatırken karakterlerle alakalı memoryleak var ise dump dosyası oluşturur.
@fingo004: Lonca mesajlarına süre limiti eklendi.
@fingo005: Uzaktan +basma engellendi.
@fingo006: Partiden çıktıktan sonra parti bufflarının silinmemesi engellendi ve fonksiyon düzenlendi.
@fingo007: +64000 üzeri eşya kodlarında paketi doğru iletmemeyle ilgili düzenleme.
@fingo008: Kemer yüzük ve kostümlere ekipman niteliği verildi.
@fingo009: Harita yüklemesi source kısmına taşındı.
@fingo010: shopSign düzenlendi.
@fingo011: Leveli anlık güncelleme eklendi.
@fingo012: Building syserri güncellendi.
@fingo013: Olası bir land core crash fixlendi.
@fingo014: char_manager SpawnMob syserri güncellendi.
@fingo015: char_state victim core crash fixlendi.
@fingo016: map_allow syserri güncellendi.
@fingo017: Ticarete quest üzerinde kullanılan aktif eşyaların eklenmesi engellendi.
@fingo018: auth coresinin fishing.txt okuması engellendi.
@fingo019: Lonca kurma querysi ile alakalı bir düzenleme yapıldı.
@fingo020: Attr tablosu boş iken oyunun rare efsunlardan crash yemesi önlendi.
@fingo021: Ox etkinliği açık değil iken ox etkinliğine girilmesi ile ilgili kontrol eklendi.
@fingo022: Regen yok ise regen event çalıştığında veren core crash fixlendi.
@fingo023: Oyuncu oyundan çıktığında lonca tablosunda otomatik güncellememesi fixlendi.
@fingo024: Bineklerin dönüş hızları ayarlandı.
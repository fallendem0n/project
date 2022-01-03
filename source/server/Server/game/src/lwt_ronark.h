#pragma once

/* Ronark */
class CRonarkSystem : public singleton<CRonarkSystem>
{
	private:
		BYTE ronark_acikmi, ronark_max_player = 30, ronark_min_level = 90, ronarkoldumu, loncaSayisi = 0;
		BYTE ronark_lonca_min_uye = 20, ronark_lonca_min_lv = 10, ronark_siklet = 0, izleyiciSayisi = 0;
		DWORD m_dwHakim;
		std::map<DWORD, float> ronark_data; // tut

	protected:
		LPEVENT ronark_hazirlik_event;

	public:
		CRonarkSystem();
		enum ERonarkBilgiler
		{
			RONARK_BOSS_VNUM = 6418, //Ronark Boss Kodu
			RONARK_MAP_VNUM	= 103, // Ronark Arena Index
			RONARK_ORTA_SIKLET_KATILIM = 30, // Orta siklet max katilim
			RONARK_BUYUK_SIKLET_KATILIM = 75, // Buyuk siklet max katilim
			RONARK_ORTA_SIKLET_UYE = 20, // Orta siklet min lonca uye sayisi
			RONARK_BUYUK_SIKLET_UYE = 70, // Buyuk sikler min lonca uye sayisi
			RONARK_BASLANGIC_ORTA_SAAT = 21, // Orta siklet giris acilis saati
			RONARK_BASLANGIC_BUYUK_SAAT = 22, // Buyuk sikler giris acilis saati
			RONARK_BITIS_SAAT = 23, // Tum verilerin silinip girislerin kapatilacagi saat
		};

		virtual		~CRonarkSystem();

		void		RonarkOlduAmk(LPCHARACTER pkVictim, LPCHARACTER pkKiller);
		void		LoncaHasarEkle(DWORD dwID, float Damage);
		void		IzleyiciyimKnkBen(LPCHARACTER izleyici);
		bool		RonarkaGirebilirMi(LPCHARACTER oyuncu);
		void		RonarkArenayaGit(LPCHARACTER oyuncu);
		void		GirenLonca(LPCHARACTER girenoyuncu);
		void		LoncaSayisiArttir();
		// void		FlagiSil();

		void		RonarkHazirlikBaslat(BYTE siklet);
		void		VerileriGonder(bool a = false);
		void		RonarkVerileriTemizle();
		void		RonarkHazirlikKapat();
		void		RonarkSpawnla();

/* Set - Get Fonksiyonlar */
		BYTE		GetRonarkStatus() { return ronark_acikmi;}
		void		SetRonarkStatus(BYTE gelen)	{ ronark_acikmi = gelen;}
		BYTE		GetDeadRonarkStatus()	{ return ronarkoldumu; }
		void		SetDeadRonarkStatus(BYTE gelen)	{ ronarkoldumu = gelen;}
		BYTE		GetRonarkMaxPlayer() { return ronark_max_player;}
		void		SetRonarkMaxPlayer(BYTE gelen)	{ ronark_max_player = gelen;}
		BYTE		GetRonarkMinLevel() { return ronark_min_level;}
		void		SetRonarkMinLevel(BYTE gelen)	{ ronark_min_level = gelen;}
		BYTE		GetRonarkMinLoncaLevel() { return ronark_lonca_min_lv;}
		void		SetRonarkMinLoncaLevel(BYTE gelen)	{ ronark_lonca_min_lv = gelen;}
		BYTE		GetRonarkMinLoncaUye() { return ronark_lonca_min_uye;}
		void		SetRonarkMinLoncaUye(BYTE gelen)	{ ronark_lonca_min_uye = gelen;}
		DWORD		GetRonarkHakimi() { return m_dwHakim; } // ronark hakim
		void		SetRonarkHakimi(DWORD dwID) { m_dwHakim = dwID; } // ronark hakim
		BYTE		GetRonarkSiklet() { return ronark_siklet;}
		void		SetRonarkSiklet(BYTE gelen) // 1 buyuk siklet 2 orta
					{ ronark_siklet = gelen; 
					SetRonarkMinLoncaUye(gelen == 1 ? RONARK_BUYUK_SIKLET_UYE :  RONARK_ORTA_SIKLET_UYE);
					SetRonarkMaxPlayer(gelen == 1 ? RONARK_BUYUK_SIKLET_KATILIM : RONARK_ORTA_SIKLET_KATILIM);
					} // siklet islem bitis
/* END */

/* Lonca Katilimci Islemleri */
		void		LoncaOnlineArttir(LPCHARACTER ch);
		void		LoncaOnlineSil(LPCHARACTER ch);
/* END */
};
/* Ronark */

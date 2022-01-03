/**************************
* Author: Larry Watterson *
***************************/
#include "stdafx.h"
#ifdef ENABLE_RONARK_SYSTEM
#include "char.h"
#include "guild.h"
#include "guild_manager.h"
#include "questmanager.h"
#include "char_manager.h"
#include "config.h"
#ifdef ENABLE_AUTO_NOTICE_SYSTEM
#include "auto_notice_manager.h"
#endif
#include "lwt_ronark.h"
#include "sectree_manager.h"

//#define OLDURENE_ODUL // eger ronarki olduren "kisi"'ye odul ve ismini map icinde duyurmak istiyorsaniz aktif edin
//#define LOG_TUT  // log tutmak isterseniz aktif edin (sadece test'de tavsiye edilir)
CRonarkSystem::CRonarkSystem() { RonarkVerileriTemizle(); } //constructor
CRonarkSystem::~CRonarkSystem(){ RonarkVerileriTemizle(); } //destructor


extern void RonarkSorguYolla(const char * c_pszBuf); // ronark sorgu ext

/* Event - Timer Islemleri */

const char* RONARK_TEXT_ARY(BYTE gelen) // duyuru yazilari locale_string
{
	typedef std::map<BYTE, const char *> TMapTranslate;
	TMapTranslate RONARK_TEXT_ARY;
	
	RONARK_TEXT_ARY[5] = LC_TEXT("ronark_duyuru1");
	RONARK_TEXT_ARY[4] = LC_TEXT("ronark_duyuru2");
	RONARK_TEXT_ARY[3] = LC_TEXT("ronark_duyuru3");
	RONARK_TEXT_ARY[2] = LC_TEXT("ronark_duyuru4");
	RONARK_TEXT_ARY[1] = LC_TEXT("ronark_duyuru5");
	RONARK_TEXT_ARY[0] = LC_TEXT("ronark_duyuru6");
	
	RONARK_TEXT_ARY[6] = LC_TEXT("ronark_kalan%d");
	RONARK_TEXT_ARY[7] = LC_TEXT("savas_sorumlusu");

	return RONARK_TEXT_ARY[gelen];
}

EVENTINFO(RonarkTimeInfo)
{
	int		left_second;

	RonarkTimeInfo() 
	:left_second(0)
	{
	}
};


EVENTFUNC(ronark_dirilme_timer)
{
	if (event == NULL)
		return 0;

	if (event->info == NULL)
		return 0;

	auto info = dynamic_cast<RonarkTimeInfo *>( event->info );
	
	if ( info == NULL )
	{
		sys_err( "<RonarkTimeInfo> <Factor> Null pointer" );
		return 0;
	}
#ifndef ENABLE_AUTO_NOTICE_SYSTEM
	char szNotice[512];
#endif
	if (info->left_second <= 0)
	{
		CRonarkSystem::instance().RonarkSpawnla(); // gonder gelsin
		CRonarkSystem::instance().RonarkHazirlikKapat(); // giris duyuru event kapat
#ifdef ENABLE_AUTO_NOTICE_SYSTEM
		CAutoNotice::instance().SendNoticeLine(2, RONARK_TEXT_ARY(0));
#else
		snprintf(szNotice, sizeof(szNotice), RONARK_TEXT_ARY(0));
		BroadcastNotice(szNotice);
#endif
		return 0;
	}
	else
	{
		BYTE gidecek = info->left_second % 60;
		if (gidecek == 0)
		{
			if (info->left_second > 300)
			{
#ifdef ENABLE_AUTO_NOTICE_SYSTEM
				CAutoNotice::instance().SendNoticeLine(2, RONARK_TEXT_ARY(6), (info->left_second / 60) - 5); // beyin bedava
				CAutoNotice::instance().SendNoticeLine(2, RONARK_TEXT_ARY(7));
#else
		snprintf(szNotice, sizeof(szNotice), RONARK_TEXT_ARY(6), (info->left_second / 60) - 5);
		BroadcastNotice(szNotice);
		snprintf(szNotice, sizeof(szNotice), RONARK_TEXT_ARY(7));
		BroadcastNotice(szNotice);
#endif
			}
			else{
				if (CRonarkSystem::instance().GetRonarkStatus() == 0)
				{
					CRonarkSystem::instance().SetRonarkStatus(1); // ronark_core icin girisler acildi
					RonarkSorguYolla("ronark_open"); // herkese yolla gitsin
				}
#ifdef ENABLE_AUTO_NOTICE_SYSTEM
				CAutoNotice::instance().SendNoticeLine(2, RONARK_TEXT_ARY(info->left_second / 60)); // evet, bedava
#else
				snprintf(szNotice, sizeof(szNotice), RONARK_TEXT_ARY(info->left_second / 60));
				BroadcastNotice(szNotice);
			}
#endif
		}
		--info->left_second;
	}

	return PASSES_PER_SEC(1);
}

void CRonarkSystem::RonarkHazirlikBaslat(BYTE siklet)
{
	if (ronark_hazirlik_event != NULL)
	{
		event_cancel(&ronark_hazirlik_event);
		ronark_hazirlik_event = NULL;
	}

	// SetRonarkSiklet(gelen); // acilan siklete gore sinirlar belirlendi

	auto* info = AllocEventInfo<RonarkTimeInfo>();
	info->left_second = 600; // 5dk duyuru - 5dk spawn oncesi total 10dk
	ronark_hazirlik_event = event_create(ronark_dirilme_timer, std::move(info), 1);
}

void CRonarkSystem::RonarkHazirlikKapat()
{
	if (ronark_hazirlik_event != NULL)
	{
		event_cancel(&ronark_hazirlik_event);
		ronark_hazirlik_event = NULL;
	}
}
void CRonarkSystem::RonarkSpawnla()
{
	CHARACTER_MANAGER::instance().SpawnMob(RONARK_BOSS_VNUM, RONARK_MAP_VNUM, 38400, 63900, 0, false, 360);
}

/* Event - Timer Islemleri */

void CRonarkSystem::RonarkVerileriTemizle() // ronark verileri temizlendi
{
	if (!ronark_data.empty())
	{
		for (const auto& it : ronark_data)
		{
			auto guild = CGuildManager::instance().FindGuild(it.first);
			if (guild)
			{
				guild->SetRonarkLoncaIcerdeMi(false);
				guild->SetRonarkOnline(0);
			}
		}
		ronark_data.clear(); // mapi temizle
	}
	loncaSayisi = 0;
	izleyiciSayisi = 0;
	sys_err("Ronark verileri temizlendi!");
	SetRonarkStatus(0); // girisleri kapat
	SECTREE_MANAGER::instance().PurgeMonstersInMap(RONARK_MAP_VNUM); // jotunu sil
}

// void CRonarkSystem::FlagiSil() // her acilista her ihtimale karsi kontrol flagini sifirlayalim
// {
	// quest::CQuestManager::instance().RequestSetEventFlag("ronark_aktif", 0);
// }

void CRonarkSystem::GirenLonca(LPCHARACTER girenoyuncu)
{
	if (!girenoyuncu)
		return;

	// if (ronark_acikmi == 0)
	// {
		// girenoyuncu->GoHome();
		// return;
	// }
	bool izleyiciMi = girenoyuncu->GetQuestFlag("ronark.izleyici_mi") > 0 ? true : false;
	if (!izleyiciMi)// cmd_generalden gelen bi' karar vardir
	{
		if (girenoyuncu->GetGuild() == NULL)
			return;

		const DWORD dwID = girenoyuncu->GetGuild()->GetID();
		LoncaOnlineArttir(girenoyuncu); // lonca online sayisi arttirildi

		girenoyuncu->SetPKMode(PK_MODE_GUILD); // pk mod degistirildi

		if (girenoyuncu->GetGuild()->GetRonarkLoncaIcerdeMi() == true) // icerdeyse gerisini yapma
			return;

		girenoyuncu->GetGuild()->SetRonarkLoncaIcerdeMi(true);

		const auto& RonarkGuild = CGuildManager::instance().FindGuild(dwID);

		ronark_data.emplace(dwID, 0);
		girenoyuncu->GetGuild()->SetRonarkOnline(1);
#ifdef ENABLE_AUTO_NOTICE_SYSTEM
		CAutoNotice::instance().SendNoticeLine(2,LC_TEXT("ronark_lonca_girdi%s"), RonarkGuild->GetName());
		CAutoNotice::instance().SendNoticeLine(2,LC_TEXT("ronark_toplam_lonca%d"), loncaSayisi+1);
#else
		char szNotice[512+1];
		snprintf(szNotice, sizeof(szNotice), "<Ronark Bolgesi> Ronark bolgesine %s katildi!", RonarkGuild->GetName());
		BroadcastNotice(szNotice);
		snprintf(szNotice, sizeof(szNotice), "Toplamda [%d] lonca var.", loncaSayisi+1);
		BroadcastNotice(szNotice);
#endif
		LoncaSayisiArttir(); // total lonca sayisi arttirildi
	}
	else{
		girenoyuncu->SetObserverMode(true); // izleyici modu aktif
		izleyiciSayisi++; // izleyici sayisini arttir
		girenoyuncu->SetQuestFlag("ronark.izleyici_mi", 0); // her ihtimale karsi
	}
}

void CRonarkSystem::RonarkOlduAmk(LPCHARACTER pkVictim, LPCHARACTER pkKiller)
{
	if (!pkVictim || !pkKiller || pkKiller->IsPC() == false || pkVictim->GetRaceNum() != RONARK_BOSS_VNUM || pkKiller->GetMapIndex() != RONARK_MAP_VNUM)
		return;

	if (ronark_acikmi == 0)
		return;

	SetDeadRonarkStatus(1); // jotun naneyi yidi
	SetRonarkStatus(1); // arenayi kapat

#ifdef OLDURENE_ODUL
	pkKiller->ZindanOdulGuiAc();

	char buf[512+1];
	snprintf(buf, sizeof(buf), "<Ronark> %s son vurusu yapti!", pkKiller->GetName());
	SendNotice(buf, true); 
#endif
	auto RonarkGuild = CGuildManager::instance().FindGuild(GetRonarkHakimi());
	const auto& it = ronark_data.find(RonarkGuild->GetID());
	if (it != ronark_data.end())
	{
		
		quest::CQuestManager::instance().RequestSetEventFlag("ronark_king", RonarkGuild->GetID()); // Ronark Hakimi tagi verildi 

	#ifdef ENABLE_AUTO_NOTICE_SYSTEM
		CAutoNotice::instance().SendNoticeLine(2,"Jotun Katledildi! En fazla vuran lonca : %s[%%%d]", RonarkGuild->GetName(), static_cast<BYTE>(it->second));
		// CAutoNotice::instance().SendNoticeLine(2,LC_TEXT("ronark_kapatiliyor"));
	#else
		char szNotice[512+1];
		snprintf(szNotice, sizeof(szNotice), "Jotun Katledildi! En fazla vuran lonca : %s[%%%d]", RonarkGuild->GetName(), static_cast<BYTE>(it->second));
		BroadcastNotice(szNotice);
		snprintf(szNotice, sizeof(szNotice), LC_TEXT("ronark_kapatiliyor"));
		BroadcastNotice(szNotice);
	#endif
	}
	else
	{
		sys_err("ERROR! CAN'T FIND GUILD ID WTF?");
	}
}

void CRonarkSystem::RonarkArenayaGit(LPCHARACTER oyuncu)
{
	if (!oyuncu || oyuncu->GetGuild() == NULL || ronark_acikmi == 0)
		return;

	// if (!RonarkaGirebilirMi(oyuncu))
		// return;

	if (-1 == oyuncu->GetEmptyInventory(3)) // envanter bos slot kontrolu, binek icin
	{
		oyuncu->ChatPacket(1, "Envanterinde 3 slot yer ayirmalisin.");
		return;
	}

	if (oyuncu->GetGuild()->GetRonarkOnline() >= ronark_max_player)
		return;

// binek varsa cikar ve affectlerini sil
	oyuncu->RemoveAffect(AFFECT_MOUNT);
	oyuncu->RemoveAffect(AFFECT_MOUNT_BONUS);
	auto binek = oyuncu->GetWear(WEAR_COSTUME_MOUNT);
	if (binek) 
		oyuncu->UnequipItem(binek);

	if (oyuncu->GetEmpire() == 1)
		oyuncu->WarpSet(46800, 46200);
	else if (oyuncu->GetEmpire() == 2)
		oyuncu->WarpSet(22100, 56000);
	else if (oyuncu->GetEmpire() == 3)
		oyuncu->WarpSet(44500, 83100);
	else
		return;
}

bool CRonarkSystem::RonarkaGirebilirMi(LPCHARACTER oyuncu)
{
	if (oyuncu->GetGuild()->GetMemberCount() < GetRonarkMinLoncaUye())
	{
		oyuncu->ChatPacket(1, LC_TEXT("ronarkloncauyeyetersizmin%d"), GetRonarkMinLoncaUye());
		return false;
	}
	if (oyuncu->GetGuild()->GetLevel() < GetRonarkMinLoncaLevel())
	{
		oyuncu->ChatPacket(1, LC_TEXT("ronarkloncalevelyetersizmin%d"), GetRonarkMinLoncaLevel());
		return false;
	}
	if (oyuncu->GetLevel() < ronark_min_level)
	{
		oyuncu->ChatPacket(1, LC_TEXT("ronarklevelyetersizmin%d"), ronark_min_level);
		return false;
	}
	return true;
}

void CRonarkSystem::IzleyiciyimKnkBen(LPCHARACTER izleyici)
{
	if (!izleyici || ronark_acikmi == 0)
		return;

	if (-1 == izleyici->GetEmptyInventory(3))
	{
		izleyici->ChatPacket(1, "Envanterinde 3 slot yer ayirmalisin.");
		return;
	}
	izleyici->SetQuestFlag("ronark.izleyici_mi", 1);
	izleyici->WarpSet(38400, 63700);
}

void CRonarkSystem::LoncaSayisiArttir()
{
	loncaSayisi += 1;
}

void CRonarkSystem::LoncaHasarEkle(DWORD dwID, float Damage)
{
	if (ronark_acikmi == 0 || Damage == 0)
		return;

	const auto& it = ronark_data.find(dwID);
	if (it == ronark_data.end())
		ronark_data.emplace(dwID, Damage); // yoksa listeye ekle
	else
		it->second += Damage;
	VerileriGonder();
}

void CRonarkSystem::LoncaOnlineArttir(LPCHARACTER ch)
{
	if (!ch || !ch->GetGuild() || ch->GetMapIndex() != CRonarkSystem::instance().RONARK_MAP_VNUM)
		return;
	
	ch->GetGuild()->SetRonarkOnline(ch->GetGuild()->GetRonarkOnline() + 1);
}

void CRonarkSystem::LoncaOnlineSil(LPCHARACTER ch)
{
	if (!ch  || ch->GetMapIndex() != RONARK_MAP_VNUM)
		return;

	if (!ch->IsObserverMode())
	{
		if (!ch->GetGuild())
			return;
		ch->GetGuild()->SetRonarkOnline(ch->GetGuild()->GetRonarkOnline() - 1);
	}
	else
	{
		--izleyiciSayisi; //bb
	}
}

namespace
{
	struct siralaAmk
	{
		template<typename T>
		bool operator()(const T &l, const T &r) const
		{
			// if (l.first != r.first)
				// return l.first > r.first;
			return l.first != r.first ? (l.second > r.second) : (l.first > r.first);
		}
	};

	struct FPacket
	{
		FPacket(const char* p) : m_pcData(p)
		{
		}

		void operator () (LPENTITY ent)
		{
			if (ent->IsType(ENTITY_CHARACTER))
			{
				const auto& ch = (LPCHARACTER)ent;

				if(!ch || !ch->GetGuild() || ch->IsPC() != true || ch->GetMapIndex() != CRonarkSystem::instance().RONARK_MAP_VNUM)
					return;

				ch->ChatPacket(CHAT_TYPE_COMMAND, m_pcData);
			}
		}
		const char* m_pcData;
	};


	void Packet(const char* veri)
	{
		const auto& pMap = SECTREE_MANAGER::instance().GetMap(CRonarkSystem::instance().RONARK_MAP_VNUM);
		if (pMap)
		{
			FPacket f(veri);
			pMap->for_each(f);
		}
		else
		{
			sys_err("cannot find map by index %d", CRonarkSystem::instance().RONARK_MAP_VNUM);
			return;
		}
	}
};

void CRonarkSystem::VerileriGonder(bool a) 
{
	char szVeri[52];
	std::set<std::pair<DWORD, float>, siralaAmk> sRN(ronark_data.cbegin(), ronark_data.cend());

	if (a)
	{
		SetRonarkHakimi(sRN.rbegin()->first);
		return;
	}

	BYTE i = 0;

	for (auto it = sRN.cbegin(); it != sRN.cend(); it++)
	{
#ifdef LOG_TUT
		sys_err("%d - %f" , it->first, it->second);
#endif
		if (i > 5)
			continue;
		const auto& LoncaID = CGuildManager::instance().FindGuild(it->first);
		const char * loncaadi = LoncaID->GetName();
		snprintf(szVeri, sizeof(szVeri),
		"RonarkInfo %d %d %s %f %d %d %d",
		i,
		it->first,
		loncaadi, 
		it->second,
		LoncaID->GetRonarkOnline(), 
		GetRonarkMaxPlayer(), 
		izleyiciSayisi);
		i++;
		Packet(szVeri);
	}
}
#endif //bb
/**************************
* Author: Larry Watterson *
* Date: 03.06.21 *
***************************/
#include "stdafx.h"
#ifdef ENABLE_BOSS_HASAR_SIRALAMA
#include "char.h"
#include "lwt_bosshasarsiralama.h"
#include "char_manager.h"
#include "questmanager.h"

#define LOG_TUT
/* -------------------------------------------------------- */
enum eBossInfos
{
	BOSS_VNUM = 0,
	POS_X = 1,
	POS_Y = 2,
	MAP_INDEX = 3,  
	RESPAWN_TIME_H = 4,
	RESPAWN_TIME_M = 5,
	SECURITY = 6,
	BOSS_INFO_MAX_NUM,	
};

DWORD _BossInfos[][BOSS_INFO_MAX_NUM] = 
{ /* BOSS VNUM - MAP_X - MAP_Y - MAP_INDEX - R_H - R_M */
	{2206, 6032, 6922, 62, 0, 30, false}, // alev kral
	{1901, 4333, 2165, 61, 1, 0, false}, // dokuz kuyruk
	{1304, 5750, 932, 65, 1, 0, false}, // sari kaplan hayaleti
	{1191, 1353, 13438, 72, 4, 0, false}, // buz cadisi
	{2492, 2749, 12593, 73, 0, 30, false}, // general 1
	{2494, 1914, 12281, 73, 0, 30, false}, // general 2
	{2495, 2245, 13171, 73, 0, 30, false}, // general 3
};

struct siralaAmk
{
	template <typename T>
	bool operator()(const T &l, const T &r) const
	{
		return l.second.iTotalDamage < r.second.iTotalDamage;
	}
};
/* -------------------------------------------------------- */

void CBossHasarSiralama::Initialize() //deactive
{
	for (DWORD i = 0; i < sizeof(_BossInfos)/sizeof(*_BossInfos); i++)
	{
		bossCont.emplace_back(M2_NEW BossHasarSiralamaInfo(_BossInfos[i][BOSS_VNUM]));
#ifdef LOG_TUT
		sys_err("CBossHasarSiralama Class olusturuldu '%d'", _BossInfos[i][BOSS_VNUM]);
#endif
	}
}

void CBossHasarSiralama::Packet(const char* veri)
{
	for (const auto& it : characterList)
		it->ChatPacket(CHAT_TYPE_COMMAND, veri);
}

void CBossHasarSiralama::ListeyeEkle(LPCHARACTER ch)
{
	if (ch)
		characterList.emplace_back(ch);
}

void CBossHasarSiralama::ListeyiTemizle()
{
	if (!characterList.empty())
		characterList.clear();
}

void CBossHasarSiralama::CheckBoss(int hour, int min, int sec)
{
	if (sec == 0)
	{
		for (DWORD i = 0; i < sizeof(_BossInfos)/sizeof(*_BossInfos); i++)
		{
			if (_BossInfos[i][RESPAWN_TIME_M] == 0 && hour % _BossInfos[i][RESPAWN_TIME_H] == 0 && min == 0)
			{
				CHARACTER_MANAGER::instance().SpawnMob(_BossInfos[i][BOSS_VNUM], _BossInfos[i][MAP_INDEX], _BossInfos[i][POS_X]*100, _BossInfos[i][POS_Y]*100, 0, false, 360);
			}
			if (_BossInfos[i][RESPAWN_TIME_H] == 0 && min % _BossInfos[i][RESPAWN_TIME_M] == 0)
			{
				CHARACTER_MANAGER::instance().SpawnMob(_BossInfos[i][BOSS_VNUM], _BossInfos[i][MAP_INDEX], _BossInfos[i][POS_X]*100, _BossInfos[i][POS_Y]*100, 0, false, 360);
			}
		}
	}
}

BossHasarSiralamaInfo*	CBossHasarSiralama::FindBossClass(DWORD dwID)
{
	for (const auto& it : bossCont) {
		if (it->GetBossVID() == dwID) {
			return it;
		}
	}
	return nullptr;
}

bool CBossHasarSiralama::BossVnum(DWORD mVnum) // vurulan boss'da gui acilsin mi
{
	for (DWORD i = 0; i < sizeof(_BossInfos)/sizeof(*_BossInfos); i++)
	{
		if (mVnum ==_BossInfos[i][BOSS_VNUM])
			return true;
	}
	return false;
}

BossHasarSiralamaInfo::BossHasarSiralamaInfo(DWORD dwID)
{
	SetBossVID(dwID);
}

void BossHasarSiralamaInfo::BasAmk(std::map<VID, CHARACTER::TBattleInfo>& rMP)
{
	std::set<std::pair<VID, CHARACTER::TBattleInfo>, siralaAmk>  sSET(rMP.begin(), rMP.end());
	BYTE list = 0;

	for (auto it = sSET.rbegin(); it != sSET.rend(); it++) // gonder baqm
	{
		if (list > 5) // five member in list
			continue;

		auto oyuncu = CHARACTER_MANAGER::instance().Find(it->first);
		if(!oyuncu)
		{
			continue;
		}

		float fDamage = MINMAX(0, (double)(it->second.iTotalDamage * 100) / (double)(GetBossHP()), 100);
		char szMP[128];
		snprintf(szMP, sizeof(szMP), "br_info %d %d %s %d %d %f %d",
		list,
		oyuncu->GetRaceNum(),
		oyuncu->GetName(),
		oyuncu->GetLevel(),
		oyuncu->GetEmpire(),
		fDamage,
		oyuncu->zehirledim == true ? 1 : 0);
		CBossHasarSiralama::instance().Packet(szMP);
		list++;
	}
}
#endif
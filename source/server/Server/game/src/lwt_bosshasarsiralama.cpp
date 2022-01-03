/**************************
* * Author: Larry Watterson *
* ! Date: 03.06.21 !
***************************/
#include "stdafx.h"
#ifdef ENABLE_BOSS_HASAR_SIRALAMA
#include "lwt_bosshasarsiralama.h"
#include "buffer_manager.h"
#include "char_manager.h"
#include "char.h"
#include "desc.h"

#ifdef ENABLE_KORUMALI_ALAN
	#define GUVENLI_ALAN_SURE 1
	#define SAATTEN_ONCEKI_DK  59
#endif

// #define LOG_TUT
/* -------------------------------------------------------- */
DWORD _BossInfos[][CBossHasarSiralama::BOSS_INFO_MAX_NUM] =
{ /* BOSS VNUM - MAP_X - MAP_Y - MAP_INDEX - R_H - R_M */
	{2206, 6032, 6922, 62, 0, 30, false, false}, // alev kral
	{1901, 4333, 2165, 61, 1, 0, false, false}, // dokuz kuyruk
	{1304, 5750, 932, 65, 1, 0, false, false}, // sari kaplan hayaleti
	{1191, 1353, 13438, 72, 4, 0, false, false}, // buz cadisi
	{2492, 2749, 12593, 73, 0, 30, false, false}, // general 1
	{2494, 1914, 12281, 73, 0, 30, false, false}, // general 2
	{2495, 2245, 13171, 73, 0, 30, false, false}, // general 3
};
struct vecAlgo
{
	LPCHARACTER ch;
	vecAlgo(LPCHARACTER ch) : ch(ch) {}
	template <typename T>
	bool operator()(const T& p) const
	{
		return p.first == ch;
	}
};
struct sortVec
{
	template <typename T>
	bool operator()(const T& p, const T& p2) const
	{
		return p.second.dwDamage > p2.second.dwDamage;
	}
};
/* -------------------------------------------------------- */

BossHasarSiralamaInfo::BossHasarSiralamaInfo(const DWORD dwID, const DWORD dwMaxHP)
{
	SetBossVID(dwID);
	SetBossHP(dwMaxHP);
}

BossHasarSiralamaInfo* CBossHasarSiralama::FindBossClass(const DWORD dwID) const
{
	for (const auto& it : bossCont) {
		if (it->GetBossVID() == dwID) {
			return it;
		}
	}
	return nullptr;
}

void CBossHasarSiralama::Initialize(const DWORD dwNumber, const DWORD dwMaxHP)
{
	bossCont.pusback(M2_NEW BossHasarSiralamaInfo(dwNumber, dwMaxHP));
#ifdef LOG_TUT
	sys_err("Create class (vnum : %d - maxHP : %d)", dwNumber, dwMaxHP);
#endif
}

void CBossHasarSiralama::VecActions(const LPCHARACTER ch, const DWORD damage)
{
	const auto& it = std::find_if(BossRankVec.begin(), BossRankVec.end(),vecAlgo(ch));
	if (it != BossRankVec.end())
	{
		it->second.dwDamage += damage;
	}
	else
	{
		damageInfo d{};
		d.bRace = static_cast<BYTE>(ch->GetRaceNum());
		d.cName = ch->GetName();
		d.bLevel = static_cast<BYTE>(ch->GetLevel());
		d.bEmpire = ch->GetEmpire();
		d.dwDamage = damage;
		BossRankVec.push_back(ch, d);
		SendClient(GC_BRINFO_ADD, nullptr, 0);
	}
}

void CBossHasarSiralama::SendClient(const BYTE bSubHeader, const void* c_pvData, const size_t iSize)
{
	TBossHasarAction packet{};
	packet.bHeader = HEADER_GC_BHASAR;
	packet.bSubHeader = bSubHeader;

	TEMP_BUFFER buf;
	buf.write(&packet, sizeof(packet));
	if (iSize)
		buf.write(c_pvData, iSize);
	for (const auto& it : BossRankVec)
		it.first->GetDesc()->Packet(buf.read_peek(), buf.size());
}

void CBossHasarSiralama::CheckBoss(const int hour, const int min, const int sec) const
{
	// if (sec == 0)
	// {
		for (BYTE i = 0; i < sizeof(_BossInfos) / sizeof(_BossInfos[0]); i++)
		{
			if (_BossInfos[i][IS_SPAWN] == true)
				continue;
			if (_BossInfos[i][RESPAWN_TIME_M] == 0 && hour % _BossInfos[i][RESPAWN_TIME_H] == 0 && min == 0)
			{
				CHARACTER_MANAGER::instance().SpawnMob(_BossInfos[i][BOSS_VNUM], _BossInfos[i][MAP_INDEX], _BossInfos[i][POS_X] * 100, _BossInfos[i][POS_Y] * 100, 0, false, 360);
				_BossInfos[i][IS_SPAWN] = true;
			}
			if (_BossInfos[i][RESPAWN_TIME_H] == 0 && min % _BossInfos[i][RESPAWN_TIME_M] == 0)
			{
				CHARACTER_MANAGER::instance().SpawnMob(_BossInfos[i][BOSS_VNUM], _BossInfos[i][MAP_INDEX], _BossInfos[i][POS_X] * 100, _BossInfos[i][POS_Y] * 100, 0, false, 360);
				_BossInfos[i][IS_SPAWN] = true;
			}
		}
	// }
}

bool CBossHasarSiralama::BossVnum(const DWORD mVnum) const
{
	for (BYTE i = 0; i < sizeof(_BossInfos) / sizeof(_BossInfos[0]); i++)
	{
		if (mVnum == _BossInfos[i][BOSS_VNUM])
			return true;
	}
	return false;
}

void CBossHasarSiralama::UpdateInfo(const DWORD bossHP)
{
	std::sort(BossRankVec.begin(), BossRankVec.end(), sortVec());
	int8_t list = 0;
	for (const auto& it: BossRankVec)
	{
		if (list > 9) { continue; }
		BYTE Damage = MINMAX(0, (it.second.dwDamage * 100) / (bossHP), static_cast<BYTE>(100));

		TBossHasarData pack{};
		pack.bHeader = HEADER_GC_BHASAR;
		pack.wRaceNum = it.second.bRace;
		pack.bRank = list++;
		std::strcpy(pack.cName, it.second.cName);
		pack.bLevel = it.second.bLevel;
		pack.bEmpire = it.second.bEmpire;
		pack.bDamage = Damage;
		SendClient(GC_BRINFO_UPDATE, &pack, sizeof(pack));
	}
}

void CBossHasarSiralama::BossAction(DWORD dwRaceNum)
{
	BYTE index;
	for (BYTE i = 0; i < sizeof(_BossInfos) / sizeof(_BossInfos[0]); i++)
	{
		if (dwRaceNum == _BossInfos[i][BOSS_VNUM])
		{
			_BossInfos[i][IS_SPAWN] = false;
			break;
		}
	}
}

void CBossHasarSiralama::Destroy()
{
	for (const auto& it : bossCont)
		delete it;
	bossCont.clear();
}

void CBossHasarSiralama::RemoveVec(LPCHARACTER ch)
{
	const auto& it = std::remove_if(BossRankVec.begin(), BossRankVec.end(), vecAlgo(ch));
	if (it != BossRankVec.end())
		BossRankVec.erase(it);
}

void CBossHasarSiralama::ClearVec()
{
	SendClient(GC_BRINFO_CLEAR, nullptr, 0);
	if (!BossRankVec.empty())
		BossRankVec.clear();
}
#endif
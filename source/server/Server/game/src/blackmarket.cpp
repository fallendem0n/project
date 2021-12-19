#include "stdafx.h"
#include "blackmarket.h"
#include "char.h"
#include "db.h"
#include "utils.h"
#include "config.h"
#include "desc_client.h"
#include "desc_manager.h"

extern int passes_per_sec;

CBlackMarket::CBlackMarket()
{
	Initialize();
}

CBlackMarket::~CBlackMarket()
{
	m_map_pkBlackMarket.clear();
}

CBlackMarket::SBlackMarket::SBlackMarket()
{
	dwVnum	= 0;
	llPrice	= 0;
	llWon	= 0;
}


bool CBlackMarket::GetPriceData(DWORD dwVnum, TBlackMarket ** pPriceData)
{
	TBlackMarketMap::iterator it = m_map_pkBlackMarket.find(dwVnum);
	if (m_map_pkBlackMarket.end() == it)
		return false;

	*pPriceData = &(it->second);
	return true;
}

void CBlackMarket::Initialize()
{
	m_map_pkBlackMarket.clear();

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(
			"select vnum, won, yang from player.blackmarket"));

	if (pMsg->Get()->uiNumRows == 0)
	{
		// sys_err("sql query null");
		return;
	}

	MYSQL_ROW row;
	DWORD dwItemVnum = 0;
	DWORD dwGold, dwWon = 0;

	while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
	{
		str_to_number(dwItemVnum, row[0]);
		str_to_number(dwWon, row[1]);
		str_to_number(dwGold, row[2]);

		m_map_pkBlackMarket.insert(std::make_pair(dwItemVnum, SBlackMarket()));

		TBlackMarket & rPriceData = m_map_pkBlackMarket[dwItemVnum];
		rPriceData.dwVnum = dwItemVnum;		
		rPriceData.llWon = (long long)dwWon;
		rPriceData.llPrice = (long long)dwGold;
	}
}

int* CBlackMarket::GetPriceInfo(LPCHARACTER ch, DWORD dwVnum, short sCount)
{
	
	int info[2];
	info[0] = -1;
	info[1] = -1;
	
	if (!ch || !ch->GetDesc())
	{
		return info;
	}
	
	SBlackMarket * c_pPriceData;
	if (!GetPriceData(dwVnum, &c_pPriceData))
	{
		return info;
	}
	int neededwon = c_pPriceData->llWon;
	int neededgold = c_pPriceData->llPrice;
	if (sCount != 1)
	{
		if (c_pPriceData->llWon == 0 && c_pPriceData->llPrice > 0)
		{
			unsigned long long llMoney;
			llMoney = c_pPriceData->llPrice * sCount;
			if (llMoney >= (long long)GOLD_MAX)
			{
				llMoney /= 100000000;
				neededwon = (int)llMoney;
				neededgold = 0;
			}
			else
			{
				neededwon = neededwon*sCount;
				neededgold = neededgold*sCount;
				
			}
		}
		else
		{
			neededwon = neededwon*sCount;
			neededgold = neededgold*sCount;
		}
	}
	sys_log(0,"Price 1 %d",neededwon);
	info[0] = neededwon;
	sys_log(0,"Price 2 %d",neededgold);
	info[1] = neededgold;
	sys_log(0,"Price 3 %d - %d",info[0], info[1]);
	return info;
}


int CBlackMarket::GetGoldPrice(LPCHARACTER ch, DWORD dwVnum)
{
	if (!ch || !ch->GetDesc())
	{
		return -1;
	}
	
	SBlackMarket * c_pPriceData;
	if (!GetPriceData(dwVnum, &c_pPriceData))
	{
		return -1;
	}
	bool bOverFlow = false;
	int gold = c_pPriceData->llPrice;
	return gold;
}

int CBlackMarket::GetWonPrice(LPCHARACTER ch, DWORD dwVnum)
{
	if (!ch || !ch->GetDesc())
	{
		return -1;
	}
	
	SBlackMarket * c_pPriceData;
	if (!GetPriceData(dwVnum, &c_pPriceData))
	{
		return -1;
	}
	bool bOverFlow = false;
	int won = c_pPriceData->llWon;
	return won;
}


void CBlackMarket::GetPriceList(LPCHARACTER ch)
{
	if (!ch || !ch->GetDesc())
	{
		return;
	}
	
	TBlackMarketMap::iterator it = m_map_pkBlackMarket.begin();
	SBlackMarket * c_pPriceData;
	
	ch->ChatPacket(CHAT_TYPE_COMMAND,"blackmarket_clear");

	while (it != m_map_pkBlackMarket.end())
	{
		c_pPriceData = &(it->second);
		ch->ChatPacket(CHAT_TYPE_COMMAND,"blackmarket_insert %d %d %d",c_pPriceData->dwVnum, (int)c_pPriceData->llWon, (int)c_pPriceData->llPrice);
		++it;
	}
	return;
}



bool CBlackMarket::GetPrice(LPCHARACTER ch, DWORD dwVnum, short sCount, int iCheque, int iGold)
{
	if (!ch || !ch->GetDesc())
	{
		return false;
	}

	SBlackMarket * c_pPriceData;
	if (!GetPriceData(dwVnum, &c_pPriceData))
	{
		return true;
	}
	bool bOverFlow = false;
	int neededwon = c_pPriceData->llWon;
	int neededgold = c_pPriceData->llPrice;
	if (sCount != 1)
	{
		if (c_pPriceData->llWon == 0 && c_pPriceData->llPrice > 0)
		{
			unsigned long long llMoney;
			llMoney = c_pPriceData->llPrice * sCount;
			if (llMoney >= (long long)GOLD_MAX)
			{
				llMoney /= 100000000;
				neededwon = (int)llMoney;
				neededgold = 0;
				bOverFlow = true;
			}
			else
			{
				iCheque /= sCount;
				iGold /= sCount;
			}
		}
		else
		{
			iCheque /= sCount;
			iGold /= sCount;
		}
	}
	if (neededwon > iCheque || neededgold > iGold)
	{

		ch->ChatPacket(CHAT_TYPE_INFO, "Minimum koyabilecegin tutar %d won %d yang.", (int)c_pPriceData->llWon, (int)c_pPriceData->llPrice);
		if (sCount > 1 && bOverFlow == false)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "Minimum koyman gereken tutar %d won %d yang.", (int)c_pPriceData->llWon * sCount, (int)c_pPriceData->llPrice * sCount);
		}
		else if (sCount > 1 && bOverFlow == true)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "Minimum koyman gereken tutar %d won %d yang.", neededwon, neededgold);
		}
		return false;
	}
	return true;
}

bool CBlackMarket::HaveLimit(LPCHARACTER ch, DWORD dwVnum)
{
	if (!ch || !ch->GetDesc())
	{
		return false;
	}

	SBlackMarket * c_pPriceData;
	if (!GetPriceData(dwVnum, &c_pPriceData))
	{
		return false;
	}
	return true;
}

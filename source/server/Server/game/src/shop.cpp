#include "stdafx.h"
#include "../../libgame/include/grid.h"
#include "constants.h"
#include "utils.h"
#include "config.h"
#include "shop.h"
#include "desc.h"
#include "desc_manager.h"
#include "char.h"
#include "char_manager.h"
#include "item.h"
#include "item_manager.h"
#include "buffer_manager.h"
#include "packet.h"
#include "log.h"
#include "db.h"
#include "p2p.h"
#include "questmanager.h"
#include "monarch.h"
#include "mob_manager.h"
#include "locale_service.h"
#include "../../common/CommonDefines.h"

//#define ENABLE_SHOP_BLACKLIST
/* ------------------------------------------------------------------------------------ */
CShop::CShop()
	: m_dwVnum(0), m_dwNPCVnum(0), m_pkPC(NULL)
{
#ifdef ENABLE_EXTRA_SLOT_SYSTEM
	m_pGrid = M2_NEW CGrid(8, 8);
#else
	m_pGrid = M2_NEW CGrid(5, 9);
#endif
#ifdef OFFLINE_SHOP
	SetLocked(false);
#endif
}

#ifdef SHOP_SEARCH
#ifdef SHOP_SEARCH_PRICE_MIN
inline bool SHOP_SEARCH_PRICE_VAILD(long long item_price,long long price) {return (item_price <= price || price == 0);}
#else
inline bool SHOP_SEARCH_PRICE_VAILD(long long item_price,long long price) {return (item_price >= price);}
#endif
bool CShop::SearchItem(DWORD vnum, long long price,DWORD book)
{
	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		const SHOP_ITEM & item = m_itemVector[i];
		if (!item.pkItem)
			continue;
		if(item.vnum != vnum)
			continue;
		switch(item.vnum)
		{
			case 50300://skill book
			case 70037://forget skill book
			case 70055://forget skill book
				if (SHOP_SEARCH_PRICE_VAILD(item.price,price) && item.pkItem->GetSocket(0) == book)
					return true;
				break;
			default:
				if (SHOP_SEARCH_PRICE_VAILD(item.price,price))
					return true;
				break;
		}

	}

	return false;
}
#endif

CShop::~CShop()
{
	TPacketGCShop pack;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_END;
	pack.size		= sizeof(TPacketGCShop);

	Broadcast(&pack, sizeof(pack));

	GuestMapType::iterator it;

	it = m_map_guest.begin();

	while (it != m_map_guest.end())
	{
		LPCHARACTER ch = it->first;
		ch->SetShop(NULL);
		++it;
	}

	M2_DELETE(m_pGrid);
}

void CShop::SetPCShop(LPCHARACTER ch)
{
	m_pkPC = ch;
}

bool CShop::Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pTable)
{
	/*
	   if (NULL == CMobManager::instance().Get(dwNPCVnum))
	   {
	   sys_err("No such a npc by vnum %d", dwNPCVnum);
	   return false;
	   }
	 */
	sys_log(0, "SHOP #%d (Shopkeeper %d)", dwVnum, dwNPCVnum);

	m_dwVnum = dwVnum;
	m_dwNPCVnum = dwNPCVnum;

	BYTE bItemCount;

	for (bItemCount = 0; bItemCount < SHOP_HOST_ITEM_MAX_NUM; ++bItemCount)
		if (0 == (pTable + bItemCount)->vnum)
			break;

	SetShopItems(pTable, bItemCount);
	return true;
}

void CShop::SetShopItems(TShopItemTable * pTable, BYTE bItemCount)
{
	if (bItemCount > SHOP_HOST_ITEM_MAX_NUM)
		return;

	m_pGrid->Clear();

	m_itemVector.resize(SHOP_HOST_ITEM_MAX_NUM);
	msl::refill(m_itemVector);

	for (int i = 0; i < bItemCount; ++i)
	{
		LPITEM pkItem = NULL;
		const TItemTable * item_table;

		if (m_pkPC)
		{
			pkItem = m_pkPC->GetItem(pTable->pos);

			if (!pkItem)
			{
				sys_err("cannot find item on pos (%d, %d) (name: %s)", pTable->pos.window_type, pTable->pos.cell, m_pkPC->GetName());
				continue;
			}

			item_table = pkItem->GetProto();
		}
		else
		{
			if (!pTable->vnum)
				continue;

			item_table = ITEM_MANAGER::instance().GetTable(pTable->vnum);
		}

		if (!item_table)
		{
			sys_err("Shop: no item table by item vnum #%d", pTable->vnum);
			continue;
		}

		int iPos;

		if (IsPCShop())
		{
			sys_log(0, "MyShop: use position %d", pTable->display_pos);
			iPos = pTable->display_pos;
		}
		else
			iPos = m_pGrid->FindBlank(1, item_table->bSize);

		if (iPos < 0)
		{
			sys_err("not enough shop window");
			continue;
		}

		if (!m_pGrid->IsEmpty(iPos, 1, item_table->bSize))
		{
			if (IsPCShop())
			{
				sys_err("not empty position for pc shop %s[%d]", m_pkPC->GetName(), m_pkPC->GetPlayerID());
			}
			else
			{
				sys_err("not empty position for npc shop");
			}
			continue;
		}

		m_pGrid->Put(iPos, 1, item_table->bSize);

		SHOP_ITEM & item = m_itemVector[iPos];

		item.pkItem = pkItem;
		item.itemid = 0;

		if (item.pkItem)
		{
			item.vnum = pkItem->GetVnum();
			item.count = pkItem->GetCount(); 
			item.price = pTable->price; 
			item.itemid	= pkItem->GetID();
#ifdef ENABLE_CHEQUE_SYSTEM
			item.cheque = pTable->cheque;
#endif
#ifdef PRICE_TYPE
			item.price_type = pTable->price_type;
#endif
#ifdef SHOP_STOK
			item.stok = pTable->stok;
#endif

		}
		else
		{
			item.vnum = pTable->vnum;
			item.count = pTable->count;
			
#ifdef PRICE_TYPE
			item.price = pTable->price;
			item.price_type = pTable->price_type;
#endif
#ifdef SHOP_STOK
			item.stok = pTable->stok;
#endif
#ifdef ENABLE_CHEQUE_SYSTEM
			item.cheque = 0;
#endif


			if (IS_SET(item_table->dwFlags, ITEM_FLAG_COUNT_PER_1GOLD))
			{
				if (item_table->dwGold == 0)
				{
					item.price = item.count;
				}
				else
				{
					item.price = item.count / item_table->dwGold;
				}
			}
			else
			{
#ifdef PRICE_TYPE
				item.price = item.price * item.count;
#else				
				item.price = item_table->dwGold * item.count;
#endif
			}

		}

		char name[36];
		snprintf(name, sizeof(name), "%-20s(#%-5d) (x %d)", item_table->szName, (int) item.vnum, item.count);

#ifdef PRICE_TYPE
		sys_log(0, "SHOP_ITEM: %-36s PRICE %-5d Type %d Stok %d", name, item.price, item.price_type, item.stok);
#else
		sys_log(0, "SHOP_ITEM: %-36s PRICE %-5d", name, item.price);
#endif
		++pTable;
	}
}

#ifdef OFFLINE_SHOP
#include "char.h"
int CShop::Buy(LPCHARACTER ch, BYTE pos)
{
	if (IsLocked())
		return SHOP_SUBHEADER_GC_END;
	
	if (pos >= m_itemVector.size())
	{
		sys_log(0, "Shop::Buy : invalid position %d : %s", pos, ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}

	sys_log(0, "Shop::Buy : name %s pos %d", ch->GetName(), pos);

	GuestMapType::iterator it = m_map_guest.find(ch);

	if (it == m_map_guest.end())
		return SHOP_SUBHEADER_GC_END;

	SHOP_ITEM& r_item = m_itemVector[pos];

	if (r_item.price < 0)
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLD_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
	if (r_item.cheque<0)
	{
		LogManager::instance().HackLog("SHOP_BUY_CHEQUE_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_CHEQUE;
	}
#endif

	LPITEM pkSelectedItem = ITEM_MANAGER::instance().Find(r_item.itemid);
	
#ifdef FULL_YANG
	long long dwPrice = r_item.price;
#else
	DWORD dwPrice = r_item.price;
#endif
#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
	DWORD dwCheque = r_item.cheque;
#endif
	DWORD dwTax = 0;
	int iVal = quest::CQuestManager::instance().GetEventFlag ("personal_shop");

	if (0 < iVal)
	{
		if (iVal > 100)
		{
			iVal = 100;
		}

		dwTax = dwPrice * iVal / 100;
		dwPrice = dwPrice - dwTax;
	}
	else
	{
		iVal = 0;
		dwTax = 0;
	}
#ifdef SHOP_STOK
	DWORD dwStok = r_item.stok;
	if (!IsPCShop() && dwStok < 1)
	{
		sys_log(1, "stok yok! ");
		return SHOP_SUBHEADER_GC_STOK;
	}
#endif
#ifdef PRICE_TYPE
	DWORD dwPriceType = r_item.price_type;
	int ep = 0;
	if (dwPriceType == 0)
	{
		if (ch->GetGold() < (int) dwPrice && ch->GetCheque() >= (int) dwCheque)
		{
			sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
		}
		if (ch->GetCheque() < (int) dwCheque && ch->GetGold() >= (int) dwPrice)
		{
			sys_log(1, "Shop::Buy : Not enough won : %s has %d, price_cheque %d", ch->GetName(), ch->GetCheque(), dwCheque);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_CHEQUE;
		}
		if (ch->GetGold() < (int) dwPrice && ch->GetCheque() < (int) dwCheque)
		{
			sys_log(1, "Shop::Buy : Not enough won_money : %s has %d and %d, price %d and price_cheque %d", ch->GetName(), ch->GetGold(), ch->GetCheque(), dwPrice, dwCheque);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_CHEQUE;
		}
	}
	else if (dwPriceType == 2)
	{
		ep = ch->GetDragonCoin();
		if (ep < (int) dwPrice)
		{
			sys_log(1, "Shop::Buy : Not enough EP : %s has %d, price %d, type %d", ch->GetName(), ep, dwPrice, dwPriceType);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_EX_EP;
		}
		
	}
	else if (dwPriceType == 3)
	{
		if (ch->GetCheque() < (int) dwPrice)
		{
			sys_log(1, "Shop::Buy : Not enough won : %s has %d, price %d, type %d", ch->GetName(), ch->GetCheque(), dwPrice, dwPriceType);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_CHEQUE;
		}
	}
	else
	{
		if (ch->CountSpecifyItem(dwPriceType) < (int) dwPrice)
		{
			sys_log(1, "Shop::Buy : Not enough item : %s has %d, price %d, type %d", ch->GetName(), ch->CountSpecifyItem(dwPriceType), dwPrice, dwPriceType);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_ITEM;
		}
			
	}
#else
	#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
		if ((int)dwPrice>0 && (int)dwCheque > 0) // Yang-Cheque
		{
			if (ch->GetGold() < (int)dwPrice || ch->GetCheque() < (int)dwCheque)
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_CHEQUE;
		}
		else if ((int)dwPrice>0 && (int)dwCheque <= 0) // Yang
		{
			if (ch->GetGold() < (int)dwPrice)
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
		}
		else if ((int)dwPrice<=0 && (int)dwCheque > 0) // cheque
		{
			if (ch->GetCheque() < (int)dwCheque)
				return SHOP_SUBHEADER_GC_NOT_ENOUGH_CHEQUE;
		}
	#else
		if (ch->GetGold() < r_item.price)
		{
			sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
		}
	#endif
#endif

	LPITEM item;

	if (m_pkPC) 
		item = r_item.pkItem;
	else {
		item = ITEM_MANAGER::instance().CreateItem(r_item.vnum, r_item.count);
	}
	if (!item)
		return SHOP_SUBHEADER_GC_SOLD_OUT;

#ifdef ENABLE_SHOP_BLACKLIST
	if (!m_pkPC)
	{
		if (quest::CQuestManager::instance().GetEventFlag("hivalue_item_sell") == 0)
		{
			//축복의 구슬 && 만년한철 이벤트
			if (item->GetVnum() == 70024 || item->GetVnum() == 70035)
			{
				return SHOP_SUBHEADER_GC_END;
			}
		}
	}
#endif

	int iEmptyPos;
	if (item->IsDragonSoul())
	{
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
	}
	else
	{
		iEmptyPos = ch->GetEmptyInventory(item->GetSize());
	}

	if (iEmptyPos < 0)
	{
		if (m_pkPC)
		{
			sys_log(1, "Shop::Buy at PC Shop : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
		else
		{
			sys_log(1, "Shop::Buy : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			M2_DESTROY_ITEM(item);
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
	}
	
	
#ifdef PRICE_TYPE
	
	if (dwPriceType == 0)
	{
		#ifdef FULL_YANG_OWN
			ch->ChangeGold(-dwPrice);
		#else
			ch->PointChange(POINT_GOLD, -dwPrice, false);
		#endif
		#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
			ch->PointChange(POINT_CHEQUE, -dwCheque, false);
		#endif
	}
	else if (dwPriceType == 2)
	{
		ch->SetDragonCoin(ep-dwPrice);
	}
	else if (dwPriceType == 3)
	{
		ch->PointChange(POINT_CHEQUE, -dwPrice, false);
	}
	else
	{
		ch->RemoveSpecifyItem(dwPriceType, dwPrice);
	}
#else
	#ifdef FULL_YANG_OWN
		ch->ChangeGold(-dwPrice);
	#else
		ch->PointChange(POINT_GOLD, -dwPrice, false);
	#endif
	#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
		ch->PointChange(POINT_CHEQUE, -dwCheque, false);
	#endif
#endif

#ifdef SHOP_STOK
	if (!IsPCShop() && dwStok != 999)
	{
		sys_log(1, "stok azaldi! ");
		r_item.stok--;
		BroadcastUpdateItem(pos);
	}
#endif
	

	// ±?AO ˝?˝??? : ??±Y Aˇ?o
	if (m_pkPC)
	{
		if (!m_pkPC->IsPrivShop())
			m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);

		char buf[512];
		DWORD mpid = (m_pkPC->IsPrivShop() ? m_pkPC->GetPrivShopOwner() : m_pkPC->GetPlayerID());
		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			snprintf(buf, sizeof(buf), "%s FROM: %u TO: %u PRICE: %u", item->GetName(), ch->GetPlayerID(), mpid, dwPrice);
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), SHOP_BUY, buf);
			LogManager::instance().GoldBarLog(mpid, item->GetID(), SHOP_SELL, buf);
		}
		LPITEM pkNewItem = ITEM_MANAGER::instance().CreateItem(r_item.vnum, r_item.count);

		if (pkNewItem)
		{
			for (int i = 0; i < ITEM_SOCKET_MAX_NUM; i++)
			{
				pkNewItem->SetSocket(i, item->GetSocket(i));
			}
			// 매직 아이템 설정
			item->CopyAttributeTo(pkNewItem);

			if (pkNewItem->IsDragonSoul())
				pkNewItem->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
			else
				pkNewItem->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			item->RemoveFromCharacter();
			M2_DESTROY_ITEM(item);
			ITEM_MANAGER::instance().FlushDelayedSave(pkNewItem);
			std::string szBuy("SHOP_BUY");
			std::string szSell("SHOP_SELL");
			if (m_pkPC->IsPrivShop())
			{
				std::string temp("OFFLINE_");
				szBuy = temp + szBuy;
				szSell = temp + szSell;
			}
#ifdef FULL_YANG
			snprintf(buf, sizeof(buf), "%s %u(%s) %lld %u", pkNewItem->GetName(), mpid, m_pkPC->GetName(), dwPrice, pkNewItem->GetCount());
			LogManager::instance().ItemLog(ch, pkNewItem, szBuy.c_str(), buf);
			snprintf(buf, sizeof(buf), "%s %u(%s) %lld %u", pkNewItem->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, pkNewItem->GetCount());
			LogManager::instance().ItemLog(m_pkPC, pkNewItem, szSell.c_str(), buf);
#else
			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", pkNewItem->GetName(), mpid, m_pkPC->GetName(), dwPrice, pkNewItem->GetCount());
			LogManager::instance().ItemLog(ch, pkNewItem, szBuy.c_str(), buf);
			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", pkNewItem->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, pkNewItem->GetCount());
			LogManager::instance().ItemLog(m_pkPC, pkNewItem, szSell.c_str(), buf);
#endif

			r_item.pkItem = NULL;
			BroadcastUpdateItem(pos);
			if (m_pkPC->IsPrivShop()) {
				LPCHARACTER owner = CHARACTER_MANAGER::instance().FindByPID(m_pkPC->GetPrivShopOwner());
				

#ifdef FULL_YANG
					DBManager::instance().DirectQuery("UPDATE player_shop SET gold=gold + %lld WHERE id=%d", dwPrice, m_pkPC->GetPrivShop());
#else
					DBManager::instance().DirectQuery("UPDATE player_shop SET gold=gold + %d WHERE id=%d", dwPrice, m_pkPC->GetPrivShop());
#endif
#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
				DBManager::instance().DirectQuery("UPDATE player_shop SET cheque=cheque + %d WHERE id=%d", dwCheque, m_pkPC->GetPrivShop());
#endif
					
			
				DBManager::instance().DirectQuery("DELETE FROM player_shop_items WHERE shop_id=%d and id = %d", m_pkPC->GetPrivShop(), r_item.itemid);
				if (owner)
				{
					owner->LoadPrivShops();
					if (owner->GetGiftPages() > 0)
						owner->ChatPacket(CHAT_TYPE_COMMAND, "gift_info %d", owner->GetGiftPages());
				}
			}
			else
			{
				
#ifdef PRICE_TYPE
				if (dwPriceType == 0)
				{
					#ifdef FULL_YANG_OWN
						m_pkPC->ChangeGold(dwPrice);
					#else
						m_pkPC->PointChange(POINT_GOLD, dwPrice, false);
					#endif
					#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
						m_pkPC->PointChange(POINT_CHEQUE, dwCheque, false);
					#endif
				}
				else if (dwPriceType == 2)
				{
					int ep2 = m_pkPC->GetDragonCoin();
					m_pkPC->SetDragonCoin(ep2-dwPrice);
				}
				else
				{
					m_pkPC->RemoveSpecifyItem(dwPriceType, dwPrice);
				}
#else
				#ifdef FULL_YANG_OWN
					m_pkPC->ChangeGold(dwPrice);
				#else
					m_pkPC->PointChange(POINT_GOLD, dwPrice, false);
				#endif
				#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
					m_pkPC->PointChange(POINT_CHEQUE, dwCheque, false);
				#endif

#endif

				if (iVal > 0)
				{
					m_pkPC->ChatPacket (CHAT_TYPE_INFO, LC_TEXT ("판매금액의 %d %% 가 세금으로 나가게됩니다"), iVal);
				}

			}
			item = pkNewItem;
		}
		else {
			return SHOP_SUBHEADER_GC_INVALID_POS;
		}


	}
	else
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		LogManager::instance().ItemLog(ch, item, "BUY", item->GetName());

		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), PERSONAL_SHOP_BUY, "");
		}

		//DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), -dwPrice);
	}

	if (item)
		sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price %u", ch->GetName(), item->GetName(), item->GetCount(), item->GetID(), dwPrice);
	ch->Save();
#ifdef ENABLE_OFFLINESHOP_MESSAGE_SYSTEM
	if (m_pkPC && m_pkPC->IsPrivShop())
	{
		LPCHARACTER tch = CHARACTER_MANAGER::instance().FindByPID(m_pkPC->GetPrivShopOwner());

		if (tch && item)
		{
			char msg[CHAT_MAX_LEN + 1];
			snprintf(msg, sizeof(msg), LC_TEXT("Your item %s sold, buyer is: %s."), item->GetName(), ch->GetName());

			LPDESC pkVictimDesc = tch->GetDesc();
			
			if (pkVictimDesc)
			{
				TPacketGCWhisper pack;

				int len = MIN(CHAT_MAX_LEN, strlen(msg) + 1);

				pack.bHeader = HEADER_GC_WHISPER;
				pack.wSize = sizeof(TPacketGCWhisper) + len;
				pack.bType = WHISPER_TYPE_SYSTEM;
				strlcpy(pack.szNameFrom, "[D?kan]", sizeof(pack.szNameFrom));

				TEMP_BUFFER buf;

				buf.write(&pack, sizeof(TPacketGCWhisper));
				buf.write(msg, len);

				pkVictimDesc->Packet(buf.read_peek(), buf.size());
			}

			//tch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Market Tezg??dan nesne sat?d? %s."), item->GetName());
		}
		else if (item)
		{
			// P2P_FIND

			TPacketGGOfflineShopMessage p;
			p.bHeader = HEADER_GG_OFFLINE_SHOP_SEND_MESSAGE;
			p.dwTargetPID = m_pkPC->GetPrivShopOwner();
			strlcpy(p.szItemName, item->GetName(), sizeof(p.szItemName));
			strlcpy(p.szName, ch->GetName(), sizeof(p.szName));
			P2P_MANAGER::instance().Send(&p, sizeof(TPacketGGOfflineShopMessage));
		}
	}
#endif
#if defined(SHOP_AUTO_CLOSE) && defined(OFFLINE_SHOP)
	if (m_pkPC && m_pkPC->IsPrivShop())
	{
		if (GetItemCount()<=0)
			m_pkPC->DeleteMyShop();
	}
#endif
	return (SHOP_SUBHEADER_GC_OK);
}
void CShop::RemoveGuests(LPCHARACTER except)
{
	GuestMapType::iterator it = m_map_guest.begin();
	while (it != m_map_guest.end())
	{
		LPCHARACTER ch = it->first;
		if (except && ch == except)
		{
			it++;
			continue;
		}
		if (ch)
		{
			ch->SetShop(NULL);

			TPacketGCShop pack;

			pack.header = HEADER_GC_SHOP;
			pack.subheader = SHOP_SUBHEADER_GC_END;
			pack.size = sizeof(TPacketGCShop);

			ch->GetDesc()->Packet(&pack, sizeof(pack));
		}
		m_map_guest.erase(it++);
	}
}
void CShop::ClearItems()
{
	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		m_itemVector[i].pkItem = NULL;
		BroadcastUpdateItem(i);
	}
}
int CShop::GetItemCount()
{
	int count = 0;
	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		if (m_itemVector[i].pkItem)
			count++;
	}
	return count;
}
bool CShop::GetItems()
{
	if (!m_pkPC)
		return false;
	if (!m_pkPC)
		return false;
	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		if (!m_itemVector[i].pkItem)
			continue;
		char query[8192];
		sprintf(query, "INSERT INTO player_gift SET \
		owner_id=%d,vnum=%d,count=%d,reason='%s',`from`=replace(\"%s\",' ','_'),status='WAIT',date_add=NOW()",
		m_pkPC->GetPrivShopOwner(), m_itemVector[i].vnum, m_itemVector[i].count, LC_TEXT("SHOP_REASON"), m_pkPC->GetName());

		for (int s = 0; s < ITEM_SOCKET_MAX_NUM; s++)
		{
			sprintf(query, "%s, socket%d='%ld'", query, s, m_itemVector[i].pkItem->GetSocket(s));

		}
		for (int ia = 0; ia < ITEM_ATTRIBUTE_MAX_NUM; ia++)
		{
			const TPlayerItemAttribute& attr = m_itemVector[i].pkItem->GetAttribute(ia);
			if (ia < 7)
			{
				sprintf(query, "%s, attrtype%d='%u'", query, ia, attr.bType);
				sprintf(query, "%s, attrvalue%d='%d'", query, ia, attr.sValue);
			}
			else
			{
				sprintf(query, "%s, applytype%d='%u'", query, ia-7, attr.bType);
				sprintf(query, "%s, applyvalue%d='%d'", query, ia-7, attr.sValue);
			}
		}
		DBManager::instance().DirectQuery(query);

		DBManager::instance().DirectQuery("delete from player_shop_items where id='%d'", m_itemVector[i].itemid);
		m_itemVector[i].pkItem->RemoveFromCharacter();
		m_itemVector[i].pkItem = NULL;
		BroadcastUpdateItem(i);

	}


	return true;
}
void CShop::SetPrivShopItems(std::vector<TShopItemTable *> map_shop)
{
	m_pGrid->Clear();

	m_itemVector.resize(SHOP_HOST_ITEM_MAX_NUM);
	memset(&m_itemVector[0], 0, sizeof(SHOP_ITEM) * m_itemVector.size());

	for (DWORD count = 0;count < map_shop.size();count++)
	{
		TShopItemTable * pTable = map_shop[count];
			LPITEM pkItem = NULL;
			const TItemTable * item_table;

			if (!m_pkPC)
				return;
			pkItem = m_pkPC->GetItem(pTable->pos);

			if (!pkItem)
			{
				sys_err("cannot find item on pos (%d, %d) (name: %s)", pTable->pos.window_type, pTable->pos.cell, m_pkPC->GetName());
				continue;
			}

		item_table = pkItem->GetProto();


		if (!item_table)
		{
			sys_err("Shop: no item table by item vnum #%d", pTable->vnum);
			continue;
		}

		WORD iPos = pTable->display_pos;
		sys_log(0, "MyShop: use position %d", iPos);


		if (iPos < 0)
		{
			sys_err("not enough shop window");
			continue;
		}

		if (!m_pGrid->IsEmpty(iPos, 1, item_table->bSize))
		{
			sys_err("not empty position for pc shop %s[%d] fixing", m_pkPC->GetName(), m_pkPC->GetPlayerID());
			iPos = m_pGrid->FindBlank(1, item_table->bSize);
			if (!m_pGrid->IsEmpty(iPos, 1, item_table->bSize))
			{
				sys_err("not empty position for pc shop %s[%d]", m_pkPC->GetName(), m_pkPC->GetPlayerID());
				continue;
			}
		}

		m_pGrid->Put(iPos, 1, item_table->bSize);

		SHOP_ITEM & item = m_itemVector[iPos];

		item.pkItem = pkItem;
		item.itemid = 0;
#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
		item.cheque = 0;
#endif

		if (item.pkItem)
		{
			item.vnum = pkItem->GetVnum();
			item.count = pkItem->GetCount(); // PC ?? ?? ??? ??? ?? ???? ???? ??.
			item.price = pTable->price; // ??? ???? ????..
			item.itemid = pkItem->GetRealID();
#ifdef ENABLE_OFFLINE_SHOP_USE_CHEQUE
			item.cheque = pTable->cheque;
#endif
		}

		char name[36];
		snprintf(name, sizeof(name), "%-20s(#%-5d) (x %d)", item_table->szName, (int)item.vnum, item.count);

		sys_log(0, "PRIV_SHOP_ITEM: %-36s PRICE %-5d", name, item.price);
	}
}
#else
int CShop::Buy(LPCHARACTER ch, BYTE pos)
{
	if (pos >= m_itemVector.size())
	{
		sys_log(0, "Shop::Buy : invalid position %d : %s", pos, ch->GetName());
		return SHOP_SUBHEADER_GC_INVALID_POS;
	}

	sys_log(0, "Shop::Buy : name %s pos %d", ch->GetName(), pos);

	GuestMapType::iterator it = m_map_guest.find(ch);

	if (it == m_map_guest.end())
		return SHOP_SUBHEADER_GC_END;

	SHOP_ITEM& r_item = m_itemVector[pos];
//0 Yang ?em Almama Fix
	if (r_item.price < 0)
//0 Yang ?em Almama Fix
	{
		LogManager::instance().HackLog("SHOP_BUY_GOLD_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
#ifdef ENABLE_SHOP_USE_CHEQUE
	if (r_item.cheque<0)
	{
		LogManager::instance().HackLog("SHOP_BUY_CHEQUE_OVERFLOW", ch);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_CHEQUE;
	}
#endif

	LPITEM pkSelectedItem = ITEM_MANAGER::instance().Find(r_item.itemid);

	if (IsPCShop())
	{
		if (!pkSelectedItem)
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(),
					m_pkPC->GetPlayerID());

			return SHOP_SUBHEADER_GC_SOLD_OUT; // @fixme132 false to SHOP_SUBHEADER_GC_SOLD_OUT
		}

		if ((pkSelectedItem->GetOwner() != m_pkPC))
		{
			sys_log(0, "Shop::Buy : Critical: This user seems to be a hacker : invalid pcshop item : BuyerPID:%d SellerPID:%d",
					ch->GetPlayerID(),
					m_pkPC->GetPlayerID());

			return SHOP_SUBHEADER_GC_SOLD_OUT; // @fixme132 false to SHOP_SUBHEADER_GC_SOLD_OUT
		}
	}

	DWORD dwPrice = r_item.price;
#ifdef ENABLE_SHOP_USE_CHEQUE
	DWORD dwCheque = r_item.cheque;
#endif

	//if (it->second)	// if other empire, price is triple
	//	dwPrice *= 3;

#ifdef ENABLE_SHOP_USE_CHEQUE
	if ((int)dwPrice>0 && (int)dwCheque > 0) // Yang-Cheque
	{
		if (ch->GetGold() < (int)dwPrice || ch->GetCheque() < (int)dwCheque)
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY_CHEQUE;
	}
	else if ((int)dwPrice>0 && (int)dwCheque <= 0) // Yang
	{
		if (ch->GetGold() < (int)dwPrice)
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
	else if ((int)dwPrice<=0 && (int)dwCheque > 0) // cheque
	{
		if (ch->GetCheque() < (int)dwCheque)
			return SHOP_SUBHEADER_GC_NOT_ENOUGH_CHEQUE;
	}
#else
	if (ch->GetGold() < (int) dwPrice)
	{
		sys_log(1, "Shop::Buy : Not enough money : %s has %d, price %d", ch->GetName(), ch->GetGold(), dwPrice);
		return SHOP_SUBHEADER_GC_NOT_ENOUGH_MONEY;
	}
#endif

	LPITEM item;

	if (m_pkPC) 
		item = r_item.pkItem;
	else
		item = ITEM_MANAGER::instance().CreateItem(r_item.vnum, r_item.count);

	if (!item)
		return SHOP_SUBHEADER_GC_SOLD_OUT;

#ifdef ENABLE_SHOP_BLACKLIST
	if (!m_pkPC)
	{
		if (quest::CQuestManager::instance().GetEventFlag("hivalue_item_sell") == 0)
		{
			
			if (item->GetVnum() == 70024 || item->GetVnum() == 70035)
			{
				return SHOP_SUBHEADER_GC_END;
			}
		}
	}
#endif

	int iEmptyPos;
	if (item->IsDragonSoul())
	{
		iEmptyPos = ch->GetEmptyDragonSoulInventory(item);
	}
#ifdef ENABLE_SPECIAL_STORAGE
	else if (item->IsUpgradeItem())
		iEmptyPos = ch->GetEmptyUpgradeInventory(item);
	else if (item->IsBook())
		iEmptyPos = ch->GetEmptyBookInventory(item);
	else if (item->IsStone())
		iEmptyPos = ch->GetEmptyStoneInventory(item);
#endif
	else
	{
		iEmptyPos = ch->GetEmptyInventory(item->GetSize());
	}

	if (iEmptyPos < 0)
	{
		if (m_pkPC)
		{
			sys_log(1, "Shop::Buy at PC Shop : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
		else
		{
			sys_log(1, "Shop::Buy : Inventory full : %s size %d", ch->GetName(), item->GetSize());
			M2_DESTROY_ITEM(item);
			return SHOP_SUBHEADER_GC_INVENTORY_FULL;
		}
	}

	ch->PointChange(POINT_GOLD, -dwPrice, false);
#ifdef ENABLE_SHOP_USE_CHEQUE
	ch->PointChange(POINT_CHEQUE, -dwCheque, false);
#endif

	DWORD dwTax = 0;
	int iVal = 0;

	{
		iVal = quest::CQuestManager::instance().GetEventFlag("personal_shop");

		if (0 < iVal)
		{
			if (iVal > 100)
				iVal = 100;

			dwTax = dwPrice * iVal / 100;
			dwPrice = dwPrice - dwTax;
		}
		else
		{
			iVal = 0;
			dwTax = 0;
		}
	}

	
	if (!m_pkPC)
	{
		CMonarch::instance().SendtoDBAddMoney(dwTax, ch->GetEmpire(), ch);
	}

	
	if (m_pkPC)
	{
		m_pkPC->SyncQuickslot(QUICKSLOT_TYPE_ITEM, item->GetCell(), 255);

		if (item->GetVnum() == 90008 || item->GetVnum() == 90009) // VCARD
		{
			VCardUse(m_pkPC, ch, item);
			item = NULL;
		}
		else
		{
			char buf[512];

			if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
			{
				snprintf(buf, sizeof(buf), "%s FROM: %u TO: %u PRICE: %u", item->GetName(), ch->GetPlayerID(), m_pkPC->GetPlayerID(), dwPrice);
				LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), SHOP_BUY, buf);
				LogManager::instance().GoldBarLog(m_pkPC->GetPlayerID(), item->GetID(), SHOP_SELL, buf);
			}

			item->RemoveFromCharacter();
			if (item->IsDragonSoul())
				item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
#ifdef ENABLE_SPECIAL_STORAGE
			else if (item->IsUpgradeItem())
				item->AddToCharacter(ch, TItemPos(UPGRADE_INVENTORY, iEmptyPos));
			else if (item->IsBook())
				item->AddToCharacter(ch, TItemPos(BOOK_INVENTORY, iEmptyPos));
			else if (item->IsStone())
				item->AddToCharacter(ch, TItemPos(STONE_INVENTORY, iEmptyPos));
#endif
			else
				item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
			ITEM_MANAGER::instance().FlushDelayedSave(item);


			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), m_pkPC->GetPlayerID(), m_pkPC->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(ch, item, "SHOP_BUY", buf);

			snprintf(buf, sizeof(buf), "%s %u(%s) %u %u", item->GetName(), ch->GetPlayerID(), ch->GetName(), dwPrice, item->GetCount());
			LogManager::instance().ItemLog(m_pkPC, item, "SHOP_SELL", buf);
		}

		r_item.pkItem = NULL;
		BroadcastUpdateItem(pos);

		m_pkPC->PointChange(POINT_GOLD, dwPrice, false);
#ifdef ENABLE_SHOP_USE_CHEQUE
		m_pkPC->PointChange(POINT_CHEQUE, dwCheque, false);
#endif

		if (iVal > 0)
			m_pkPC->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("판매금액의 %d %% 가 세금으로 나가게됩니다"), iVal);

		CMonarch::instance().SendtoDBAddMoney(dwTax, m_pkPC->GetEmpire(), m_pkPC);
	}
	else
	{
		if (item->IsDragonSoul())
			item->AddToCharacter(ch, TItemPos(DRAGON_SOUL_INVENTORY, iEmptyPos));
#ifdef ENABLE_SPECIAL_STORAGE
		else if (item->IsUpgradeItem())
			item->AddToCharacter(ch, TItemPos(UPGRADE_INVENTORY, iEmptyPos));
		else if (item->IsBook())
			item->AddToCharacter(ch, TItemPos(BOOK_INVENTORY, iEmptyPos));
		else if (item->IsStone())
			item->AddToCharacter(ch, TItemPos(STONE_INVENTORY, iEmptyPos));
#endif
		else
			item->AddToCharacter(ch, TItemPos(INVENTORY, iEmptyPos));
		ITEM_MANAGER::instance().FlushDelayedSave(item);
		LogManager::instance().ItemLog(ch, item, "BUY", item->GetName());

		if (item->GetVnum() >= 80003 && item->GetVnum() <= 80007)
		{
			LogManager::instance().GoldBarLog(ch->GetPlayerID(), item->GetID(), PERSONAL_SHOP_BUY, "");
		}

		DBManager::instance().SendMoneyLog(MONEY_LOG_SHOP, item->GetVnum(), -dwPrice);
	}

	if (item)
		sys_log(0, "SHOP: BUY: name %s %s(x %d):%u price %u", ch->GetName(), item->GetName(), item->GetCount(), item->GetID(), dwPrice);

    ch->Save();

    return (SHOP_SUBHEADER_GC_OK);
}
#endif

bool CShop::AddGuest(LPCHARACTER ch, DWORD owner_vid, bool bOtherEmpire)
{
	if (!ch)
		return false;

	if (ch->GetExchange())
		return false;

	if (ch->GetShop())
		return false;

	ch->SetShop(this);

	m_map_guest.insert(GuestMapType::value_type(ch, bOtherEmpire));

	TPacketGCShop pack;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_START;

	TPacketGCShopStart pack2;

	memset(&pack2, 0, sizeof(pack2));
	pack2.owner_vid = owner_vid;

	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		const SHOP_ITEM & item = m_itemVector[i];

#ifdef ENABLE_SHOP_BLACKLIST
		//HIVALUE_ITEM_EVENT
		if (quest::CQuestManager::instance().GetEventFlag("hivalue_item_sell") == 0)
		{
			
			if (item.vnum == 70024 || item.vnum == 70035)
			{
				continue;
			}
		}
#endif
		//END_HIVALUE_ITEM_EVENT
		if (m_pkPC && !item.pkItem)
			continue;

		pack2.items[i].vnum = item.vnum;

		// REMOVED_EMPIRE_PRICE_LIFT
#ifdef ENABLE_NEWSTUFF
		if (bOtherEmpire && !g_bEmpireShopPriceTripleDisable) // no empire price penalty for pc shop
#else
		if (bOtherEmpire) // no empire price penalty for pc shop
#endif
		{
			pack2.items[i].price = item.price * 3;
		}
		else
		{
			pack2.items[i].price = item.price;
		}
#ifdef ENABLE_CHEQUE_SYSTEM
		pack2.items[i].cheque = item.cheque;
#endif
#ifdef PRICE_TYPE
		if (IsPCShop())
		{
			pack2.items[i].price_type = 0;
		}
		else
		{
			pack2.items[i].price_type = item.price_type;
		}
#endif
#ifdef SHOP_STOK
		if (IsPCShop())
		{
			pack2.items[i].stok = 0;
		}
		else
		{
			pack2.items[i].stok = item.stok;
		}
#endif

		// END_REMOVED_EMPIRE_PRICE_LIFT

		pack2.items[i].count = item.count;

		if (item.pkItem)
		{
			thecore_memcpy(pack2.items[i].alSockets, item.pkItem->GetSockets(), sizeof(pack2.items[i].alSockets));
			thecore_memcpy(pack2.items[i].aAttr, item.pkItem->GetAttributes(), sizeof(pack2.items[i].aAttr));
		}
	}

	pack.size = sizeof(pack) + sizeof(pack2);

	ch->GetDesc()->BufferedPacket(&pack, sizeof(TPacketGCShop));
	ch->GetDesc()->Packet(&pack2, sizeof(TPacketGCShopStart));
	return true;
}

void CShop::RemoveGuest(LPCHARACTER ch)
{
	if (ch->GetShop() != this)
		return;

	m_map_guest.erase(ch);
	ch->SetShop(NULL);

	TPacketGCShop pack;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_END;
	pack.size		= sizeof(TPacketGCShop);

	ch->GetDesc()->Packet(&pack, sizeof(pack));
}

void CShop::Broadcast(const void * data, int bytes)
{
	sys_log(1, "Shop::Broadcast %p %d", data, bytes);

	GuestMapType::iterator it;

	it = m_map_guest.begin();

	while (it != m_map_guest.end())
	{
		LPCHARACTER ch = it->first;

		if (ch->GetDesc())
			ch->GetDesc()->Packet(data, bytes);

		++it;
	}
}

void CShop::BroadcastUpdateItem(BYTE pos)
{
	TPacketGCShop pack;
	TPacketGCShopUpdateItem pack2;

	TEMP_BUFFER	buf;

	pack.header		= HEADER_GC_SHOP;
	pack.subheader	= SHOP_SUBHEADER_GC_UPDATE_ITEM;
	pack.size		= sizeof(pack) + sizeof(pack2);

	pack2.pos		= pos;

	if (m_pkPC && !m_itemVector[pos].pkItem)
		pack2.item.vnum = 0;
	else
	{
		pack2.item.vnum	= m_itemVector[pos].vnum;
		if (m_itemVector[pos].pkItem)
		{
			thecore_memcpy(pack2.item.alSockets, m_itemVector[pos].pkItem->GetSockets(), sizeof(pack2.item.alSockets));
			thecore_memcpy(pack2.item.aAttr, m_itemVector[pos].pkItem->GetAttributes(), sizeof(pack2.item.aAttr));
		}
		else
		{
			memset(pack2.item.alSockets, 0, sizeof(pack2.item.alSockets));
			memset(pack2.item.aAttr, 0, sizeof(pack2.item.aAttr));
		}
	}

	pack2.item.price	= m_itemVector[pos].price;
#ifdef ENABLE_CHEQUE_SYSTEM
	pack2.item.cheque = m_itemVector[pos].cheque;
#endif
	pack2.item.count	= m_itemVector[pos].count;
#ifdef PRICE_TYPE
	pack2.item.price_type	= m_itemVector[pos].price_type;
#endif
#ifdef SHOP_STOK
	pack2.item.stok	= m_itemVector[pos].stok;
#endif

	buf.write(&pack, sizeof(pack));
	buf.write(&pack2, sizeof(pack2));

	Broadcast(buf.read_peek(), buf.size());
}

int CShop::GetNumberByVnum(DWORD dwVnum)
{
	int itemNumber = 0;

	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		const SHOP_ITEM & item = m_itemVector[i];

		if (item.vnum == dwVnum)
		{
			itemNumber += item.count;
		}
	}

	return itemNumber;
}

bool CShop::IsSellingItem(DWORD itemID)
{
	bool isSelling = false;

	for (DWORD i = 0; i < m_itemVector.size() && i < SHOP_HOST_ITEM_MAX_NUM; ++i)
	{
		if ((unsigned int)(m_itemVector[i].itemid) == itemID)
		{
			isSelling = true;
			break;
		}
	}

	return isSelling;

}

#ifdef RELOAD_SHOP
void CShop::RemoveAllGuests()
{
	if (m_map_guest.empty())
		return;
	
	for (GuestMapType::iterator it = m_map_guest.begin(); it != m_map_guest.end(); it++)
	{
		LPCHARACTER ch = it->first;
		if (ch)
		{
			if (ch->GetDesc() && ch->GetShop() == this)
			{
				ch->SetShop(NULL);

				TPacketGCShop pack;

				pack.header = HEADER_GC_SHOP;
				pack.subheader = SHOP_SUBHEADER_GC_END;
				pack.size = sizeof(TPacketGCShop);

				ch->GetDesc()->Packet(&pack, sizeof(pack));
			}
		}
	}
	m_map_guest.clear();
}
#endif

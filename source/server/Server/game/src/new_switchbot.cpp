/*
	TO DO:
		-verificacoes de lojas abertas etc;
		
*/

#include "stdafx.h"

#ifdef ENABLE_SWITCHBOT
#include "new_switchbot.h"
#include "desc.h"
#include "item.h"
#include "item_manager.h"
#include "char_manager.h"
#include "questmanager.h"
#include "buffer_manager.h"
#include "char.h"
#include "config.h"
#include "p2p.h"

bool ValidPosition(DWORD wCell)
{
	return wCell < SWITCHBOT_SLOT_COUNT;
}

/*A verificao de rodar dos talismas e trajes não verifica se está ativo o sistema
	sendo que é verificado aqui se pode ou não meter o item no bot
*/
bool SwitchbotHelper::IsValidItem(LPITEM pkItem)
{
	if (!pkItem)
		return false;

	if (!pkItem->CanSwitchItem())
		return false;
	
	switch (pkItem->GetType())
	{
	case ITEM_WEAPON:
		switch (pkItem->GetSubType()) //Evita meter flechas e aljavas no bot de rodar
		{
		case WEAPON_ARROW:
#ifdef __QUIVER_SYSTEM__
		case WEAPON_QUIVER:
#endif
			return false;
		default:
			return true;
		}

	case ITEM_ARMOR:
		switch (pkItem->GetSubType())
		{
		case ARMOR_BODY:
		case ARMOR_HEAD:
		case ARMOR_SHIELD:
		case ARMOR_WRIST:
		case ARMOR_FOOTS:
		case ARMOR_NECK:
		case ARMOR_EAR:
		#ifdef ENABLE_PENDANT  //Habilita os talismas no bot de rodar
		case ARMOR_PENDANT:
		#endif
			return true;
		}
	
	#ifdef __COSTUME_ATTR_SYSTEM__ //Habilita os trajes no bot de rodar
	case ITEM_COSTUME:
		switch (pkItem->GetSubType())
		{
			case COSTUME_BODY:
			case COSTUME_HAIR:
			#ifdef __WEAPON_COSTUME_SYSTEM__
			case COSTUME_WEAPON:
			#endif
				return true;
		}
	#endif
	
	default:
		return false;
	}
}


CSwitchbot::CSwitchbot()
{
	m_pkSwitchEvent = nullptr;
	m_table = {};
	m_isWarping = false;
	b_BotSpeed = 0;
}

CSwitchbot::~CSwitchbot()
{
	if (m_pkSwitchEvent)
	{
		event_cancel(&m_pkSwitchEvent);
		m_pkSwitchEvent = nullptr;
	}

	m_table = {};
	m_isWarping = false;
	b_BotSpeed = 0;
}

void CSwitchbot::SetTable(TSwitchbotTable table)
{
	m_table = table;
}

TSwitchbotTable CSwitchbot::GetTable()
{
	return m_table;
}

void CSwitchbot::SetPlayerId(DWORD player_id)
{
	m_table.player_id = player_id;
}

DWORD CSwitchbot::GetPlayerId(DWORD player_id)
{
	return m_table.player_id;
}

void CSwitchbot::RegisterItem(WORD wCell, DWORD item_id)
{
	if (!ValidPosition(wCell))
	{
		return;
	}

	m_table.items[wCell] = item_id;
}

void CSwitchbot::UnregisterItem(WORD wCell)
{
	if (!ValidPosition(wCell))
	{
		return;
	}

	m_table.items[wCell] = 0;
	m_table.active[wCell] = false;
	m_table.finished[wCell] = false;
	memset(&m_table.alternatives[wCell], 0, sizeof(m_table.alternatives[wCell]));
}

void CSwitchbot::SetAttributes(BYTE slot, std::vector<TSwitchbotAttributeAlternativeTable> vec_alternatives)
{
	if (!ValidPosition(slot))
	{
		return;
	}

	for (BYTE alternative = 0; alternative < SWITCHBOT_ALTERNATIVE_COUNT; ++alternative)
	{
		for (BYTE attrIdx = 0; attrIdx < MAX_NORM_ATTR_NUM; ++attrIdx)
		{
			m_table.alternatives[slot][alternative].attributes[attrIdx].bType = vec_alternatives[alternative].attributes[attrIdx].bType;
			m_table.alternatives[slot][alternative].attributes[attrIdx].sValue = vec_alternatives[alternative].attributes[attrIdx].sValue;
		}
	}
}

void CSwitchbot::SetActive(BYTE slot, bool active)
{
	if (!ValidPosition(slot))
	{
		return;
	}

	m_table.active[slot] = active;
	m_table.finished[slot] = false;
}

EVENTINFO(TSwitchbotEventInfo)
{
	CSwitchbot* pkSwitchbot;

	TSwitchbotEventInfo() : pkSwitchbot(nullptr)
	{
	}
};

EVENTFUNC(switchbot_event)
{
	TSwitchbotEventInfo* info = dynamic_cast<TSwitchbotEventInfo*>(event->info);

	if (info == NULL)
	{
		sys_err("switchbot_event> <Factor> Info Null pointer");
		return 0;
	}

	if (!info->pkSwitchbot)
	{
		sys_err("switchbot_event> <Factor> Switchbot Null pointer");
		return 0;
	}

	info->pkSwitchbot->SwitchItems();
	
	return PASSES_PER_SEC(info->pkSwitchbot->GetRealBotSpeed());
}

void CSwitchbot::Start()
{
	TSwitchbotEventInfo* info = AllocEventInfo<TSwitchbotEventInfo>();
	info->pkSwitchbot = this;

	m_pkSwitchEvent = event_create(switchbot_event, info, GetRealBotSpeed());

	CSwitchbotManager::Instance().SendSwitchbotUpdate(m_table.player_id);
	CSwitchbotManager::Instance().UpdatePlayerBotSpeed(m_table.player_id);
}

void CSwitchbot::Stop()
{
	if (m_pkSwitchEvent)
	{
		event_cancel(&m_pkSwitchEvent);
		m_pkSwitchEvent = nullptr;
	}

	memset(&m_table.active, 0, sizeof(m_table.active));

	CSwitchbotManager::Instance().SendSwitchbotUpdate(m_table.player_id);
	CSwitchbotManager::Instance().UpdatePlayerBotSpeed(m_table.player_id);
}

void CSwitchbot::Pause()
{
	if (m_pkSwitchEvent)
	{
		event_cancel(&m_pkSwitchEvent);
		m_pkSwitchEvent = nullptr;
	}
}

bool CSwitchbot::IsActive(BYTE slot)
{
	if (!ValidPosition(slot))
	{
		return false;
	}

	return m_table.active[slot];
}

bool CSwitchbot::HasActiveSlots()
{
	for (const auto& it : m_table.active)
	{
		if (it)
		{
			return true;
		}
	}

	return false;
}

bool CSwitchbot::IsSwitching()
{
	return m_pkSwitchEvent != nullptr;
}

bool CSwitchbot::IsWarping()
{
	return m_isWarping;
}

void CSwitchbot::SetIsWarping(bool warping)
{
	m_isWarping = warping;
}

float CSwitchbot::GetRealBotSpeed()
{
	switch (b_BotSpeed)
	{
		case 0:
			return 0.33f;
		case 1:
			return 0.25f;
		case 2:
			return 0.20f;
		case 3:
			return 0.16f;
		case 4:
			return 0.14f;
		case 5:
			return 0.12f;
	}
	
	return 0.33f;
}

bool CSwitchbot::CanChangeBotSpeed(BYTE bNewSpeed)
{
	if (bNewSpeed != b_BotSpeed && HasActiveSlots())
		return false;
	return true;
}


bool CSwitchbot::CanContinueSwitch(LPCHARACTER ch)
{
	if(!ch)
		return false;

	if(ch->GetExchange())
		return false;

	if(ch->GetSafebox())
		return false;

	if(ch->GetShop())
		return false;

	if (quest::CQuestManager::instance().GetPCForce(ch->GetPlayerID())->IsRunning() == true)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("You cannot trade if you're using quests"));
	}
	
	return true;
}


void CSwitchbot::SwitchItems()
{
	for (BYTE bSlot = 0; bSlot < SWITCHBOT_SLOT_COUNT; ++bSlot)
	{
		if (!m_table.active[bSlot])
		{
			continue;
		}

		m_table.finished[bSlot] = false;

		const DWORD item_id = m_table.items[bSlot];

		LPITEM pkItem = ITEM_MANAGER::Instance().Find(item_id);
		if (!pkItem)
		{
			continue;
		}
		
		LPCHARACTER pkOwner = pkItem->GetOwner();
		if (!pkOwner)
		{
			return;
		}
		

		if (CheckItem(pkItem, bSlot))
		{
			LPDESC desc = pkOwner->GetDesc();
			if (desc)
			{
				desc->ChatPacket(CHAT_TYPE_COMMAND, "switch_bot_message %s", pkItem->GetName()); // Bvural41 Bildirim 28-11-20
				pkOwner->ChatPacket(CHAT_TYPE_COMMAND, "COMMAND_BlinkExeIcon");

			}

			SetActive(bSlot, false);

			m_table.finished[bSlot] = true;

			if (!HasActiveSlots())
			{
				Stop();
			}
			else
			{
				CSwitchbotManager::Instance().SendSwitchbotUpdate(m_table.player_id);
				CSwitchbotManager::Instance().UpdatePlayerBotSpeed(m_table.player_id);
			}
		}
		else
		{
			bool stop = true;
			bool isLowLevelItem = false; //Usado unicamente para itens != de trajes e talismas
			DWORD switchItemUsed = 0; //Variavel geral para armazenar o id do item de rodar
			
			if (SWITCHBOT_PRICE_TYPE == 1)
			{
				// Rodar talismas
				// if (pkItem->IsPendant())
				// {
					// Só precisa de verificar se tem o item necessário para rodar talismas
					// for (const auto& itemPendantVnum : dwSwitchingPendantItem) {
						// if (pkOwner->CountSpecifyItem(itemPendantVnum) >= SWITCHBOT_PRICE_AMOUNT) {
							// switchItemUsed = itemPendantVnum;
							// stop = false;
							// break;
						// }
					// }
				// }
				if (pkItem->GetType() == ITEM_COSTUME) //Rodar trajes
				{
					//Só precisa de verificar se tem o item necessário para rodar trajes
					if (pkOwner->CountSpecifyItem(dwSwitchingCostumeItem) >= SWITCHBOT_PRICE_AMOUNT) {
						switchItemUsed = dwSwitchingCostumeItem;
						stop = false;
					}
				}
				else
				{
					//Verifica se o nível do item é inferior a 40
					for (int i = 0; i < ITEM_LIMIT_MAX_NUM; ++i) {
						if (pkItem->GetLimitType(i) == LIMIT_LEVEL && pkItem->GetLimitValue(i) <= 40) {
							isLowLevelItem = true;
							break;
						}
					}
					
					if (!isLowLevelItem) //Se for superior a 40 verifica se tem os rodares normais
					{
						for (const auto& itemVnum : c_arSwitchingItems) {
							if (pkOwner->CountSpecifyItem(itemVnum) >= SWITCHBOT_PRICE_AMOUNT) {
								switchItemUsed = itemVnum;
								stop = false;
								break;
							}
						}
					}
					else //Se não, vai verificar primeiro se tem os rodares verdes e só depois os normais
					{
						//Verifica primeiro se o jogador tem os rodares verdes
						for (const auto& itemLowVnum : c_arSwitchingLowItens) {
							if (pkOwner->CountSpecifyItem(itemLowVnum) >= SWITCHBOT_PRICE_AMOUNT) {
								switchItemUsed = itemLowVnum;
								stop = false;
								break;
							}
						}
						
						//Verifica em seguinte se o jogador tem os rodares normais caso não tenha rodares verdes
						if (!switchItemUsed) {
							for (const auto& itemHightVnum : c_arSwitchingItems) {
								if (pkOwner->CountSpecifyItem(itemHightVnum) >= SWITCHBOT_PRICE_AMOUNT) { 
									switchItemUsed = itemHightVnum;
									stop = false;
									break;
								}
							}
						}
					}
				}
			}
			else if (SWITCHBOT_PRICE_TYPE == 2) {
				if (pkOwner->GetGold() >= SWITCHBOT_PRICE_AMOUNT)
					stop = false;
			}
			
			//Para o bot caso stop seja verdadeiro, ou não existe item para rodar
			if (stop || (!switchItemUsed && SWITCHBOT_PRICE_TYPE != 2))
			{
				SetActive(bSlot, false);
				m_table.finished[bSlot] = false;
				if (!HasActiveSlots())
				{
					Stop();
				}
				else
				{
					CSwitchbotManager::Instance().SendSwitchbotUpdate(m_table.player_id);
					CSwitchbotManager::Instance().UpdatePlayerBotSpeed(m_table.player_id);
				}
				// Stop();

				if (SWITCHBOT_PRICE_TYPE == 1)
					pkOwner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Switchbot stopped. Out of switchers."));
				else
					pkOwner->ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Switchbot stopped. Not enough money."));

				return;
			}

			if (SWITCHBOT_PRICE_TYPE == 1)
			{
#ifdef ENABLE_SPECIAL_STORAGE
				LPITEM pkItemChanger = pkOwner->FindSpecifyItemSpecial(switchItemUsed);
#else
				LPITEM pkItemChanger = pkOwner->FindSpecifyItem(switchItemUsed);
#endif
				if (pkItemChanger)
					pkItemChanger->SetCount(pkItemChanger->GetCount() - SWITCHBOT_PRICE_AMOUNT);
				else //Se o item não existir para o bot de rodar
					Stop();
			}
			else if (SWITCHBOT_PRICE_TYPE == 2)
				pkOwner->GiveGold(-SWITCHBOT_PRICE_AMOUNT);
			
			pkItem->ChangeAttribute();
			SendItemUpdate(pkOwner, bSlot, pkItem);
		}
	}
}

bool CSwitchbot::CheckItem(LPITEM pkItem, BYTE slot)
{
	if (!ValidPosition(slot))
	{
		return false;
	}

	if (!pkItem)
	{
		return false;
	}

	bool checked = 0;

	for (const auto& alternative : m_table.alternatives[slot])
	{
		if (!alternative.IsConfigured())
		{
			continue;
		}

		BYTE configuredAttrCount = 0;
		BYTE correctAttrCount = 0;

		for (const auto& destAttr : alternative.attributes)
		{
			if (!destAttr.bType || !destAttr.sValue)
			{
				continue;
			}

			++configuredAttrCount;

			for (BYTE attrIdx = 0; attrIdx < MAX_NORM_ATTR_NUM; ++attrIdx)
			{
				const TPlayerItemAttribute& curAttr = pkItem->GetAttribute(attrIdx);

				if (curAttr.bType != destAttr.bType || curAttr.sValue < destAttr.sValue)
				{
					continue;
				}

				++correctAttrCount;
				break;
			}
		}

		checked = true;

		if (configuredAttrCount == correctAttrCount)
		{
			return true;
		}
	}

	if (!checked)
	{
		return true;
	}

	return false;
}

void CSwitchbot::SendItemUpdate(LPCHARACTER ch, BYTE slot, LPITEM item)
{
	LPDESC desc = ch->GetDesc();
	if (!desc)
	{
		return;
	}

	TPacketGCSwitchbot pack;
	pack.header = HEADER_GC_SWITCHBOT;
	pack.subheader = SUBHEADER_GC_SWITCHBOT_UPDATE_ITEM;
	pack.size = sizeof(TPacketGCSwitchbot) + sizeof(TSwitchbotUpdateItem);

	TSwitchbotUpdateItem update = {};
	update.slot = slot;
	update.vnum = item->GetVnum();
	update.count = item->GetCount();

	thecore_memcpy(update.alSockets, item->GetSockets(), sizeof(update.alSockets));
	thecore_memcpy(update.aAttr, item->GetAttributes(), sizeof(update.aAttr));

	desc->BufferedPacket(&pack, sizeof(pack));
	desc->Packet(&update, sizeof(TSwitchbotUpdateItem));
}

CSwitchbotManager::CSwitchbotManager()
{
	Initialize();
}

CSwitchbotManager::~CSwitchbotManager()
{
	Initialize();
}

void CSwitchbotManager::Initialize()
{
	m_map_Switchbots.clear();
}

void CSwitchbotManager::RegisterItem(DWORD player_id, DWORD item_id, WORD wCell)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		pkSwitchbot = new CSwitchbot();
		pkSwitchbot->SetPlayerId(player_id);
		m_map_Switchbots.insert(std::make_pair(player_id, pkSwitchbot));
	}

	if (pkSwitchbot->IsWarping())
	{
		return;
	}

	pkSwitchbot->RegisterItem(wCell, item_id);
	SendSwitchbotUpdate(player_id);
	UpdatePlayerBotSpeed(player_id);
}

void CSwitchbotManager::UnregisterItem(DWORD player_id, WORD wCell)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		return;
	}

	if (pkSwitchbot->IsWarping())
	{
		return;
	}

	pkSwitchbot->UnregisterItem(wCell);
	SendSwitchbotUpdate(player_id);
	UpdatePlayerBotSpeed(player_id);
}

void CSwitchbotManager::Start(DWORD player_id, BYTE slot, BYTE bBotSpeed, std::vector<TSwitchbotAttributeAlternativeTable> vec_alternatives)
{
	if (!ValidPosition(slot))
	{
		return;
	}

	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		sys_err("No Switchbot found for player_id %d slot %d", player_id, slot);
		return;
	}

	if (pkSwitchbot->IsActive(slot))
	{
		sys_err("Switchbot slot %d already running for player_id %d", slot, player_id);
		return;
	}
	
	if (!pkSwitchbot->CanChangeBotSpeed(bBotSpeed))
	{
		SendSwitchbotUpdate(player_id);
		UpdatePlayerBotSpeed(player_id);
		return;
	}
	
	
	pkSwitchbot->SetActive(slot, true);
	pkSwitchbot->SetAttributes(slot, vec_alternatives);
	pkSwitchbot->SetBotSpeed(bBotSpeed);
	
	if (pkSwitchbot->HasActiveSlots() && !pkSwitchbot->IsSwitching())
		pkSwitchbot->Start();
	else
	{
		SendSwitchbotUpdate(player_id);
		UpdatePlayerBotSpeed(player_id);
	}
	
}

void CSwitchbotManager::Stop(DWORD player_id, BYTE slot)
{
	if (!ValidPosition(slot))
	{
		return;
	}

	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		sys_err("No Switchbot found for player_id %d slot %d", player_id, slot);
		return;
	}

	if (!pkSwitchbot->IsActive(slot))
	{
		sys_err("Switchbot slot %d is not running for player_id %d", slot, player_id);
		return;
	}

	pkSwitchbot->SetActive(slot, false);

	if (!pkSwitchbot->HasActiveSlots() && pkSwitchbot->IsSwitching())
	{
		pkSwitchbot->Stop();
	}
	else
	{
		SendSwitchbotUpdate(player_id);
		UpdatePlayerBotSpeed(player_id);
	}
}

bool CSwitchbotManager::IsActive(DWORD player_id, BYTE slot)
{
	if (!ValidPosition(slot))
	{
		return false;
	}

	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		return false;
	}

	return pkSwitchbot->IsActive(slot);
}

bool CSwitchbotManager::IsWarping(DWORD player_id)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		return false;
	}

	return pkSwitchbot->IsWarping();
}

void CSwitchbotManager::SetIsWarping(DWORD player_id, bool warping)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		return;
	}

	pkSwitchbot->SetIsWarping(warping);
}

bool CSwitchbotManager::CanFindSwitchbot(DWORD player_id)
{
	return (FindSwitchbot(player_id) != nullptr);
}

CSwitchbot* CSwitchbotManager::FindSwitchbot(DWORD player_id)
{
	const auto& it = m_map_Switchbots.find(player_id);
	if (it == m_map_Switchbots.end())
	{
		return nullptr;
	}

	return it->second;
}

void CSwitchbotManager::P2PSendSwitchbot(DWORD player_id, WORD wTargetPort)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		sys_err("No switchbot found to transfer. (pid %d source_port %d target_port %d)", player_id, mother_port, wTargetPort);
		return;
	}

	pkSwitchbot->Pause();
	m_map_Switchbots.erase(player_id);

	TPacketGGSwitchbot pack;
	pack.wPort = wTargetPort;
	pack.table = pkSwitchbot->GetTable();

	P2P_MANAGER::Instance().Send(&pack, sizeof(pack));
}

void CSwitchbotManager::P2PReceiveSwitchbot(TSwitchbotTable table)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(table.player_id);
	if (!pkSwitchbot)
	{
		pkSwitchbot = new CSwitchbot();
		m_map_Switchbots.insert(std::make_pair(table.player_id, pkSwitchbot));
	}

	pkSwitchbot->SetTable(table);
}

void CSwitchbotManager::SendItemAttributeInformations(LPCHARACTER ch)
{
	if (!ch)
	{
		return;
	}

	LPDESC desc = ch->GetDesc();
	if (!desc)
	{
		return;
	}

	TPacketGCSwitchbot pack;
	pack.header = HEADER_GC_SWITCHBOT;
	pack.subheader = SUBHEADER_GC_SWITCHBOT_SEND_ATTRIBUTE_INFORMATION;
	pack.size = sizeof(TPacketGCSwitchbot);

	TEMP_BUFFER buf;
	for (BYTE bAttributeSet = ATTRIBUTE_SET_WEAPON; bAttributeSet <= ATTRIBUTE_SET_EAR; ++bAttributeSet)
	{
		for (int iApplyNum = 0; iApplyNum < MAX_APPLY_NUM; ++iApplyNum)
		{
			const TItemAttrTable& r = g_map_itemAttr[iApplyNum];

			BYTE max = r.bMaxLevelBySet[bAttributeSet];
			if (max > 0)
			{
				TSwitchbottAttributeTable table = {};
				table.attribute_set = bAttributeSet;
				table.apply_num = iApplyNum;
				table.max_value = r.lValues[max-1];

				buf.write(&table, sizeof(table));
			}
		}
	}

#ifdef __COSTUME_ATTR_SYSTEM__
	for (BYTE bAttributeSetCostume = ATTRIBUTE_SET_COSTUME_BODY; bAttributeSetCostume <= ATTRIBUTE_SET_COSTUME_WEAPON; ++bAttributeSetCostume)
	{
		for (int iApplyCostumeNum = 0; iApplyCostumeNum < MAX_APPLY_NUM; ++iApplyCostumeNum)
		{
			const TItemAttrTable& r_costume = g_map_itemAttrCostume[iApplyCostumeNum];

			BYTE max_costume = r_costume.bMaxLevelBySet[bAttributeSetCostume];
			if (max_costume > 0)
			{
				TSwitchbottAttributeTable tableCostume = {};
				tableCostume.attribute_set = bAttributeSetCostume;
				tableCostume.apply_num = iApplyCostumeNum;
				tableCostume.max_value = r_costume.lValues[max_costume-1];

				buf.write(&tableCostume, sizeof(tableCostume));
			}
		}
	}
#endif

#ifdef ENABLE_PENDANT
	for (int iApplyPendantNum = 0; iApplyPendantNum < MAX_APPLY_NUM; ++iApplyPendantNum)
	{
		const TItemAttrTable& r_pendant = g_map_itemAttrPendant[iApplyPendantNum];
		BYTE max_pendant = r_pendant.bMaxLevelBySet[ATTRIBUTE_SET_PENDANT];
		if (max_pendant > 0)
		{
			TSwitchbottAttributeTable tablePendant = {};
			tablePendant.attribute_set = ATTRIBUTE_SET_PENDANT;
			tablePendant.apply_num = iApplyPendantNum;
			tablePendant.max_value = r_pendant.lValues[max_pendant-1];

			buf.write(&tablePendant, sizeof(tablePendant));
		}
	}
#endif

	if (buf.size())
	{
		pack.size += buf.size();
		desc->BufferedPacket(&pack, sizeof(pack));
		desc->Packet(buf.read_peek(), buf.size());
	}
	else
	{
		desc->Packet(&pack, sizeof(pack));
	}
}

void CSwitchbotManager::SendSwitchbotUpdate(DWORD player_id)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
	{
		return;
	}

	LPCHARACTER ch = CHARACTER_MANAGER::Instance().FindByPID(player_id);
	if (!ch)
	{
		return;
	}

	LPDESC desc = ch->GetDesc();
	if (!desc)
	{
		return;
	}

	TSwitchbotTable table = pkSwitchbot->GetTable();

	TPacketGCSwitchbot pack;
	pack.header = HEADER_GC_SWITCHBOT;
	pack.subheader = SUBHEADER_GC_SWITCHBOT_UPDATE;
	pack.size = sizeof(TPacketGCSwitchbot) + sizeof(TSwitchbotTable);

	desc->BufferedPacket(&pack, sizeof(pack));
	desc->Packet(&table, sizeof(table));
}

void CSwitchbotManager::EnterGame(LPCHARACTER ch)
{
	SendItemAttributeInformations(ch);
	SetIsWarping(ch->GetPlayerID(), false);
	SendSwitchbotUpdate(ch->GetPlayerID());
	
	CSwitchbot* pkSwitchbot = FindSwitchbot(ch->GetPlayerID());
	if (pkSwitchbot && pkSwitchbot->HasActiveSlots() && !pkSwitchbot->IsSwitching())
	{
		pkSwitchbot->Start();
	}
}

void CSwitchbotManager::UpdatePlayerBotSpeed(DWORD player_id)
{
	CSwitchbot* pkSwitchbot = FindSwitchbot(player_id);
	if (!pkSwitchbot)
		return;

	LPCHARACTER ch = CHARACTER_MANAGER::Instance().FindByPID(player_id);
	if (!ch)
		return;

	ch->ChatPacket(CHAT_TYPE_COMMAND, "BINARY_SwitchBotSpeedReload %d", pkSwitchbot->GetBotSpeed());
}


#endif
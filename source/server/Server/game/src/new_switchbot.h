#pragma once

#ifdef ENABLE_SWITCHBOT
#include "../../common/tables.h"

class SwitchbotHelper
{
public:
	static bool IsValidItem(LPITEM pkItem);
};

class CSwitchbot
{
public:
	CSwitchbot();
	~CSwitchbot();

	void SetTable(TSwitchbotTable table);
	TSwitchbotTable GetTable();

	void SetPlayerId(DWORD player_id);
	DWORD GetPlayerId(DWORD player_id);
	
	void SetBotSpeed(BYTE bBotSpeed) { b_BotSpeed = bBotSpeed; }
	BYTE GetBotSpeed() const { return b_BotSpeed; }
	float GetRealBotSpeed(); //Dá os segundos do evento de rodar baseado na opcao
	bool CanChangeBotSpeed(BYTE bNewSpeed); //Usado para verificar se pode ou não mudar a velocidade do bot
	
	bool CanContinueSwitch(LPCHARACTER ch);
	void RegisterItem(WORD wCell, DWORD item_id);
	void UnregisterItem(WORD wCell);
	void SetAttributes(BYTE slot, std::vector<TSwitchbotAttributeAlternativeTable> vec_alternatives);
	
	void SetActive(BYTE slot, bool active);
	bool IsActive(BYTE slot);
	bool HasActiveSlots();
	bool IsSwitching();
	bool IsWarping();
	void SetIsWarping(bool warping);

	void Start();
	void Stop();
	void Pause();

	void SwitchItems();
	bool CheckItem(LPITEM pkItem, BYTE slot);

	void SendItemUpdate(LPCHARACTER ch, BYTE slot, LPITEM item);

protected:
	TSwitchbotTable m_table;
	LPEVENT m_pkSwitchEvent;
	bool m_isWarping;
	BYTE b_BotSpeed;
};

class CSwitchbotManager : public singleton<CSwitchbotManager>
{
public:
	CSwitchbotManager();
	virtual ~CSwitchbotManager();

	void Initialize();
	void RegisterItem(DWORD player_id, DWORD item_id, WORD wCell);
	void UnregisterItem(DWORD player_id, WORD wCell);
	void Start(DWORD player_id, BYTE slot, BYTE bBotSpeed, std::vector<TSwitchbotAttributeAlternativeTable> vec_alternatives);
	void Stop(DWORD player_id, BYTE slot);

	bool IsActive(DWORD player_id, BYTE slot);
	bool IsWarping(DWORD player_id);
	void SetIsWarping(DWORD player_id, bool warping);

	bool CanFindSwitchbot(DWORD player_id);
	CSwitchbot* FindSwitchbot(DWORD player_id);

	void P2PSendSwitchbot(DWORD player_id, WORD wTargetPort);
	void P2PReceiveSwitchbot(TSwitchbotTable table);

	void SendItemAttributeInformations(LPCHARACTER ch);
	void SendSwitchbotUpdate(DWORD player_id);

	void EnterGame(LPCHARACTER ch);
	
	void UpdatePlayerBotSpeed(DWORD player_id);

protected:
	std::map<DWORD, CSwitchbot*> m_map_Switchbots;
};
#endif
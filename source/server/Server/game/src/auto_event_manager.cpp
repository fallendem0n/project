#include "stdafx.h"
#include "config.h"
#include "auto_event_manager.h"
#include "questmanager.h"
#include "char.h"
#ifdef ENABLE_RONARK_SYSTEM
#include "lwt_ronark.h"
#endif
#ifdef ENABLE_BOSS_HASAR_SIRALAMA
#include "lwt_bosshasarsiralama.h"
#endif
static LPEVENT running_event = NULL;

EVENTINFO(EventsManagerInfoData)
{
	CAutoEventSystem* pEvents;

	EventsManagerInfoData()
		: pEvents(0)
	{
	}
};

EVENTFUNC(automatic_event_timer)
{
	if (event == NULL)
		return 0;

	if (event->info == NULL)
		return 0;

	EventsManagerInfoData * info = dynamic_cast<EventsManagerInfoData*>(event->info);

	if (info == NULL)
		return 0;

	CAutoEventSystem * pInstance = info->pEvents;

	if (pInstance == NULL)
		return 0;

	CAutoEventSystem::instance().PrepareChecker();
	return PASSES_PER_SEC(1);
}

void CAutoEventSystem::PrepareChecker()
{
	time_t cur_Time = time(NULL);
	struct tm vKey = *localtime(&cur_Time);

	int day = vKey.tm_wday;
	int hour = vKey.tm_hour;
	int minute = vKey.tm_min;
	int second = vKey.tm_sec;
	// CAutoNotice::instance().Check(day, hour, minute, second);
	CAutoEventSystem::instance().Check(day, hour, minute, second);
#ifdef ENABLE_BOSS_HASAR_SIRALAMA
	CBossHasarSiralama::instance().CheckBoss(hour, minute, second);
#endif
}

void CAutoEventSystem::Check(int day, int hour, int minute, int second)
{
#ifdef ENABLE_RONARK_SYSTEM
	if (quest::CQuestManager::instance().GetEventFlag("ronark_event") == 1)
	{
		if (hour >= 0 && quest::CQuestManager::instance().GetEventFlag("ronark_aktif") == 0)
		{
			quest::CQuestManager::instance().RequestSetEventFlag("ronark_aktif", 1);
			if (CRonarkSystem::instance().GetRonarkStatus() == 0)
			{
				CRonarkSystem::instance().RonarkHazirlikBaslat(1); // orta siklet
			}
		}

		// if (hour == 23 && quest::CQuestManager::instance().GetEventFlag("ronark_aktif") == 1)
		// {
			// CRonarkSystem::instance().RonarkVerileriTemizle();// veriler temizlendi
			// quest::CQuestManager::instance().RequestSetEventFlag("ronark_aktif", 0); // arena kapatildi
		// }
	}
#endif

}

bool CAutoEventSystem::Initialize()
{
	if (running_event != NULL)
	{
		event_cancel(&running_event);
		running_event = NULL;
	}

	EventsManagerInfoData* info = AllocEventInfo<EventsManagerInfoData>();
	info->pEvents = this;

	running_event = event_create(automatic_event_timer, info, PASSES_PER_SEC(30));
	return true;
}



void CAutoEventSystem::Destroy()
{
	if (running_event != NULL)
	{
		event_cancel(&running_event);
		running_event = NULL;
	}
}
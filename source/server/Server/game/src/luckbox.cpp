#include "stdafx.h"
#include "luckbox.h"
#include "char.h"
#include "db.h"
#include "utils.h"
#include "config.h"
#include "desc_client.h"
#include "desc_manager.h"
#include "item.h"
#include "item_manager.h"

CLuckBox::CLuckBox()
{
	Initialize();
}

CLuckBox::~CLuckBox()
{
	m_map_pkLuckBoxInfo.clear();
}

CLuckBox::SLuckBox::SLuckBox()
{

}


void CLuckBox::SetReward(LPITEM item)
{
	
	if (item)
	{
		int luck = number(1,m_map_pkLuckBoxInfo.size());
		int i = 1;
		
		TLuckBox *info = NULL;
		TLuckBoxMap::iterator iter;

		for (iter=m_map_pkLuckBoxInfo.begin(); iter!=m_map_pkLuckBoxInfo.end(); ++iter)
		{
			info = *iter;
			if (i == luck)
			{
				item->SetSocket(1,info->vnum);
				item->SetSocket(2,info->count);
			}
			i++;
		}
		
		
	}

}


void CLuckBox::Initialize()
{
	
	TLuckBox *info = NULL;
	TLuckBoxMap::iterator iter;
	for (iter=m_map_pkLuckBoxInfo.begin(); iter!=m_map_pkLuckBoxInfo.end(); ++iter)
	{
		info = *iter;
		M2_DELETE(info);
	}
	m_map_pkLuckBoxInfo.clear();
	

	std::auto_ptr<SQLMsg> pMsg(DBManager::instance().DirectQuery(
			"select vnum,count from player.luckbox"));

	if (pMsg->Get()->uiNumRows == 0)
	{
		sys_err("sql query null");
		return;
	}

	MYSQL_ROW row;


	while (NULL != (row = mysql_fetch_row(pMsg->Get()->pSQLResult)))
	{
		
		info = M2_NEW TLuckBox;
		memset(info, 0x00, sizeof(TLuckBox));
		
		str_to_number(info->vnum, row[0]);
		str_to_number(info->count, row[1]);

		m_map_pkLuckBoxInfo.push_back(info);

	}
}

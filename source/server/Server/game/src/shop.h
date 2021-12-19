#ifndef __INC_METIN_II_GAME_SHOP_H__
#define __INC_METIN_II_GAME_SHOP_H__
#include "../../common/CommonDefines.h"

enum
{
	SHOP_MAX_DISTANCE = 1000
};

class CGrid;

/* ---------------------------------------------------------------------------------- */
class CShop
{
	public:
		typedef struct shop_item
		{
			DWORD	vnum;		// ¾ÆÀÌÅÛ ¹øÈ£
			#ifdef FULL_YANG
			long	long	price;		// ¡Æ¢§¡ÆY
			#else
			DWORD	price;		// ¡Æ¢§¡ÆY
			#endif
#ifdef ENABLE_CHEQUE_SYSTEM
			int		cheque;
#endif
#ifdef PRICE_TYPE
			long	price_type;	
#endif
#ifdef SHOP_STOK			
			long	stok;	
#endif	

			BYTE	count;		// ¾ÆÀÌÅÛ °³¼ö

			LPITEM	pkItem;
			int		itemid;		// ¾ÆÀÌÅÛ °íÀ¯¾ÆÀÌµğ
			shop_item()
			{
				vnum = 0;
				price = 0;
#ifdef ENABLE_CHEQUE_SYSTEM
				cheque = 0;
#endif
#ifdef PRICE_TYPE
				price_type = 0;
#endif
#ifdef SHOP_STOK
				stok = 999;
#endif
				count = 0;
				itemid = 0;
				pkItem = NULL;
			}
		} SHOP_ITEM;

		CShop();
		virtual ~CShop(); // @fixme139 (+virtual)

		bool	Create(DWORD dwVnum, DWORD dwNPCVnum, TShopItemTable * pItemTable);
		void	SetShopItems(TShopItemTable * pItemTable, BYTE bItemCount);

		virtual void	SetPCShop(LPCHARACTER ch);
		virtual bool	IsPCShop()	{ return m_pkPC ? true : false; }

		virtual bool	AddGuest(LPCHARACTER ch,DWORD owner_vid, bool bOtherEmpire);
		void	RemoveGuest(LPCHARACTER ch);

#ifdef RELOAD_SHOP
		void	RemoveAllGuests();
#endif
		
		virtual int	Buy(LPCHARACTER ch, BYTE pos);

		
		void	BroadcastUpdateItem(BYTE pos);

		
		int		GetNumberByVnum(DWORD dwVnum);

		
		virtual bool	IsSellingItem(DWORD itemID);
#if defined(SHOP_SEARCH)
		bool SearchItem(DWORD vnum,long long price,DWORD book);
#endif

		DWORD	GetVnum() { return m_dwVnum; }
		DWORD	GetNPCVnum() { return m_dwNPCVnum; }

	protected:
		void	Broadcast(const void * data, int bytes);

	protected:
		DWORD				m_dwVnum;
		DWORD				m_dwNPCVnum;

		CGrid *				m_pGrid;
#ifdef OFFLINE_SHOP
	public:
		int		GetItemCount();
		bool	GetItems();
		void	SetLocked(bool val) { m_bLocked = val; }
		bool	IsLocked() { return m_bLocked; }
		void	RemoveGuests(LPCHARACTER except=NULL);
		void	ClearItems();
		void	SetPrivShopItems(std::vector<TShopItemTable *> map_shop);
		LPCHARACTER GetPC() { return m_pkPC; }
	protected:
		bool					m_bLocked;
#endif
		typedef TR1_NS::unordered_map<LPCHARACTER, bool> GuestMapType;
		GuestMapType m_map_guest;
		std::vector<SHOP_ITEM>		m_itemVector;	

		LPCHARACTER			m_pkPC;
};

#endif

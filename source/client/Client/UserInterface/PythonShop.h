#pragma once

#include "Packet.h"
#include "Locale_inc.h"

/*
 *	상점 처리
 *
 *	2003-01-16 anoa	일차 완료
 *	2003-12-26 levites 수정
 *
 *	2012-10-29 rtsummit 새로운 화폐 출현 및 tab 기능 추가로 인한 shop 확장.
 *
 */
typedef enum
{
	SHOP_COIN_TYPE_GOLD, // DEFAULT VALUE
	SHOP_COIN_TYPE_SECONDARY_COIN,
} EShopCoinType;

class CPythonShop : public CSingleton<CPythonShop>
{
	public:
		CPythonShop(void);
		virtual ~CPythonShop(void);

		void Clear();

		void SetItemData(DWORD dwIndex, const TShopItemData & c_rShopItemData);
		BOOL GetItemData(DWORD dwIndex, const TShopItemData ** c_ppItemData);

		void SetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData & c_rShopItemData);
		BOOL GetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData ** c_ppItemData);

		void SetTabCount(BYTE bTabCount) { m_bTabCount = bTabCount; }
		BYTE GetTabCount() { return m_bTabCount; }

		void SetTabCoinType(BYTE tabIdx, BYTE coinType);
		BYTE GetTabCoinType(BYTE tabIdx);

		void SetTabName(BYTE tabIdx, const char* name);
		const char* GetTabName(BYTE tabIdx);


		//BOOL GetSlotItemID(DWORD dwSlotPos, DWORD* pdwItemID);

		void Open(BOOL isPrivateShop, BOOL isMainPrivateShop);
		void Close();
		BOOL IsOpen();
		BOOL IsPrivateShop();
		BOOL IsMainPlayerPrivateShop();

		void ClearPrivateShopStock();
		//void AddPrivateShopItemStock(TItemPos ItemPos, BYTE byDisplayPos, DWORD dwPrice);
		void DelPrivateShopItemStock(TItemPos ItemPos);
		//int GetPrivateShopItemPrice(TItemPos ItemPos);
#ifndef ENABLE_OFFLINE_SHOP
		void BuildPrivateShop(const char * c_szName);
#else
		void BuildPrivateShop(const char * c_szName, DWORD days);
#endif
#ifdef PRICE_TYPE
		int GetPrivateShopItemPriceType(TItemPos ItemPos);
#endif
#ifdef SHOP_STOK
		int GetPrivateShopItemStok(TItemPos ItemPos);
#endif

#ifdef ENABLE_FULL_YANG
	#ifdef ENABLE_CHEQUE_SYSTEM
		#ifdef PRICE_TYPE
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwCheque, DWORD dwPriceType, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwCheque, DWORD dwPriceType);
			#endif
		#else
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, int dwPrice, DWORD dwCheque, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, int dwPrice, DWORD dwCheque);
			#endif
		#endif
	#else
		#ifdef PRICE_TYPE
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwPriceType, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwPriceType);
			#endif
		#else
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice);
			#endif
		#endif
	#endif
#else
	#ifdef ENABLE_CHEQUE_SYSTEM
		#ifdef PRICE_TYPE
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque, DWORD dwPriceType, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque, DWORD dwPriceType);
			#endif
		#else
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque);
			#endif
		#endif
	#else
		#ifdef PRICE_TYPE
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwPriceType, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwPriceType);
			#endif
		#else
			#ifdef SHOP_STOK
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwStok);
			#else
				void AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice);
			#endif
		#endif
	#endif
#endif

#ifdef ENABLE_FULL_YANG
	long long GetPrivateShopItemPrice(TItemPos ItemPos);
#else
	int GetPrivateShopItemPrice(TItemPos ItemPos);
#endif


#ifdef ENABLE_CHEQUE_SYSTEM
		int GetPrivateShopItemCheque(TItemPos ItemPos);
#endif

	protected:
		BOOL	CheckSlotIndex(DWORD dwIndex);

	protected:
		BOOL				m_isShoping;
		BOOL				m_isPrivateShop;
		BOOL				m_isMainPlayerPrivateShop;

		struct ShopTab
		{
			ShopTab()
			{
				coinType = SHOP_COIN_TYPE_GOLD;
			}
			BYTE				coinType;
			std::string			name;
			TShopItemData		items[SHOP_HOST_ITEM_MAX_NUM];
		};

		BYTE m_bTabCount;
		ShopTab m_aShoptabs[SHOP_TAB_COUNT_MAX];

		typedef std::map<TItemPos, TShopItemTable> TPrivateShopItemStock;
		TPrivateShopItemStock	m_PrivateShopItemStock;
};

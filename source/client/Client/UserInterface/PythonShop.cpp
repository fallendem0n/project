#include "stdafx.h"
#include "PythonShop.h"

#include "PythonNetworkStream.h"
#include "Locale_inc.h"

//BOOL CPythonShop::GetSlotItemID(DWORD dwSlotPos, DWORD* pdwItemID)
//{
//	if (!CheckSlotIndex(dwSlotPos))
//		return FALSE;
//	const TShopItemData * itemData;
//	if (!GetItemData(dwSlotPos, &itemData))
//		return FALSE;
//	*pdwItemID=itemData->vnum;
//	return TRUE;
//}
void CPythonShop::SetTabCoinType(BYTE tabIdx, BYTE coinType)
{
	if (tabIdx >= m_bTabCount)
	{
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
		return;
	}
	m_aShoptabs[tabIdx].coinType = coinType;
}

BYTE CPythonShop::GetTabCoinType(BYTE tabIdx)
{
	if (tabIdx >= m_bTabCount)
	{
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
		return 0xff;
	}
	return m_aShoptabs[tabIdx].coinType;
}

void CPythonShop::SetTabName(BYTE tabIdx, const char* name)
{
	if (tabIdx >= m_bTabCount)
	{
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
		return;
	}
	m_aShoptabs[tabIdx].name = name;
}

const char* CPythonShop::GetTabName(BYTE tabIdx)
{
	if (tabIdx >= m_bTabCount)
	{
		TraceError("Out of Index. tabIdx(%d) must be less than %d.", tabIdx, SHOP_TAB_COUNT_MAX);
		return NULL;
	}

	return m_aShoptabs[tabIdx].name.c_str();
}

void CPythonShop::SetItemData(DWORD dwIndex, const TShopItemData & c_rShopItemData)
{
	BYTE tabIdx = dwIndex / SHOP_HOST_ITEM_MAX_NUM;
	DWORD dwSlotPos = dwIndex % SHOP_HOST_ITEM_MAX_NUM;

	SetItemData(tabIdx, dwSlotPos, c_rShopItemData);
}

BOOL CPythonShop::GetItemData(DWORD dwIndex, const TShopItemData ** c_ppItemData)
{
	BYTE tabIdx = dwIndex / SHOP_HOST_ITEM_MAX_NUM;
	DWORD dwSlotPos = dwIndex % SHOP_HOST_ITEM_MAX_NUM;

	return GetItemData(tabIdx, dwSlotPos, c_ppItemData);
}

void CPythonShop::SetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData & c_rShopItemData)
{
	if (tabIdx >= SHOP_TAB_COUNT_MAX || dwSlotPos >= SHOP_HOST_ITEM_MAX_NUM)
	{
		TraceError("Out of Index. tabIdx(%d) must be less than %d. dwSlotPos(%d) must be less than %d", tabIdx, SHOP_TAB_COUNT_MAX, dwSlotPos, SHOP_HOST_ITEM_MAX_NUM);
		return;
	}

	m_aShoptabs[tabIdx].items[dwSlotPos] = c_rShopItemData;
}

BOOL CPythonShop::GetItemData(BYTE tabIdx, DWORD dwSlotPos, const TShopItemData ** c_ppItemData)
{
	if (tabIdx >= SHOP_TAB_COUNT_MAX || dwSlotPos >= SHOP_HOST_ITEM_MAX_NUM)
	{
		TraceError("Out of Index. tabIdx(%d) must be less than %d. dwSlotPos(%d) must be less than %d", tabIdx, SHOP_TAB_COUNT_MAX, dwSlotPos, SHOP_HOST_ITEM_MAX_NUM);
		return FALSE;
	}

	*c_ppItemData = &m_aShoptabs[tabIdx].items[dwSlotPos];

	return TRUE;
}
//
//BOOL CPythonShop::CheckSlotIndex(DWORD dwSlotPos)
//{
//	if (dwSlotPos >= SHOP_HOST_ITEM_MAX_NUM * SHOP_TAB_COUNT_MAX)
//		return FALSE;
//
//	return TRUE;
//}

void CPythonShop::ClearPrivateShopStock()
{
	m_PrivateShopItemStock.clear();
}
#ifdef ENABLE_FULL_YANG
	#ifdef ENABLE_CHEQUE_SYSTEM
			#ifdef PRICE_TYPE
				#ifdef SHOP_STOK
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwCheque, DWORD dwPriceType, DWORD dwStok)
				#else
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwCheque, DWORD dwPriceType)
				#endif
			#else
				#ifdef SHOP_STOK
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, int dwPrice, DWORD dwCheque, DWORD dwStok)
				#else
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, int dwPrice, DWORD dwCheque)
				#endif
			#endif
		// void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwCheque)
	#else
		#ifdef PRICE_TYPE
				#ifdef SHOP_STOK
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwPriceType, DWORD dwStok)
				#else
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwPriceType)
				#endif
			#else
				#ifdef SHOP_STOK
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice, DWORD dwStok)
				#else
					void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice)
				#endif
			#endif
		// void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, long long dwPrice)
	#endif
#else
	#ifdef ENABLE_CHEQUE_SYSTEM
		#ifdef PRICE_TYPE
			#ifdef SHOP_STOK
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque, DWORD dwPriceType, DWORD dwStok)
			#else
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque, DWORD dwPriceType)
			#endif
		#else
			#ifdef SHOP_STOK
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque, DWORD dwStok)
			#else
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque)
			#endif
		#endif
		// void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwCheque)
	#else
	
		#ifdef PRICE_TYPE
			#ifdef SHOP_STOK
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwPriceType, DWORD dwStok)
			#else
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwPriceType)
			#endif
		#else
			#ifdef SHOP_STOK
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice, DWORD dwStok)
			#else
				void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice)
			#endif
		#endif
		// void CPythonShop::AddPrivateShopItemStock(TItemPos ItemPos, BYTE dwDisplayPos, DWORD dwPrice)
	#endif
#endif
{
	DelPrivateShopItemStock(ItemPos);

	TShopItemTable SellingItem;
	SellingItem.vnum = 0;
	SellingItem.count = 0;
	SellingItem.pos = ItemPos;
	SellingItem.price = dwPrice;
#ifdef ENABLE_CHEQUE_SYSTEM
	SellingItem.cheque = dwCheque;
#endif
#ifdef PRICE_TYPE
	SellingItem.price_type = dwPriceType;
#endif
#ifdef SHOP_STOK
	SellingItem.stok = dwStok;
#endif
	SellingItem.display_pos = dwDisplayPos;
	m_PrivateShopItemStock.insert(make_pair(ItemPos, SellingItem));
}
void CPythonShop::DelPrivateShopItemStock(TItemPos ItemPos)
{
	if (m_PrivateShopItemStock.end() == m_PrivateShopItemStock.find(ItemPos))
		return;

	m_PrivateShopItemStock.erase(ItemPos);
}


#ifdef PRICE_TYPE
int CPythonShop::GetPrivateShopItemPriceType(TItemPos ItemPos)
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price_type;
}
#endif
#ifdef SHOP_STOK
int CPythonShop::GetPrivateShopItemStok(TItemPos ItemPos)
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.stok;
}
#endif

#ifdef ENABLE_FULL_YANG
long long CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
#else
int CPythonShop::GetPrivateShopItemPrice(TItemPos ItemPos)
#endif
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.price;
}
#ifdef ENABLE_CHEQUE_SYSTEM
int CPythonShop::GetPrivateShopItemCheque(TItemPos ItemPos)
{
	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.find(ItemPos);

	if (m_PrivateShopItemStock.end() == itor)
		return 0;

	TShopItemTable & rShopItemTable = itor->second;
	return rShopItemTable.cheque;
}
#endif
struct ItemStockSortFunc
{
	bool operator() (TShopItemTable & rkLeft, TShopItemTable & rkRight)
	{
		return rkLeft.display_pos < rkRight.display_pos;
	}
};
#ifdef ENABLE_OFFLINE_SHOP
void CPythonShop::BuildPrivateShop(const char * c_szName,DWORD days)
#else
void CPythonShop::BuildPrivateShop(const char * c_szName)
#endif
{
	std::vector<TShopItemTable> ItemStock;
	ItemStock.reserve(m_PrivateShopItemStock.size());

	TPrivateShopItemStock::iterator itor = m_PrivateShopItemStock.begin();
	for (; itor != m_PrivateShopItemStock.end(); ++itor)
	{
		ItemStock.push_back(itor->second);
	}

	std::sort(ItemStock.begin(), ItemStock.end(), ItemStockSortFunc());
	#ifdef ENABLE_OFFLINE_SHOP
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock,days);
	#else
	CPythonNetworkStream::Instance().SendBuildPrivateShopPacket(c_szName, ItemStock);
	#endif
}

void CPythonShop::Open(BOOL isPrivateShop, BOOL isMainPrivateShop)
{
	m_isShoping = TRUE;
	m_isPrivateShop = isPrivateShop;
	m_isMainPlayerPrivateShop = isMainPrivateShop;
}

void CPythonShop::Close()
{
	m_isShoping = FALSE;
	m_isPrivateShop = FALSE;
	m_isMainPlayerPrivateShop = FALSE;
}

BOOL CPythonShop::IsOpen()
{
	return m_isShoping;
}

BOOL CPythonShop::IsPrivateShop()
{
	return m_isPrivateShop;
}

BOOL CPythonShop::IsMainPlayerPrivateShop()
{
	return m_isMainPlayerPrivateShop;
}

void CPythonShop::Clear()
{
	m_isShoping = FALSE;
	m_isPrivateShop = FALSE;
	m_isMainPlayerPrivateShop = FALSE;
	ClearPrivateShopStock();
	m_bTabCount = 1;

	for (int i = 0; i < SHOP_TAB_COUNT_MAX; i++)
	{
		// @fixme016 BEGIN
		m_aShoptabs[i].coinType = SHOP_COIN_TYPE_GOLD;
		m_aShoptabs[i].name = "";
		// @fixme016 END
		memset (m_aShoptabs[i].items, 0, sizeof(TShopItemData) * SHOP_HOST_ITEM_MAX_NUM);
	}
}

CPythonShop::CPythonShop(void)
{
	Clear();
}

CPythonShop::~CPythonShop(void)
{
}

PyObject * shopOpen(PyObject * poSelf, PyObject * poArgs)
{
	int isPrivateShop = false;
	PyTuple_GetInteger(poArgs, 0, &isPrivateShop);
	int isMainPrivateShop = false;
	PyTuple_GetInteger(poArgs, 1, &isMainPrivateShop);

	CPythonShop& rkShop=CPythonShop::Instance();
	rkShop.Open(isPrivateShop, isMainPrivateShop);
	return Py_BuildNone();
}

PyObject * shopClose(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	rkShop.Close();
	return Py_BuildNone();
}

PyObject * shopIsOpen(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsOpen());
}

PyObject * shopIsPrviateShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsPrivateShop());
}

PyObject * shopIsMainPlayerPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop& rkShop=CPythonShop::Instance();
	return Py_BuildValue("i", rkShop.IsMainPlayerPrivateShop());
}

PyObject * shopGetItemID(PyObject * poSelf, PyObject * poArgs)
{
	int nPos;
	if (!PyTuple_GetInteger(poArgs, 0, &nPos))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(nPos, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->vnum);

	return Py_BuildValue("i", 0);
}

PyObject * shopGetItemCount(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->count);

	return Py_BuildValue("i", 0);
}

#ifdef PRICE_TYPE
PyObject * shopGetItemPriceType(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->price_type);

	return Py_BuildValue("i", 0);
}
#endif
#ifdef SHOP_STOK
PyObject * shopGetItemStok(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->stok);

	return Py_BuildValue("i", 0);
}
#endif


PyObject * shopGetItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
#ifdef ENABLE_FULL_YANG
		return Py_BuildValue("L", c_pItemData->price);
#else
		return Py_BuildValue("i", c_pItemData->price);
#endif

	return Py_BuildValue("i", 0);
}
#ifdef ENABLE_CHEQUE_SYSTEM
PyObject * shopGetItemCheque(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->cheque);

	return Py_BuildValue("i", 0);
}
#endif
PyObject * shopGetItemMetinSocket(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	int iMetinSocketIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iMetinSocketIndex))
		return Py_BuildException();

	const TShopItemData * c_pItemData;
	if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
		return Py_BuildValue("i", c_pItemData->alSockets[iMetinSocketIndex]);

	return Py_BuildValue("i", 0);
}

PyObject * shopGetItemAttribute(PyObject * poSelf, PyObject * poArgs)
{
	int iIndex;
	if (!PyTuple_GetInteger(poArgs, 0, &iIndex))
		return Py_BuildException();
	int iAttrSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &iAttrSlotIndex))
		return Py_BuildException();

	if (iAttrSlotIndex >= 0 && iAttrSlotIndex < ITEM_ATTRIBUTE_SLOT_MAX_NUM)
	{
		const TShopItemData * c_pItemData;
		if (CPythonShop::Instance().GetItemData(iIndex, &c_pItemData))
			return Py_BuildValue("ii", c_pItemData->aAttr[iAttrSlotIndex].bType, c_pItemData->aAttr[iAttrSlotIndex].sValue);
	}

	return Py_BuildValue("ii", 0, 0);
}

PyObject * shopClearPrivateShopStock(PyObject * poSelf, PyObject * poArgs)
{
	CPythonShop::Instance().ClearPrivateShopStock();
	return Py_BuildNone();
}
PyObject * shopAddPrivateShopItemStock(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
	int iDisplaySlotIndex;
	if (!PyTuple_GetInteger(poArgs, 2, &iDisplaySlotIndex))
		return Py_BuildException();

#ifdef ENABLE_FULL_YANG
	PyObject* val;
	if (!PyTuple_GetObject(poArgs, 3, &val))
		return Py_BuildException();
	long long iPrice = PyLong_AsLongLong(val);
#else
	int iPrice;
	if (!PyTuple_GetInteger(poArgs, 3, &iPrice))
		return Py_BuildException();
#endif

#ifdef ENABLE_CHEQUE_SYSTEM
	int iCheque;
	if (!PyTuple_GetInteger(poArgs, 4, &iCheque))
		return Py_BuildException();
#endif

#ifdef PRICE_TYPE
	int iPriceType;
	if (!PyTuple_GetInteger(poArgs, 5, &iPriceType))
		return Py_BuildException();
#endif

#ifdef SHOP_STOK
	int iStok;
	if (!PyTuple_GetInteger(poArgs, 6, &iStok))
		return Py_BuildException();
#endif


#ifdef ENABLE_CHEQUE_SYSTEM
	#ifdef PRICE_TYPE
		#ifdef SHOP_STOK
			CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice, iCheque,iPriceType, iStok);
		#else
			CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice, iCheque,iPriceType);
		#endif
	#else
		#ifdef SHOP_STOK
			CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice, iCheque, iStok);
		#else
			CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice, iCheque);
		#endif
	#endif
	// CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice, iCheque);
#else
	CPythonShop::Instance().AddPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex), iDisplaySlotIndex, iPrice);
#endif

	return Py_BuildNone();
}
PyObject * shopDelPrivateShopItemStock(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	CPythonShop::Instance().DelPrivateShopItemStock(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildNone();
}

#ifdef PRICE_TYPE
PyObject * shopGetPrivateShopItemPriceType(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemPriceType(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}
#endif
#ifdef SHOP_STOK
PyObject * shopGetPrivateShopItemStok(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemStok(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}
#endif

PyObject * shopGetPrivateShopItemPrice(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();
#ifdef ENABLE_FULL_YANG
	return Py_BuildValue("L", CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex)));
#else
	return Py_BuildValue("i", CPythonShop::Instance().GetPrivateShopItemPrice(TItemPos(bItemWindowType, wItemSlotIndex)));
#endif

	return Py_BuildValue("i", 0);
}
#ifdef ENABLE_CHEQUE_SYSTEM
PyObject * shopGetPrivateShopItemCheque(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bItemWindowType;
	if (!PyTuple_GetInteger(poArgs, 0, &bItemWindowType))
		return Py_BuildException();
	WORD wItemSlotIndex;
	if (!PyTuple_GetInteger(poArgs, 1, &wItemSlotIndex))
		return Py_BuildException();

	int iValue = CPythonShop::Instance().GetPrivateShopItemCheque(TItemPos(bItemWindowType, wItemSlotIndex));
	return Py_BuildValue("i", iValue);
}
#endif
PyObject * shopBuildPrivateShop(PyObject * poSelf, PyObject * poArgs)
{
	char * szName;
	if (!PyTuple_GetString(poArgs, 0, &szName))
		return Py_BuildException();
	#ifdef ENABLE_OFFLINE_SHOP
	int days;
	if (!PyTuple_GetInteger(poArgs, 1, &days))
		return Py_BuildException();
	CPythonShop::Instance().BuildPrivateShop(szName,days);
	#else
	CPythonShop::Instance().BuildPrivateShop(szName);
	#endif
	return Py_BuildNone();
}

PyObject * shopGetTabCount(PyObject * poSelf, PyObject * poArgs)
{
	return Py_BuildValue("i", CPythonShop::instance().GetTabCount());
}

PyObject * shopGetTabName(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bTabIdx;
	if (!PyTuple_GetInteger(poArgs, 0, &bTabIdx))
		return Py_BuildException();

	return Py_BuildValue("s", CPythonShop::instance().GetTabName(bTabIdx));
}

PyObject * shopGetTabCoinType(PyObject * poSelf, PyObject * poArgs)
{
	BYTE bTabIdx;
	if (!PyTuple_GetInteger(poArgs, 0, &bTabIdx))
		return Py_BuildException();

	return Py_BuildValue("i", CPythonShop::instance().GetTabCoinType(bTabIdx));
}

void initshop()
{
	static PyMethodDef s_methods[] =
	{
		// Shop
		{ "Open",						shopOpen,						METH_VARARGS },
		{ "Close",						shopClose,						METH_VARARGS },
		{ "IsOpen",						shopIsOpen,						METH_VARARGS },
		{ "IsPrivateShop",				shopIsPrviateShop,				METH_VARARGS },
		{ "IsMainPlayerPrivateShop",	shopIsMainPlayerPrivateShop,	METH_VARARGS },
		{ "GetItemID",					shopGetItemID,					METH_VARARGS },
		{ "GetItemCount",				shopGetItemCount,				METH_VARARGS },
#ifdef ENABLE_CHEQUE_SYSTEM
		{ "GetItemCheque",				shopGetItemCheque,				METH_VARARGS },
#endif

#ifdef PRICE_TYPE
		{ "GetItemPriceType",				shopGetItemPriceType,				METH_VARARGS },
		{ "GetPrivateShopItemPriceType",			shopGetPrivateShopItemPriceType,			METH_VARARGS },
#endif
#ifdef SHOP_STOK
		{ "GetItemStok", shopGetItemStok, METH_VARARGS },
		{ "GetPrivateShopItemStok", shopGetPrivateShopItemStok, METH_VARARGS },
#endif

		{ "GetItemPrice",				shopGetItemPrice,				METH_VARARGS },
		{ "GetItemMetinSocket",			shopGetItemMetinSocket,			METH_VARARGS },
		{ "GetItemAttribute",			shopGetItemAttribute,			METH_VARARGS },
		{ "GetTabCount",				shopGetTabCount,				METH_VARARGS },
		{ "GetTabName",					shopGetTabName,					METH_VARARGS },
		{ "GetTabCoinType",				shopGetTabCoinType,				METH_VARARGS },

		// Private Shop
		{ "ClearPrivateShopStock",		shopClearPrivateShopStock,		METH_VARARGS },
		{ "AddPrivateShopItemStock",	shopAddPrivateShopItemStock,	METH_VARARGS },
		{ "DelPrivateShopItemStock",	shopDelPrivateShopItemStock,	METH_VARARGS },
		{ "GetPrivateShopItemPrice",	shopGetPrivateShopItemPrice,	METH_VARARGS },
#ifdef ENABLE_CHEQUE_SYSTEM
		{ "GetPrivateShopItemCheque",	shopGetPrivateShopItemCheque,	METH_VARARGS },
#endif
		{ "BuildPrivateShop",			shopBuildPrivateShop,			METH_VARARGS },
		{ NULL,							NULL,							NULL },
	};
	PyObject * poModule = Py_InitModule("shop", s_methods);

	PyModule_AddIntConstant(poModule, "SHOP_SLOT_COUNT", SHOP_HOST_ITEM_MAX_NUM);
	PyModule_AddIntConstant(poModule, "SHOP_COIN_TYPE_GOLD", SHOP_COIN_TYPE_GOLD);
	PyModule_AddIntConstant(poModule, "SHOP_COIN_TYPE_SECONDARY_COIN", SHOP_COIN_TYPE_SECONDARY_COIN);
}
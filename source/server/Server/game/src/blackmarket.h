#ifndef __BLACKMARKET__
#define __BLACKMARKET__

class CBlackMarket : public singleton<CBlackMarket>
{
	public:
		typedef struct SBlackMarket
		{
			// Functions
			SBlackMarket();

			DWORD				dwVnum;
			unsigned long long	llPrice;
			unsigned long long	llWon;

		} TBlackMarket;

		typedef std::map<DWORD, TBlackMarket> TBlackMarketMap;

		CBlackMarket();
		virtual ~CBlackMarket();
		
		void	Initialize();
		bool	HaveLimit(LPCHARACTER ch, DWORD dwVnum);
		bool	GetPriceData(DWORD dwVnum, TBlackMarket ** pPriceData);
		bool	GetPrice(LPCHARACTER ch, DWORD dwVnum, short sCount, int iCheque, int iGold);
		int*		GetPriceInfo(LPCHARACTER ch, DWORD dwVnum, short sCount);
		int		GetWonPrice(LPCHARACTER ch, DWORD dwVnum);
		int		GetGoldPrice(LPCHARACTER ch, DWORD dwVnum);
		void		GetPriceList(LPCHARACTER ch);

	protected:
		TBlackMarketMap	m_map_pkBlackMarket;
};

#endif

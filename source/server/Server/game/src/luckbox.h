#ifndef __LUCK_BOX__H
#define __LUCK_BOX__H

class CLuckBox : public singleton<CLuckBox>
{
	public:
		typedef struct SLuckBox
		{
			SLuckBox();

			DWORD				vnum;
			DWORD				count;

		} TLuckBox;

		typedef std::vector<TLuckBox*> TLuckBoxMap;

		CLuckBox();
		virtual ~CLuckBox();
		
		void	Initialize();
		void	SetReward(LPITEM item);

	protected:
		TLuckBoxMap	m_map_pkLuckBoxInfo;
};

#endif

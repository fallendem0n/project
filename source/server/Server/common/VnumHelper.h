#ifndef __HEADER_VNUM_HELPER__
#define	__HEADER_VNUM_HELPER__

/**
	이미 존재하거나 앞으로 추가될 아이템, 몹 등을 소스에서 식별할 때 현재는 모두
	식별자(숫자=VNum)를 하드코딩하는 방식으로 되어있어서 가독성이 매우 떨어지는데

	앞으로는 소스만 봐도 어떤 아이템(혹은 몹)인지 알 수 있게 하자는 승철님의 제안으로 추가.

		* 이 파일은 변경이 잦을것으로 예상되는데 PCH에 넣으면 바뀔 때마다 전체 컴파일 해야하니
		일단은 필요한 cpp파일에서 include 해서 쓰도록 했음.

		* cpp에서 구현하면 컴파일 ~ 링크해야하니 그냥 common에 헤더만 넣었음. (game, db프로젝트 둘 다 사용 예정)

	@date	2011. 8. 29.
*/


class CItemVnumHelper
{
public:
	
	static	const bool	IsPhoenix(DWORD vnum)				{ return 53001 == vnum; }		

	
	static	const bool	IsRamadanMoonRing(DWORD vnum)		{ return 71135 == vnum; }

	
	static	const bool	IsHalloweenCandy(DWORD vnum)		{ return 71136 == vnum; }

	
	static	const bool	IsHappinessRing(DWORD vnum)		{ return 71143 == vnum; }

	
	static	const bool	IsLovePendant(DWORD vnum)		{ return 71145 == vnum; }
};

class CMobVnumHelper
{
public:
	
	static	bool	IsPhoenix(DWORD vnum)				{ return 34001 == vnum; }
	static	bool	IsIcePhoenix(DWORD vnum)				{ return 34003 == vnum; }
	
	static	bool	IsPetUsingPetSystem(DWORD vnum)	{ return (IsPhoenix(vnum) || IsReindeerYoung(vnum)) || IsIcePhoenix(vnum); }

	
	static	bool	IsReindeerYoung(DWORD vnum)	{ return 34002 == vnum; }

	
	static	bool	IsRamadanBlackHorse(DWORD vnum)		{ return 20119 == vnum || 20219 == vnum || 22022 == vnum; }
};

class CVnumHelper
{
};


#endif	//__HEADER_VNUM_HELPER__

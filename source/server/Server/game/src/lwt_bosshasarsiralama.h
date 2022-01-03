#pragma once
class BossHasarSiralamaInfo
{
private:
	DWORD	m_dwBossVID;
	unsigned long long	m_ullBossHP;

protected:
	BossHasarSiralamaInfo(DWORD dwID, DWORD dwMaxHP);
	~BossHasarSiralamaInfo() = default;

public:
	friend class CBossHasarSiralama;
	DWORD	GetBossVID() const { return m_dwBossVID; }
	void	SetBossVID(const DWORD dwVID) { m_dwBossVID = dwVID; }
	void	SetBossHP(const unsigned long long ullHP) { m_ullBossHP = ullHP; }
	unsigned long long	GetBossHP() const { return m_ullBossHP; }
};


class CBossHasarSiralama final : public singleton<CBossHasarSiralama>
{
	enum eSubPacket
	{
		GC_BRINFO_CLEAR = 1,
		GC_BRINFO_ADD = 2,
		GC_BRINFO_UPDATE = 3,
	};
	struct damageInfo
	{
		BYTE	bRace;
		const char* cName;
		BYTE	bLevel;
		BYTE	bEmpire;
		DWORD	dwDamage;
	};
public:
	enum eBossInfos
	{
		BOSS_VNUM = 0,
		POS_X = 1,
		POS_Y = 2,
		MAP_INDEX = 3,
		RESPAWN_TIME_H = 4,
		RESPAWN_TIME_M = 5,
		SECURITY = 6,
		IS_SPAWN = 7,
		BOSS_INFO_MAX_NUM,
	};
	void	CheckBoss(int hour, int min, int sec) const;
	bool	BossVnum(DWORD mVnum) const;
	void	RemoveVec(LPCHARACTER ch);
	void	ClearVec();
	void	SendClient(BYTE bSubHeader, const void* c_pvData, size_t iSize);
	void	VecActions(LPCHARACTER ch, DWORD damage);
	void	Initialize(DWORD dwNumber, DWORD dwMaxHP);
	void	BossAction(DWORD dwRaceNum);
	void	UpdateInfo(DWORD bossHP);
	void	Destroy();

	BossHasarSiralamaInfo* FindBossClass(DWORD dwID) const;

private:
	std::vector<BossHasarSiralamaInfo*> bossCont;
	std::vector<std::pair<LPCHARACTER, damageInfo> > BossRankVec;
};
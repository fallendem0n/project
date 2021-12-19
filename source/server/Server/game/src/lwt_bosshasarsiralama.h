#pragma once
class BossHasarSiralamaInfo
{
private:
	DWORD	m_ibossVID;
	int		m_ibossHP;

protected:
	BossHasarSiralamaInfo(DWORD dwID);
	void	Clear();

public:
	friend class CBossHasarSiralama;
	DWORD	GetBossVID() { return m_ibossVID; }
	void	SetBossVID(DWORD dwVID) { m_ibossVID = dwVID; }
	void	SetBossHP(int iHP) { m_ibossHP = iHP; }
	int		GetBossHP() { return m_ibossHP; }
	void	BasAmk(std::map<VID, CHARACTER::TBattleInfo>& rMP);
};


class CBossHasarSiralama : public singleton<CBossHasarSiralama>
{
public:
	void	CheckBoss(int hour, int min, int sec);
	bool	BossVnum(DWORD mVnum);
	void	ListeyeEkle(LPCHARACTER ch);
	void	ListeyiTemizle();
	void	Packet(const char* veri);
	void	Initialize();

	BossHasarSiralamaInfo*	FindBossClass(DWORD dwID);
private:
	std::vector<BossHasarSiralamaInfo*> bossCont;
	std::vector<LPCHARACTER> characterList;
};
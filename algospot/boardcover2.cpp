#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int boardh,boardw,blocksize,covered[10][10],best;
vector<string> board;
vector<vector<pair<int,int>>> rotations;

vector<string> rotate(const vector<string> &arr)
{
    vector<string> ret(arr[0].size(),string(arr.size(),' '));
    for(int i=0;i<arr.size();i++)
        for(int j=0;j<arr[0].size();j++)
            ret[j][arr.size()-i-1]=arr[i][j];
    return ret;
}

void generaterotations(vector<string> block)
{
    rotations.clear();
    rotations.resize(4);
    for(int rot=0;rot<4;rot++)
    {
        int originy=-1,originx=-1;
        for(int i=0;i<block.size();i++)
            for(int j=0;j<block[i].size();j++)
                if(block[i][j]=='#')
                    {
                        if (originy==-1)
                        {
                            originy=i;
                            originx=j;
                        }
                        rotations[rot].push_back(make_pair(i-originy,j-originx));
                    }
        block=rotate(block);
    }
    sort(rotations.begin(),rotations.end());
    rotations.erase(unique(rotations.begin(),rotations.end()),rotations.end());
    blocksize=rotations[0].size();
}

bool set(int y,int x,const vector<pair<int,int>> &block,int delta)
{
    bool ret=true;
    for(int i=0;i<block.size();i++)
    {
        if(y+block[i].first>=0&&y+block[i].first<boardh&&x+block[i].second>=0&&x+block[i].second<boardw)
        {
            covered[y+block[i].first][x+block[i].second]+=delta;
            ret=ret && (covered[y+block[i].first][x+block[i].second]==1);
        }
        else
            ret=false;
    }
    return ret;
}

int blockprune(int placed)
{
    int cnt=0;
    for(int i=0;i<boardh;i++)
        for(int j=0;j<boardw;j++)
            cnt+=!(covered[i][j])?1:0;
    return ((cnt/blocksize)+placed<=best);
}

void search(int placed)
{
    if(blockprune(placed))
        return;
    int y=-1,x=-1;
    for(int i=0;i<boardh;i++)
    {
        for(int j=0;j<boardw;j++)
        {
            if(covered[i][j]==0)
            {
                y=i;
                x=j;
                break;
            }
        }
        if(y!=-1)
            break;
    }
    if(y==-1)
    {
        best=max(best,placed);
            return;
    }
    for(int i=0;i<rotations.size();i++)
    {
        if(set(y,x,rotations[i],1))
            search(placed+1);
        set(y,x,rotations[i],-1);
    }
    covered[y][x]=1;
    search(placed);
    covered[y][x]=0;
}

int solve()
{
    best=0;
    for(int i=0;i<boardh;i++)
        for(int j=0;j<boardw;j++)
            covered[i][j]=(board[i][j]=='#'?1:0);
    search(0);
    return best;
}

int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        board.clear();
        vector<string> block;
        int blockh,blockw;
        cin>>boardh>>boardw>>blockh>>blockw;
        for(int i=0;i<boardh;i++)
        {
            string tmp;
            cin>>tmp;
            board.push_back(tmp);
        }
        for(int i=0;i<blockh;i++)
        {
            string tmp;
            cin>>tmp;            
            block.push_back(tmp);
        }
        generaterotations(block);
        cout<<solve()<<endl;
    }
    return 0;
}

#include<iostream>
#include<map>
#include<string>
#include<vector>

using namespace std;

typedef unsigned long long ull;
int idx[10][10];
int ilen;

char arr[10][11];
char block[4][10][11];
map<ull, int> mp[10][10];
int best = 0;
int h, w, r, c;
int len;
void rotate()
{
	for (int d = 1; d < 4; ++d)
	{
		for (int i = 0; i < len; ++i)
		{
			for (int j = 0; j < len; ++j)
			{
				block[d][j][len - i - 1] = block[d-1][i][j];
			}
		}
	}
	for (int d = 0; d < 4; ++d)
	{
		int si = 0, sj =0;
		for (; si < len; si++)
		{
			for (int j = 0; j < len; ++j)
			{
				if (block[d][si][j] == '#')
					goto ENDLOOP1;
			}
		}
		ENDLOOP1:
		for (int i = 0; i + si < len; ++i)
		{
			for (int j = 0; j < len; ++j)
			{
				block[d][i][j] = block[d][i + si][j];
			}
		}
		for (int i = len - si; i < len; ++i)
		{
			for (int j = 0; j < len; ++j)
				block[d][i][j] = '.';
		}

		si = 0;
		for (; si < len; si++)
		{
			for (int j = 0; j < len; ++j)
			{
				if (block[d][j][si] == '#')
					goto ENDLOOP2;
			}
		}
		ENDLOOP2:
		for (int j = 0; j + si < len; ++j)
		{
			for (int i = 0; i < len; ++i)
			{
				block[d][i][j] = block[d][i][j+si];
			}
		}
		for (int i = len - si; i < len; ++i)
		{
			for (int j = 0; j < len; ++j)
				block[d][j][i] = '.';
		}
	}
}

bool check(int r1, int c1, int b)
{
	for (int i = 0; i < len; ++i)
	{
		for (int j = 0; j < len; ++j)
		{
			if (block[b][i][j] == '.')
				continue;
			if ((r1 + i >= h || c1 + j >= w)|| arr[r1+i][c1+j] == '#')
				return false;
		}
	}
	return true;
}

void paint(int nr, int nc, int b, char c)
{
	for (int i = 0; i < len; ++i)
	{
		for (int j = 0; j < len; ++j)
		{
			if (block[b][i][j] == '#')
			{
				arr[i + nr][j + nc] = c;
			}
		}
	}
}
void getRes(int nr, int nc, int cnt)
{
	if (nr == h)
	{
		best = best > cnt ? best : cnt;
		return;
	}

	ull visit = 0;
	for (int i = 0; i < len; ++i)
	{
		if (i + nr == h)
			break;
		for (int j = 0; j < w; ++j)
		{
			if (arr[i + nr][j] == '.')
				visit += (1ULL << idx[i + nr][j]);
		}
	}
	if (mp[nr][nc].find(visit) != mp[nr][nc].end())
	{
			if (mp[nr][nc][visit] >= cnt)
				return;
	}
	mp[nr][nc][visit] = cnt;

	int nnr = nr, nnc = nc + 1;
	if (nnc == w)
	{
		++nnr;
		nnc = 0;
	}

	for (int b = 0; b < 4; ++b)
	{
		if (check(nr, nc, b))
		{
			paint(nr, nc, b, '#');
			getRes(nnr, nnc, cnt + 1);
			paint(nr, nc, b, '.');
		}
	}
	getRes(nnr, nnc, cnt);
}

int main()
{
	ios_base::sync_with_stdio(0), cout.tie(0), cin.tie(0);

	int cnt;
	cin >> cnt;

	while (cnt--)
	{
		cin >> h >> w >> r >> c;
		for (int i = 0; i < h; ++i)
			for(int j = 0; j < w; ++j)
				mp[i][j].clear();
		len = r < c ? c : r;
		best = 0;
		ilen = 0;

		for (int b = 0; b < 4; ++b)
		{
			for (int i = 0; i < r; ++i)
				for (int j = 0; j < c; ++j)
					block[b][i][j] = '.';
		}

		string temp;
		for (int i = 0; i < h; ++i)
			cin >> arr[i];
		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				if (arr[i][j] == '.')
				{
					idx[i][j] = ilen++;
				}
			}
		}
		for (int i = 0; i < r; ++i)
		{
			cin >> temp;
			for (int j = 0; j < temp.size(); ++j)
				block[0][i][j] = temp[j];
		}

		for (int i = 0; i < len; ++i)
		{
			for (int j = 0; j < len; ++j)
			{
				if (i >= r || j >= c)
					block[0][i][j] = '.';
			}
		}
		rotate();
		getRes(0, 0, 0);
		cout << best << '\n';
	}
	return 0;
}
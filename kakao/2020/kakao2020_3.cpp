#include <string>
#include <vector>

using namespace std;

int cnt,m,n;
vector<vector<int>> a,b;

void rotate()
{
	vector<vector<int>> tmp(m,vector<int>(m,0));
	for(int i=0;i<m;i++)
		for(int j=0;j<m;j++)
			tmp[j][m-i-1]=a[i][j];
	a=tmp;
}
bool solution(vector<vector<int>> key,vector<vector<int>> lock)
{
	a=key;
	b=lock;
	m=a.size();
	n=b.size();

	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(b[i][j]==0)
				cnt++;

	for(int r=0;r<4;r++)
	{
		for(int i=-20;i<=20;i++)
		{
			for(int j=-20;j<=20;j++)
			{
				int tmpcnt=0,miss=0;
				for(int y=0;y<m;y++)
				{
					for(int x=0;x<m;x++)
					{
						int ny=i+y,nx=j+x;
						if(0<=ny&&ny<n&&0<=nx&&nx<n)
						{
							if(b[ny][nx]==1&&a[y][x]==1)miss=1;
							else if(b[ny][nx]==0&&a[y][x]==1)tmpcnt++;
						}
					}
				}
				if(tmpcnt==cnt&&miss==0)return true;
			}
		}
		rotate();
	}
	return false;
}
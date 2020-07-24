#include <iostream>
#include <string>
#include <queue>
using namespace std;

int N,M;
int rx,ry,bx,by;
int hx,hy;
bool flag;
int ans=0;
char board[11][11];
bool visited[11][11][11][11];
queue<pair<int,int>> red;
queue<pair<int,int>> blue;

int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};

int main()
{
	string str;
	cin>>N>>M;
	for(int i=0;i<N;i++)
	{
		cin>>str;
		for(int j=0;j<M;j++)
		{
			board[i][j]=str[j];
			if(board[i][j]=='R'){red.push(make_pair(i,j));rx=i,ry=j;}
			if(board[i][j]=='B'){blue.push(make_pair(i,j));bx=i,by=j;}
			if(board[i][j]=='O')hx=i,hy=j;
		}
	}
	visited[rx][ry][bx][by]=true;
	while(!red.empty())
	{
		int qsize=red.size();
		while(qsize--)
		{
			rx=red.front().first;ry=red.front().second;
			bx=blue.front().first;by=blue.front().second;
			red.pop(),blue.pop();

			if(ans>10) break;
			if(rx==hx&&ry==hy){flag=true;break;}
			for(int i=0;i<4;i++)
			{
				int nrx=rx+dx[i],nry=ry+dy[i],nbx=bx+dx[i],nby=by+dy[i];
				while(1)
				{
					if(board[nrx][nry]=='#'){nrx-=dx[i];nry-=dy[i];break;}
					if(board[nrx][nry]=='O')break;
					nrx+=dx[i];nry+=dy[i];
				}
				while(1)
				{
					if(board[nbx][nby]=='#'){nbx-=dx[i];nby-=dy[i];break;}
					if(board[nbx][nby]=='O')break;
					nbx+=dx[i];nby+=dy[i];
				}
				if(nbx==hx&&nby==hy)continue;
				if(nrx==nbx&&nry==nby)
				{
					switch(i)
					{
						case 0: rx>bx? nrx++:nbx++; break;
						case 1: rx<bx? nrx--:nbx--; break;
						case 2: ry>by? nry++:nby++; break;
						case 3: ry<by? nry--:nby--; break;
					}
				}
				if(visited[nrx][nry][nbx][nby]) continue;
				red.push(make_pair(nrx,nry));
				blue.push(make_pair(nbx,nby));
				visited[nrx][nry][nbx][nby]=true;
			}
		}
		if(flag) break;
		else ans++;
	}
	ans=((flag)?ans:-1);
	cout<<ans;
}

#include <stdio.h>

#define F(A,B) for(ri=rI,rj=rJ,bi=bI,bj=bJ,mv=1;mv;)
{
	mv=0;
	if(!blocked(ri+A,rj+B,bi,bj))
	{
		ri+=A;rj+=B;mv++;
	}
	if(!blocked(bi+A,bj+B,ri,rj))
	{
		bi+=A;bj+=B;mv++;
	}
	if(ri>0&&s[ri][rj]=='O')
		ri=-1;
	if(bi>0&&s[bi][bj]=='O')
		bi=-1;
}
f(C+1,ri,rj,bi,bj);


char s[10][11];
int m = 11;

int blocked (int i, int j, int I, int J) 
{
	
	return i < 0 || s[i][j] == '#' || (i == I && j == J);
}

void f (int C, int rI, int rJ, int bI, int bJ)
{

	int ri, rj, bi, bj, mv;

	if (C >= m || rI < 0 || bI < 0)
	{
		
		if (rI < 0 && bI > 0 && m > C) m = C;
		return;
	}
	
	F(-1,0);
	F(1,0);
	F(0,-1);
	F(0,1);
}

int main (void) 
{

	int N, M, i, j, ri, rj, bi, bj;
	
	scanf ("%d %d", &N, &M);
	
	for (i = 0; i < N; i++) 
	{
		
		scanf ("%s", s[i]);
		for (j = 0; j < M; j++) 
		{
			
			if (s[i][j] == 'R') { ri = i; rj = j; s[i][j] = '.'; }
			if (s[i][j] == 'B') { bi = i, bj = j; s[i][j] = '.'; }
		}
	}
	
	f (0, ri, rj, bi, bj);
	
	printf ("%d\n", m > 10 ? -1 : m);
	
	return 0;
}

#include<cstdio>
int n, m;
int rx, ry, bx, by;
char a[11][11];
int ans = 11;
void go(int rx, int ry, int bx, int by, int mx, int my, int cnt)
{
	if (cnt >= ans) return;
	int rm = 0, bm = 0;
	if (mx != my){
		while (a[bx + mx][by + my] - '#')
		{
			bx += mx;
			by += my;
			bm++;
			if (!(a[bx][by] - 'O'))
				return;
		}
		while (a[rx + mx][ry + my] - '#')
		{
			rx += mx;
			ry += my;
			rm++;
			if (!(a[rx][ry] - 'O'))
			{
				ans = ans < cnt ? ans : cnt;
				return;
			}
		}
	}
	if (rx == bx && ry == by)
		if (rm < bm)
			bx -= mx, by -= my;
		else
			rx -= mx, ry -= my;
	if (mx == 0)
	{
		go(rx, ry, bx, by, 1, 0, cnt + 1);
		go(rx, ry, bx, by, -1, 0, cnt + 1);
	}
	if (my == 0)
	{
		go(rx, ry, bx, by, 0, 1, cnt + 1);
		go(rx, ry, bx, by, 0, -1, cnt + 1);
	}
}

int main()
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%s", a[i]);
	for (int i = 1; i < n - 1; i++)
	{
		for (int j = 1; j < m - 1; j++)
		{
			if (a[i][j] == 'R')
				rx = i, ry = j;
			if (a[i][j] == 'B')
				bx = i, by = j;
		}
	}
	go(rx, ry, bx, by, 0, 0, 0);
	printf("%d", ans < 11 ? ans : -1);
}
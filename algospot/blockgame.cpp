#include <iostream>
#include <vector>
#include <bitset>
#include <cstring>
using namespace std;

char cache[1<<25];
vector<int> moves;

inline int cell(int y,int x)
{
	return 1<<(y*5+x);
}

void precal()
{
	for(int y=0;y<4;y++)
		for(int x=0;x<4;x++)
		{
			vector<int> cells;
			for(int dy=0;dy<2;dy++)
				for(int dx=0;dx<2;dx++)
					cells.push_back(cell(y+dy,x+dx));
			int square=cells[0]+cells[1]+cells[2]+cells[3];
			for(int i=0;i<4;i++)
				moves.push_back(square-cells[i]);
		}
	for(int i=0;i<5;i++)
		for(int j=0;j<4;j++)
		{
			moves.push_back(cell(i,j)+cell(i,j+1));
			moves.push_back(cell(j,i)+cell(j+1,i));
		}
}

char play(int board)
{
	char& ret=cache[board];
	if(ret!=-1)
		return ret;
	ret=0;
	for(int i=0;i<moves.size();i++)
		if((moves[i]&board)==0)
			if(!play(board|moves[i]))
			{
				ret=1;
				break;
			}
	return ret;
}

int main()
{
	int c;
	cin>>c;
	precal();
	while(c--)
	{
		memset(cache,-1,sizeof(cache));
		int board=0;
		for(int i=0;i<5;i++)
			for(int j=0;j<5;j++)
			{
				char mark;
				cin>>mark;
				if(mark=='#')
					board+=cell(i,j);
			}
		printf("%s\n",play(board)?"WINNING":"LOSING");
	}
	return 0;
}

#include<cstdio>

int c;
char a[5][6];
char d[33554432];

int back(int s)
{
  int i,j;
  if(d[s])return d[s];
  for(i=0;i<5;i++)for(j=0;j<4;j++)if(!( s&(3<<(i*5+j)) ))
    if(back(s|(3<<(i*5+j)))==2)return d[s]=1;
  for(i=0;i<4;i++)for(j=0;j<5;j++)if(!( s&(33<<(i*5+j)) ))
    if(back(s|(33<<(i*5+j)))==2)return d[s]=1;
  for(i=0;i<4;i++)for(j=0;j<4;j++)if(!( s&(35<<(i*5+j)) ))
    if(back(s|(35<<(i*5+j)))==2)return d[s]=1;
  for(i=0;i<4;i++)for(j=0;j<4;j++)if(!( s&(67<<(i*5+j)) ))
    if(back(s|(67<<(i*5+j)))==2)return d[s]=1;
  for(i=0;i<4;i++)for(j=0;j<4;j++)if(!( s&(97<<(i*5+j)) ))
    if(back(s|(97<<(i*5+j)))==2)return d[s]=1;
  for(i=0;i<4;i++)for(j=0;j<4;j++)if(!( s&(98<<(i*5+j)) ))
    if(back(s|(98<<(i*5+j)))==2)return d[s]=1;
  return d[s]=2;
}

int main() {
  int i,j,k;
  scanf("%d",&c);
  while(c--){
    for(i=0;i<5;i++)scanf("%s",a[i]);
    k=0;
    for(i=4;i>=0;i--)for(j=4;j>=0;j--)
      k=(k<<1)|(a[i][j]=='#');
    if(back(k)==1)printf("WINNING\n");
    else printf("LOSING\n");
  }
  return 0;
}
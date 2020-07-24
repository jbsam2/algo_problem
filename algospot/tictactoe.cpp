#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int cache[19683];

bool isfinished(const vector<string> &board,char turn)
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
		{
			if(board[i][j]!=turn)break;
			if(j==2)return true;
		}
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
		{
			if(board[j][i]!=turn)break;
			if(j==2)return true;
		}
	for(int i=0;i<3;i++)
	{
		if(board[i][i]!=turn)break;
		if(i==2)return true;
	}
	for(int i=0;i<3;i++)
	{
		if(board[i][2-i]!=turn)break;
		if(i==2)return true;
	}
	return false;
}

int bijection(const vector<string> &board)
{
	int ret=0;
	for(int y=0;y<3;y++)
		for(int x=0;x<3;x++)
		{
			ret*=3;
			if(board[y][x]=='o')ret++;
			else if(board[y][x]=='x')ret+=2;
		}
	return ret;
}

int canwin(vector<string> &board,char turn)
{
	if(isfinished(board,'o'+'x'-turn))return -1;
	int &ret=cache[bijection(board)];
	if(ret!=-2)return ret;
	int minvalue=2;
	for(int y=0;y<3;y++)
		for(int x=0;x<3;x++)
			if(board[y][x]=='.')
			{
				board[y][x]=turn;
				minvalue=min(minvalue,canwin(board,'o'+'x'-turn));
				board[y][x]='.';
			}
	if(minvalue==2||minvalue==0)return ret=0;
	return ret=-minvalue;
}

int main()
{
	int test;
	cin>>test;
	vector<string> board;
	for(int i=0;i<19683;i++)
		cache[i]=-2;
	while(test--)
	{
		board.clear();
		int placed=0;
		for(int i=0;i<3;i++)
		{
			string cell;
			cin>>cell;
			for(int k=0;k<3;k++)
				if(cell[k]!='.')
					placed++;
			board.push_back(cell);
		}
		char start='x';
		if(placed%2==1)
			start='o';
		switch(canwin(board,start))
		{
			case -1:
			cout<<(char)('x'+'o'-start)<<endl;
			break;
			case 0:
			cout<<"TIE"<<endl;
			break;
			case 1:
			cout<<start<<endl;
			break;
		}
	}
	return 0;
}

#include <cstdio>

int game(int p[])
{
    for(int i=0;i<3;i++)
	{
		if(p[i]==p[i+3] && p[i]==p[i+6])
			if(p[i]==1 || p[i]==2)
				return p[i];
		if(p[3*i]==p[3*i+1] && p[3*i]==p[3*i+2])
			if(p[3*i]==1 || p[3*i]==2)
				return p[3*i];
	}
	if(p[0]==p[4] && p[0]==p[8])
			if(p[0]==1 || p[0]==2)
				return p[0];
	if(p[2]==p[4] && p[2]==p[6])
			if(p[2]==1 || p[2]==2)
				return p[2];

	int cnt=0;
	for(int i=0;i<9;i++)
		if(p[i]!=0)
			cnt++;
	if(cnt==9)
		return 0;
	int turn=cnt%2==0?2:1;
	bool possible=false; //possible to tie?
	for(int i=0;i<9;i++)
	{
		if(p[i]==0)
		{
			p[i]=turn;
			int res=game(p);
			p[i]=0;
			if(res==turn)
			{
				return res;
			}
			else if(res==0)
				possible=true;
		}
	}
	if(possible)
		return 0;
	else
		return 3-turn;
}

int main()
{
	int C;
	scanf("%d",&C);
	for(;C>0;C--)
	{
		char tmp[4];
		int pan[9];
		for(int i=0;i<3;i++)
		{
			scanf("%s",tmp);
			for(int j=0;j<3;j++)
				pan[i*3+j]=tmp[j]=='.'?0:(tmp[j]=='o'?1:2);
		}
		int res=game(pan);
		printf("%s\n",res==0?"TIE":(res==1?"o":"x"));
	}
}
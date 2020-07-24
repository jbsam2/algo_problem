#include<iostream>
#include<cstring>
using namespace std;
struct offsets
{
	int x,y;
};

offsets moveDir[8]={{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};

char word[11];
char board[5][5];
bool record[5][5][10];

bool search(int y,int x,int idx)
{
	record[y][x][idx]=1;
	if(board[y][x]!=word[idx])
		return false;
	if(idx==strlen(word)-1)
		return true;
	for(int i=0;i<8;i++)
	{
		int Y=y+moveDir[i].y,X=x+moveDir[i].x;
		if(Y<5&&X<5&&Y>=0&&X>=0)
		{
			if (record[Y][X][idx+1])
				continue;
			if(search(Y,X,idx+1))
				return true;
		}
	}
	return false;
}
int main(void)
{
	int testcase;
	cin>>testcase;
	for(int a=0;a<testcase;a++)
	{
		int word_num;
		for(int i=0;i<5;i++)
			scanf("%s",board[i]);
		scanf("%d",&word_num);
		for(int j=0;j<word_num;j++)
		{
			memset(record,0,sizeof(record));
			scanf("%s",word);
			printf("%s ",word);
			bool result=false;
			for(int k=0;k<5;k++)
			{
				for(int l=0;l<5;l++)
				{
					if(search(k,l,0))
						result=true;
					if(result)
						break;
				}
				if(result)
					break;
			}
			if(result)
			    puts("YES");
			else
			    puts("NO");
		}
	}
	return 0;
}
#include <string>
#include <vector>
using namespace std;

int charcmp(char a,char b)
{
	if(a==b)return 0;
	else if(isupper(a)&&!isupper(b)&&a==(b-32))return 0;
	else if(!isupper(a)&&isupper(b)&&a==(b+32))return 0;
	return 1;
}

int solution(int m,int n,vector<string> board)
{
    int answer = 0;
    bool flag=false;
	do
	{
		flag=0;
		for(int i=0;i<m-1;i++)
		{
			for(int j=0;j<n-1;j++)
			{
				if(board[i][j]!=' '&&!charcmp(board[i][j],board[i][j+1])&&!charcmp(board[i][j],board[i+1][j])&&!charcmp(board[i+1][j+1],board[i][j]))
				{
					if(isupper(board[i][j]))board[i][j]+=32,answer++;
					if(isupper(board[i][j+1]))board[i][j+1]+=32,answer++;
					if(isupper(board[i+1][j]))board[i+1][j]+=32,answer++;
					if(isupper(board[i+1][j+1]))board[i+1][j+1]+=32,answer++;
					flag=true;
				}
			}
		}
		if(flag)
		{
			for(int k=0;i<m-1;i++)
			{
				for(int i=0;i<m-1;i++)
				{
					for(int j=0;j<n;j++)
					{
						if(board[i+1][j]==' '||!isupper(board[i+1][j]))
						{
							board[i+1][j]=board[i][j];
							board[i][j]=' ';
						}
					}
				}
			}
		}
	}while(flag);
    return answer;
}
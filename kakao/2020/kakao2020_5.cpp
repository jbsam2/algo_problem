#include <string>
#include <vector>
using namespace std;

int board[101][101][2],N;

bool possi(int x,int y,int kind)
{
    if(!kind)
    {
        if(!y)return true;
        else if(1<=y&&board[x][y-1][0])return true;
        else if((1<=x&&board[x-1][y][1])||(x<=N-1&&board[x][y][1]))return true;
    }
    else
    {
        if((1<=y&&board[x][y-1][0])||(1<=y&&x<=N-1&&board[x+1][y-1][0]))return true;
        else if(1<=x&&board[x-1][y][1]&&x<=N-2&&board[x+1][y][1])return true;
    }
    return false;
}

bool erase()
{
    for(int i=0;i<=N;i++)
        for(int j=0;j<=N;j++)
            for(int k=0;k<2;k++)
                if(board[i][j][k])
                {
                    board[i][j][k]=0;
                    if(!possi(i,j,k))
                    {
                        board[i][j][k]=1;
                        return false;
                    }
                    board[i][j][k]=1;
                }
    return true;
}

vector<vector<int>> solution(int n,vector<vector<int>> build_frame)
{
    vector<vector<int>> answer;
    N=n;

    for(int i=0;i<build_frame.size();i++)
    {
        int x=build_frame[i][0];
        int y=build_frame[i][1];

        if(build_frame[i][3])
        {
            if(possi(x,y,build_frame[i][2]))
                board[x][y][build_frame[i][2]]=1;
        }
        else
        {
            board[x][y][build_frame[i][2]]=0;
            if(!erase())board[x][y][build_frame[i][2]]=1;
        }
    }
    for(int x=0;x<=N;x++)
        for(int y=0;y<=N;y++)
            for(int k=0;k<2;k++)
                if(board[x][y][k])
                {
                    vector<int> tmp;
                    tmp.push_back(x);
                    tmp.push_back(y);
                    tmp.push_back(k);
                    answer.push_back(tmp);
                }
    return answer;
}
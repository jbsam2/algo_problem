#include <bits/stdc++.h>
using namespace std;

int dy[4]={1,-1,0,0},dx[4]={0,0,-1,1};
int ddy[2]={0,1},ddx[2]={1,0};
int n;
int c(int y,int x,int k){return 200*y+2*x+k;}
int check(int y,int x,vector<vector<int>>& board){return 0<=y && y<n && 0<=x && x<n && board[y][x]==0;}

int solution(vector<vector<int>> board){
    n=board.size();
    int visit[100][100][2];
    memset(visit,0,sizeof(visit));
    visit[0][0][0]=1;

    queue<int> q;
    q.push(c(0,0,0));
    int answer=0;

    while(q.size())
    {
        int l=q.size();
        while(l--)
        {
            int y,x,d,k=q.front();q.pop();
            y=k/200,x=k%200/2,d=k%2;
            int y2=y+ddy[d],x2=x+ddx[d];
            if((x==n-1&&y==n-1)||(x2==n-1&&y2==n-1))return answer;
            for(int i=0;i<4;i++)
            {
                int ny=y+dy[i],nx=x+dx[i],ny2=y2+dy[i],nx2=x2+dx[i];
                if(check(ny,nx,board)&&check(ny2,nx2,board)&&!visit[ny][nx][d])visit[ny][nx][d]=1,q.push(c(ny,nx,d));
            }
            if(d)
            {
                if(check(y,x+1,board)&&check(y2,x2+1,board))
                {
                    if(!visit[y][x][0])visit[y][x][0]=1,q.push(c(y,x,0));
                    if(!visit[y+1][x][0])visit[y+1][x][0]=1,q.push(c(y+1,x,0));
                }
                if(check(y,x-1,board)&&check(y2,x2-1,board))
                {
                    if(!visit[y][x-1][0])visit[y][x-1][0]=1,q.push(c(y,x-1,0));
                    if(!visit[y+1][x-1][0])visit[y+1][x-1][0]=1,q.push(c(y+1,x-1,0));
                }
            }
            else
            {
                if(check(y+1,x,board)&&check(y2+1,x2,board))
                {
                    if(!visit[y][x][1])visit[y][x][1]=1,q.push(c(y,x,1));
                    if(!visit[y][x+1][1])visit[y][x+1][1]=1,q.push(c(y,x+1,1));
                }
                if(check(y-1,x,board)&&check(y2-1,x2,board))
                {
                    if(!visit[y-1][x][1])visit[y-1][x][1]=1,q.push(c(y-1,x,1));
                    if(!visit[y-1][x+1][1])visit[y-1][x+1][1]=1,q.push(c(y-1,x+1,1));
                }
            }            
        }
        answer++;
    }
}
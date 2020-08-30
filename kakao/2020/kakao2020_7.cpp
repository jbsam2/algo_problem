#include <string>
#include <vector>
#include <queue>
using namespace std;

struct possition
{int y[2],x[2],dir[2];};

int n;
int dy[4]={0,1,0,-1}; //우하좌상
int dx[4]={1,0,-1,0};
bool flag[101][101][4];

bool check(int y1,int x1,int y2,int x2,vector<vector<int>> board)
{return (y1<0||n<=y1||x1<0||n<=x1||y2<0||n<=y2||x2<0||n<=x2||board[y1][x1]||board[y2][x2]);}

int solution(vector<vector<int>> board)
{
    int answer=0;
    queue<possition> q;
    q.push({0,0,0,1,0,2});
    flag[0][0][0]=flag[0][1][2]=true;
    n=board.size();

    while(q.empty())
    {
        int l=q.size();
        while(l--)
        {
            possition now=q.front();
            q.pop();

            if((now.y[0]==n-1&&now.x[0]==n-1)||(now.y[1]==n-1&&now.x[1]==n-1))return answer;

            for(int i=0;i<4;i++)
            {
                int ny1=now.y[0]+dy[i],nx1=now.x[0]+dx[i];
                int ny2=now.y[1]+dy[i],nx2=now.x[1]+dx[i];
                int dir1=now.dir[0],dir2=now.dir[1];

                if(check(ny1,nx1,ny2,nx2,board)||flag[ny1][nx1][dir1]||flag[ny2][nx2][dir2])continue;
                q.push({ny1,ny2,nx1,nx2,dir1,dir2});
                flag[ny1][nx1][dir1]=flag[ny2][nx2][dir2]=true;
            }

            for(int i=-1;i<=1;i++)
            {
                if(i==0)continue;
                for(int j=0;j<2;j++)
                {
                    int y=now.y[j],x=now.x[j];

                    int dir=(now.dir[j]+i+4)%4; //델타에서 방향 인덱스를 한칸만 움직임
                    int oppodir=(dir+2)%4; //바꾼 방향에서 반대로

                    int ny3=y+dy[dir],nx3=x+dx[dir]; //머리쪽 회전후 위치
                    int ny4=y+dy[dir]+dy[now.dir[j]],nx4=x+dx[dir]+dx[now.dir[j]]; //회전축 대각선 위치 좌표

                    if(check(ny3,nx3,ny4,nx4,board)||flag[y][x][dir]||flag[ny3][nx3][oppodir])continue;
                    q.push({y,ny3,x,nx3,dir,oppodir});
                    flag[y][x][dir]=flag[ny3][nx3][oppodir]=true;
                }
            }
        }
        answer++;
    }
}
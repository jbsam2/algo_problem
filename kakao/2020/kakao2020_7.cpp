#include <string>
#include <vector>
#include <queue>
using namespace std;

struct dron
{
	int y[2],x[2],dir[2];
};

int n;
int dy[]={0,1,0,-1};
int dx[]={1,0,-1,0};
bool check[101][101][4];

bool checking(int y1,int x1,int y2,int x2,vector<vector<int>> board)
{
	return !(y1<0||y1>=n||x1<0||x1>=n||y2<0||y2>=n||x2<0||x2>=n||board[y1][x1]||board[y2][x2]);
}

int solution(vector<vector<int>> board)
{
	int answer=0;
	queue<dron> q;
	n=board.size();
	check[0][0][0]=check[0][1][2]=true;
	q.push({0,0,0,1,0,2});

	while(q.empty())
	{
		int l=q.size();
		while(l--)
		{
			dron now=q.front();
			q.pop();

			if((now.y[0]==n-1&&now.x[0]==n-1)||(now.y[1]==n-1&&now.x[1]==n-1)) return answer;

			for(int dir=0;dir<4;dir++)
			{
				int ny1=now.y[0]+dy[dir],nx1=now.x[0]+dx[dir];
				int ny2=now.y[1]+dy[dir],nx2=now.x[1]+dx[dir];
				int dir1=now.dir[0],dir2=now.dir[1];

				if(!checking(ny1,nx1,ny2,nx2,board)||check[ny1][nx1][dir1]||check[ny2][nx2][dir2]) continue;
				check[ny1][nx1][dir1]=check[ny2][nx2][dir2]=true;
				q.push({ny1,ny2,nx1,nx2,dir1,dir2});
			}

			for(int i=-1;i<=1;i++)
			{
				if(i==0)continue;
				for(int j=0;j<2;j++)
				{
					int y=now.y[j],x=now.x[j];

					int dir=(now.dir[j]+i+4)%4;
					int prev_dir=(dir-i+4)%4;
					int oppo_dir=(dir+2)%4;

					int ny=y+dy[dir],nx=x+dx[dir];
					int tmpy=y+dy[dir]+dy[prev_dir],tmpx=x+dx[dir]+dx[prev_dir];

					if(!checking(ny,nx,tmpy,tmpx,board)||check[y][x][dir]||check[ny][nx][oppo_dir]) continue;
					check[y][x][dir]=check[ny][nx][oppo_dir]=true;
					q.push({y,ny,x,nx,dir,oppo_dir});
				}
			}
		}
		answer++;
	}
}
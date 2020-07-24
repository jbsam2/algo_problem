#include<iostream>
using namespace std;
int N,M,A[10][10],B[10];
int F()
{
  int i,j,r=2;
  for(i=0;i<N;i++)
    if(!B[i])
      {
        r=B[i]=1;
        for(j=i;j<N;j++)
          if(!B[j]&A[i][j])
            {
              B[j]=1;
              r+=F();
              B[j]=0;
            }
        B[i]=0;
        i=N;
      }
  return r-1;
}
int main()
{
  int T,i,j,x,y;
  for(cin>>T;T>=1;T--)
    {
      cin>>N>>M;
      for(i=0;i<N;i++)
        for(j=0;j<N;j++)
          A[i][j]=0;
      for(i=0;i<M;i++)
        {
          cin>>x>>y;
          A[x][y]=A[y][x]=1;
        }
      cout<<F()<<endl;
    }
}

#include <iostream>
using namespace std; 

//주어진 칸을 덮을 수 있는 네가지 방법
//블록을 구성하는 세 칸의 상대적 위치 (dy, dx)의 목록
const int coverType[4][3][2]=
{
        //ㅁㅁ
        //ㅁ
        {{0,0}, {1, 0}, {0, 1}},
        //ㅁㅁ
        //  ㅁ
        {{0, 0}, {0, 1}, {1, 1}},
        //ㅁ
        //ㅁㅁ
        {{0, 0}, {1, 0}, {1, 1}},
        //  ㅁ
        //ㅁㅁ
        {{0, 0}, {1, 0}, {1, -1}}
}; 

//board의 (y, x)를 type번 방법으로 덮거나, 덮었던 블록을 없앤다
//push가 1이면 덮고, -1이면 덮었던 블록을 없앤다
//만약 블록이 제대로 덮이지 않은 경우(게임판 밖으로 나가거나
//겹치거나 검은 칸을 덮을 때) false 반환
bool set(int board[][20], int y, int x, int H, int W, int type, int push)
{
        bool ok = true;
        for (int i = 0; i < 3; i++)
        {
               const int ny = y + coverType[type][i][0];
               const int nx = x + coverType[type][i][1];
               if (ny < 0 || ny >= H || nx < 0 || nx >= W) //범위를 초과할 경우
                       ok = false;
               else if ((board[ny][nx] += push) > 1) //겹쳐질 경우
                       ok = false;
        }
        return ok;
}
//board의 모든 빈 칸을 덮을 수 있는 방법의 수를 반환
//board[i][j]=1 이미 덮인 칸 혹은 검은 칸
//board[i][j]=0 아직 덮이지 않은 칸
int cover(int board[][20], int H, int W)
{
        //아직 채우지 못한 칸 중 가장 윗줄 왼쪽에 있는 칸을 찾는다
        int y = -1, x = -1;
        for (int i = 0; i < H; i++)
        {
               for (int j = 0; j < W; j++)
                       if (!board[i][j]) //아직 채우진 못한 칸 찾음
                       {
                              y = i;
                              x = j;
                              break;
                       }
               if (y != -1)
                    break;
        }
        //기저 사례: 모든 칸을 채웠으면 1을 반환
        if (y == -1)
               return 1;
        int result = 0;
        for (int type = 0; type < 4; type++)
        {
               //만약 board[y][x]를 type 형태로 덮을 수 있으면 재귀 호출
               if (set(board, y, x, H, W, type, 1))
                       result += cover(board, H, W);
               //덮었던 블록 치운다
               set(board, y, x, H, W, type, -1);
        }
        return result;
}
int main(void)
{
        int test_case, H, W; //H=height, W=width
        int board[20][20];
        char bw[20]; //black/white
        cin >> test_case;
        if (test_case < 0 || test_case > 30)
               exit(-1);
        for (int i = 0; i < test_case; i++)
        {
               cin >> H >> W;
               if (H < 1 || H>20 || W < 1 || W>20)
                       exit(-1);
               for (int i = 0; i < H; i++)
               {
                       cin >> bw;
                       for (int j = 0; j < W; j++)
                              board[i][j] = (bw[j] == '#') ? 1 : 0;
               }
               cout << cover(board, H, W) << endl;
        }
        return 0;
}

#include <stdio.h>
#define L(m, f) if (m >= 0 && m < w*h && b[m] == '.') { b[m] = '*'; f; b[m] = '.'; }
#define R(m) L(m, s += c(i+1))
char h, w, b[420];
int c(int n)
{
  int s = 0;
  for (int i = n; i < w*h; i++) 
  {
    L(i,L(i+1, R(i+w) R(i+w+1)) L(i+w, R(i+w-1) R(i+w+1))) else continue;
    return s;
  }
  return 1;
}
int main() 
{
  int t, i;
  scanf("%d", &t);
  while (t--) 
  {
    scanf("%d %d", &h, &w);
    w++;
    for (i = h; i--;)
      scanf("%s", b+i*w);
    printf("%d\n", c(0));
  }
}

#include <stdio.h>
#include <string.h>

char B[401];
int H,W;

#define F(i,j) {B[i]=B[j]='#'; ret+=f(x+1); B[i]=B[j]='.';}

int f(int x) {
  for(;x<H*W&&B[x]!='.';++x);
  if(x==H*W) return 1;

  int ret=0;
  B[x]='#';

  if(x+W<H*W && (x+1)%W && B[x+W]=='.' &&B [x+W+1]=='.') F(x+W,x+W+1)
  if((x+1)%W && x+1+W<H*W && B[x+1]=='.' && B[x+1+W]=='.') F(x+1,x+1+W)
  if((x+1)%W && x+W<H*W && B[x+1]=='.' && B[x+W]=='.') F(x+1,x+W)
  if(x+W<H*W && x%W && B[x+W]=='.' && B[x+W-1]=='.') F(x+W,x+W-1)
  B[x]='.';
  return ret;
}

int main() {
  int C;

  scanf("%d",&C);
  while(--C>=0) {
    scanf("%d%d",&H,&W);
    for(int i=0;i<H;++i)
      scanf("%s",B+i*W);
    printf("%d\n",f(0));
  }
}
#include <iostream>
#include <algorithm>
using namespace std;

int board[50],size,cache[50][50];

int play(int left,int right)
{
	if(left>right)return 0;
	int& ret=cache[left][right];
	if(ret!=-500001)return ret;
	ret=max(board[left]-play(left+1,right),board[right]-play(left,right-1));
	if(right-left+1>=2)ret=max(ret,max(-play(left+2,right),-play(left,right-2)));
	return ret;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		for(int i=0;i<50;i++)for(int j=0;j<50;j++)cache[i][j]=-500001;
		cin>>size;
		for(int i=0;i<size;i++)cin>>board[i];
		cout<<play(0,size-1)<<endl;
	}
	return 0;
}

#include <stdio.h>
#include <algorithm>
int T,N,A[55],D[55][55],i,j,k;int main(){scanf("%d",&T);while(T--){scanf("%d",&N);for(i=1;i<=N;i++)scanf("%d",&A[i]),D[i][i]=A[i];for(k=2;k<=N;k++)for(i=1,j=k;j<=N;i++,j++)D[i][j]=std::max(std::max(-D[i+2][j],-D[i][j-2]),std::max(A[i]-D[i+1][j],A[j]-D[i][j-1]));printf("%d\n",D[1][N]);}return 0;}
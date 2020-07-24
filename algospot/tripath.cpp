#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n,triangle[100][100],cache[100][100];

int path(int y,int x)
{
	if(y==n-1)return triangle[y][x];
	int &ret=cache[y][x];
	if(ret!=-1)return ret;
	return ret=max(path(y+1,x),path(y+1,x+1))+triangle[y][x];
}

int main()
{
	int test;
	cin>>test;
	if(test>50||test<0)
		exit(-1);
	while(test--)
	{
		memset(cache,-1,sizeof(cache));
		cin>>n;
		if(n<2||n>100)
			exit(-1);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<=i;j++)
			{
				cin>>triangle[i][j];
				if(triangle[i][j]<1||triangle[i][j]>100000)
					exit(-1);
			}
		}
		cout<<path(0,0)<<endl<<endl;
	}
	return 0;
}

#include <stdio.h>

int max(int l, int r){return l>r?l:r;}

int main()
{
	int t, n, i, j, x[200][200];
	scanf("%d", &t);
	for(;t;t--)
	{
		scanf("%d", &n);
		for(i=0;i<n;i++)for(j=0;j<=i;j++)scanf("%d",&x[i][j]);
		for(i=n-1;i>0;i--)for(j=0;j<i;j++)x[i-1][j]+=max(x[i][j],x[i][j+1]);
		printf("%d\n",x[0][0]);
	}
	return 0;
}
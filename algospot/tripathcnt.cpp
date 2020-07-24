#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int cache[100][100],triangle[100][100],n,countcache[100][100];

int path(int y,int x)
{
	if(y==n-1)return triangle[y][x];
	int &ret=cache[y][x];
	if(ret!=-1)return ret;
	return ret=max(path(y+1,x),path(y+1,x+1))+triangle[y][x];
}
int count(int y,int x)
{
	if(y==n-1)return 1;
	int& ret=countcache[y][x];
	if(ret!=-1)return ret;
	ret=0;
	if(path(y+1,x+1)>=path(y+1,x))ret+=count(y+1,x+1);
	if(path(y+1,x+1)<=path(y+1,x))ret+=count(y+1,x);
	return ret;
}
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			for(int j=0;j<=i;j++)
				cin>>triangle[i][j];
		memset(cache,-1,sizeof(cache));
		memset(countcache,-1,sizeof(countcache));
		cout<<count(0,0)<<endl<<endl;
	}
	return 0;
}

#include<cstdio>
#include<cstring>
#include<algorithm>
int c,n,t[100][100],p[100][100],i,j;
int main()
{
	scanf("%d",&c);
	while(c--)
		{
			scanf("%d",&n);
			for(i=0;i<n;i++)
				for(j=0;j<=i;j++)
					scanf("%d",&t[i][j]);
			memset(p,0,sizeof(p));
			for(i=0;i<n;i++)
				p[n-1][i]=1;
			for(i=n-2;i>=0;i--)
				for(j=0;j<=i;j++)
					{
						if(t[i+1][j]>=t[i+1][j+1])p[i][j]+=p[i+1][j];
						if(t[i+1][j]<=t[i+1][j+1])p[i][j]+=p[i+1][j+1];
						t[i][j]+=std::max(t[i+1][j],t[i+1][j+1]);
					}
			printf("%d\n",p[0][0]);
		}
}
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int INF=987654321;
int n,a[100],psum[100],psqsum[100],cache[100][10];
void precalc()
{
	sort(a,a+n);
	psum[0]=a[0];
	psqsum[0]=a[0]*a[0];
	for(int i=0;i<n;i++)
	{
		psum[i]=psum[i-1]+a[i];
		psqsum[i]=psqsum[i-1]+a[i]*a[i];
	}
}
int minerror(int lo,int hi)
{
	int sum=psum[hi]-(lo==0?0:psum[lo-1]);
	int sqsum=psqsum[hi]-(lo==0?0:psqsum[lo-1]);
	int m=int(0.5+(double)sum/(hi-lo+1));
	int ret=sqsum-2*m*sum+m*m*(hi-lo+1);
	return ret;
}
int quantize(int from,int parts)
{
	if(from==n)return 0;
	if(parts==0)return INF;
	int& ret=cache[from][parts];
	if(ret!=-1)return ret;
	ret=INF;
	for(int partsize=1;from+partsize<=n;partsize++)
	{
		ret=min(ret,minerror(from,from+partsize-1)+quantize(from+partsize,parts-1));
	}
	return ret;
}
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		int use;
		cin>>n>>use;
		for(int i=0;i<n;i++)
			cin>>a[i];
		precalc();
		memset(cache,-1,sizeof(cache));
		cout<<quantize(0,use)<<endl<<endl;
	}
	return 0;
}


#include<cstdio>
#include<algorithm>
using namespace std;
int T,n,s,inp[110],dyn[12][110],gap[102][102];
int main()
{
	int i,j,k,sum,t;
	bool p;
	for(scanf("%d",&T); T--;)
	{
		scanf("%d%d",&n,&s);
		for(i=1; i<=n; i++) scanf("%d",&inp[i]);
		sort(inp+1,inp+n+1);
		for(i=1; i<=n; i++)
		{
			sum=0;
			for(j=i; j<=n; j++)
			{
				sum+=inp[j];
				p=(sum%(j-i+1)>(j-i+1)/2);
				t=sum/(j-i+1);
				gap[i][j]=0;
				for(k=i; k<=j; k++) gap[i][j]+=(inp[k]-t-p)*(inp[k]-t-p);
			}
		}
		for(i=1; i<=n; i++)
			dyn[1][i]=gap[1][i];
		for(i=2; i<=s; i++)
		{
			for(j=i; j<=n; j++)
			{
				dyn[i][j]=0x7fffffff;
				for(k=j; k>=i-1; k--)
				{
					dyn[i][j]=min(dyn[i][j],dyn[i-1][k]+gap[k+1][j]);
				}
			}
		}
		printf("%d\n",dyn[s][n]);
	}
	return 0;
}
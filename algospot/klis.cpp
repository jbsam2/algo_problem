#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX=2000000001;
int n,cachelen[501],cachecnt[501],s[501];

int lis(int start)
{
	int& ret=cachelen[start+1];
	if(ret!=-1)return ret;
	ret=1;
	for(int next=start+1;next<n;next++)
		if(start==-1||s[start]<s[next])
			ret=max(ret,lis(next)+1);
	return ret;
}

int count(int start)
{
	if(lis(start)==1)return 1;
	int& ret=cachecnt[start+1];
	if(ret!=-1)return ret;
	ret=0;
	for(int next=start+1;next<n;next++)
		if((start==-1||s[start]<s[next])&&lis(start)==lis(next)+1)
			ret=min<long long>(MAX,(long long)ret+count(next));
	return ret;
}

void reconstruct(int start,int skip,vector<int>& v)
{
	if(start!=-1)v.push_back(s[start]);
	vector<pair<int,int>> followers;
	for(int next=start+1;next<n;next++)
		if((start==-1||s[start]<s[next])&&lis(start)==lis(next)+1)
			followers.push_back(make_pair(s[next],next));
	sort(followers.begin(),followers.end());
	for(int i=0;i<followers.size();i++)
	{
		int idx=followers[i].second;
		int cnt=count(idx);
		if(cnt<=skip)
			skip-=cnt;
		else
		{
			reconstruct(idx,skip,v);
			break;
		}
	}
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		int k;
		cin>>n>>k;
		for(int i=0;i<n;i++)
			cin>>s[i];
		memset(cachelen,-1,sizeof(cachelen));
		memset(cachecnt,-1,sizeof(cachecnt));
		cout<<lis(-1)-1<<endl;
		vector<int> ret;
		reconstruct(-1,k-1,ret);
		for(int i=0;i<ret.size();i++)
			cout<<ret[i]<<" ";
		cout<<endl;
	}
	return 0;
}

#include <stdio.h>
#include <algorithm>
#define oo 2147483647

int d[505];unsigned int c[505];
struct D
{
	int no,num;
	bool friend operator < (const D &p,const D &q)
	{
		return p.num<q.num;
	}
}a[505];

int main(void)
{
	int t,n,m,i,j,k,last;

	for(scanf("%d",&t);t--;)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;++i) a[i].no=i, scanf("%d",&a[i].num);
		std::sort(a+1,a+n+1);

		for(i=n;i>=0;--i)
		{
			d[i]=1; c[i]=1;
			for(j=i+1;j<=n;++j)
				if(a[i].no<a[j].no)
					if(d[i]<d[j]+1)
						d[i]=d[j]+1, c[i]=c[j];
					else if(d[i]==d[j]+1)
						if((c[i]+=c[j])>oo) c[i]=oo;
			if(d[i]>k) k=d[i];
		}

		printf("%d\n",d[0]-1);

		last=0;
		for(i=1;i<=n;++i)
			if(a[last].no<a[i].no && d[last]==d[i]+1)
				if(m<=c[i])
				{
					printf("%d ",a[i].num);
					last=i;
				}
				else
					m-=c[i];

		printf("\n");
	}
	return 0;
}
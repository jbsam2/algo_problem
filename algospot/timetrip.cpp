#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

vector<vector<pair<int,int>>> adj;
const int MAX=1<<30;
const int MIN=-10000000;
const int INF=1<<31;

pair<int,int> bellman(int v)
{
	int s[100],l[100];
	for(int i=0;i<100;i++)
		s[i]=MAX,l[i]=MIN;
	s[0]=l[0]=0;

	bool sd,ld;
	bool su,lu;

	sd=ld=false;

	for(int time=0;time<v;time++)
	{
		su=lu=false;
		for(int i=0;i<v;i++)
		{
			if(!sd&&s[i]!=MAX)
			{
				for(int j=0;j<adj[i].size();j++)
				{
					int there=adj[i][j].first;
					int cost=s[i]+adj[i][j].second;

					if(cost<s[there])
						s[there]=cost,su=true;
				}
			}
			if(!ld&&l[i]!=MIN)
			{
				for(int j=0;j<adj[i].size();j++)
				{
					int there=adj[i][j].first;
					int cost=l[i]+adj[i][j].second;

					if(cost>l[there])
						l[there]=cost,lu=true;
				}
			}
		}
		if(!su) sd=true;
		if(!lu) ld=true;
		if(sd && ld)break;
	}
	int past,future;
	past=s[1],future=l[1];
	if(su)past=INF;
	if(lu)future=INF;
	return make_pair(past,future);
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int v,w;
		cin>>v>>w;
		adj.clear();
		adj.resize(v);
		for(int i=0;i<w;i++)
		{
			int a,b,d;
			cin>>a>>b>>d;
			adj[a].push_back(make_pair(b,d));
		}
		auto ret=bellman(v);
		int past=ret.first;
		int future=ret.second;

		if(past==INF)
			cout<<"INFINITY ";
		else if(past==MAX)
		{
			cout<<"UNREACHABLE"<<endl;
			continue;
		}
		else
			cout<<past<<" ";
		if(future==INF)
			cout<<"INFINITY"<<endl;
		else
			cout<<future<<endl;
	}
}

#include <stdio.h>
int v,w,a[1001],b[1001],d[1001],s[101],l[101],t,i;
int main()
{
	scanf("%d",&t);while(t--)
	{
		scanf("%d%d",&v,&w);for(i=0;i<w;i++)scanf("%d%d%d",&a[i],&b[i],&d[i]);for(i=0;i<v;i++)s[i]=1e9,l[i]=-1e9;
		bool f=1,k=1;int c=0,x=0;s[0]=l[0]=0;
		while(f){c++;f=0;for(i=0;i<w;i++)if(s[b[i]]>s[a[i]]+d[i])s[b[i]]=s[a[i]]+d[i],f=1;if(f&&c==v)break;}
		while(k){x++;k=0;for(i=0;i<w;i++)if(l[b[i]]<l[a[i]]+d[i])l[b[i]]=l[a[i]]+d[i],k=1;if(k&&x==v)break;}
		(s[1]>1e8)?printf("UNREACHABLE\n"):(printf((f&&c==v)?"INFINITY ":"%d ",s[1]),printf((k&&x==v)?"INFINITY\n":"%d\n",l[1]));
	}
}
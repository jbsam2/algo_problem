#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
struct BipartiteUnionfind
{
	vector<int> parent,rank,enemy,size;
	BipartiteUnionfind(int n):parent(n),rank(n,1),enemy(n,-1),size(n,1)
	{
		for(int i=0;i<n;i++)
			parent[i]=i;
	}
	int find(int u)
	{
		if(u==parent[u]) return u;
		return parent[u]=find(parent[u]);
	}
	int merge(int u,int v)
	{
		if(u==-1||v==-1)return max(u,v);
		u=find(u);v=find(v);
		if(u==v) return u;
		if(rank[u]>rank[v]) swap(u,v);
		parent[u]=v;
		if(rank[u]==rank[v])rank[v]++;
		parent[u]=v;
		size[v]+=size[u];
		return v;
	}
	bool dis(int u,int v)
	{
		u=find(u);v=find(v);
		if(u==v)return false;
		int a=merge(u,enemy[v]),b=merge(v,enemy[u]);
		enemy[a]=b;enemy[b]=a;
		return true;
	}
	bool ack(int u,int v)
	{
		u=find(u);v=find(v);
		if(v==enemy[u])return false;
		int a=merge(u,v),b=merge(enemy[u],enemy[v]);
		enemy[a]=b;
		if(b!=-1)enemy[b]=a;
		return true;
	}
};

int maxParty(const BipartiteUnionfind& buf)
{
	int ret=0;
	for(int node=0;node<N;node++)
		if(buf.parent[node]==node)
		{
			int enemy=buf.enemy[node];
			if(enemy>node)continue;
			int mySize=buf.size[node];
			int enemySize=(enemy==-1?0:buf.size[enemy]);
			ret+=max(mySize,enemySize);
		}
	return ret;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t,m,i,node1,node2;
	cin>>t;
	while(t--)
	{
		cin>>N>>m;
		BipartiteUnionfind buf(N);
		bool contradict=false;
		int num=-1;
		for(i=0;i<m;i++)
		{
			string s;
			cin>>s>>node1>>node2;
			if(contradict) continue;
			if(s=="ACK")
			{
				if(!buf.ack(node1,node2))
				{
					contradict=true;
					num=i+1;
				}
			}
			else
			{
				if(!buf.dis(node1,node2))
				{
					contradict=true;
					num=i+1;
				}
			}
		}
		if(contradict)cout<<"CONTRADICTION AT "<<num<<endl;
		else cout<<"MAX PARTY SIZE IS "<<maxParty(buf)<<endl;
	}
	return 0;
}
#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
int dist[1001];
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int V,E,n,m,a,b,t,i,sum=0;
		cin>>V>>E>>n>>m;
		vector<pair<int,int>> v[1001];
		for(i=0;i<E;i++)
		{
			cin>>a>>b>>t;
			v[a].push_back(make_pair(b,t));
			v[b].push_back(make_pair(a,t));
		}
		vector<int> dest;
		for(i=0;i<n;i++)
		{
			cin>>a;
			dest.push_back(a);
		}
		for(i=0;i<m;i++)
		{
			cin>>a;
			v[0].push_back(make_pair(a,0));
		}
		memset(dist,0x1f,sizeof(dist));
		priority_queue<pair<int,int>> pq;
		pq.push(make_pair(0,0));
		dist[0]=0;
		while(!pq.empty())
		{
			pair<int,int> a=pq.top();
			pq.pop();
			if(dist[a.second]<a.first) continue;
			int node=a.second;
			int size=v[node].size();
			for(i=0;i<size;i++)
			{
				pair<int,int> e=v[node][i];
				if(dist[e.first]>dist[node]+e.second)
				{
					dist[e.first]=dist[node]+e.second;
					pq.push(make_pair(-dist[e.first],e.first));
				}
			}
		}
		for(i=0;i<dest.size();i++)
			sum+=dist[dest[i]];
		cout<<sum<<endl;
	}
	return 0;
}

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;

const int INF=1<<29;
int v,e,n,m;
vector<pair<int,int>> adj[1001];

vector<int> sol(int src)
{
	vector<int> dist(v,INF);
	dist[src]=0;
	priority_queue<pair<int,int>> pq;
	pq.push({0,src});

	while(!pq.empty())
	{
		int cost=-pq.top().first;
		int here=pq.top().second;
		pq.pop();
		if(dist[here]<cost)continue;
		for(int i=0;i<adj[here].size();i++)
		{
			int there=adj[here][i].first;
			int nextdist=cost+adj[here][i].second;
			if(dist[there]>nextdist)
			{
				dist[there]=nextdist;
				pq.push({-nextdist,there});
			}
		}
	}
	return dist;
}

int main()
{
	int testcase;
	cin>>testcase;
	while(testcase--)
	{
		memset(adj,0,sizeof(adj));
		vector<int> arr;
		scanf("%d %d %d %d",&v,&e,&n,&m);
		v++;
		for(int i=0;i<e;i++)
		{
			int t1,t2,t3;
			scanf("%d %d %d",&t1,&t2,&t3);
			adj[t1].push_back({t2,t3});
			adj[t2].push_back({t1,t3});
		}
		for(int i=0;i<n;i++)
		{
			int t1;
			scanf("%d",&t1);
			arr.push_back(t1);
		}
		for(int i=0;i<m;i++)
		{
			int t1;
			scanf("%d",&t1);
			adj[0].push_back({t1,0});
		}
		vector<int> tmps=sol(0);
		int sum=0;
		for(int i=0;i<arr.size();i++)
		{
			sum+=tmps[arr[i]];
		}
		printf("%d\n",sum);
	}
}
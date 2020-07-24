#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

int n;
const double INF=987654321.0;

vector<pair<int,double>> adj[10000];

double dijkstra(int src)
{
	double ret;
	vector<double> dist(n,INF);
	dist[src]=0.0;
	priority_queue<pair<double,int>> pq;
	pq.push(make_pair(0.0,src));
	while(!pq.empty())
	{
		double cost=-pq.top().first;
		int here=pq.top().second;
		pq.pop();
		if(dist[here]<cost) continue;
		for(int i=0;i<adj[here].size();i++)
		{
			int there=adj[here][i].first;
			double nextDist=cost+adj[here][i].second;
			if(dist[there]>nextDist)
			{
				dist[there]=nextDist;
				pq.push(make_pair(-nextDist,there));
			}
		}
	}
	ret=exp(dist[n-1]);
	return ret;
}

int main()
{
	int t,m,t1,t2,i;
	double t3;
	cin>>t;
	while(t--)
	{
		cin>>n>>m;
		for(i=0;i<n;i++)
			adj[i].clear();
		for(i=0;i<m;i++)
		{
			cin>>t1>>t2>>t3;
			adj[t1].push_back(make_pair(t2,log(t3)));
			adj[t2].push_back(make_pair(t1,log(t3)));
		}
		cout<<fixed;
		cout.precision(10);
		cout<<dijkstra(0)<<endl;
	}
	return 0;
}
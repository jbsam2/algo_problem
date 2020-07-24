#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int V,adj[500][500],delay[500],W[500][500],E;

void sol()
{
	int i,j,k,w;
	vector<pair<int,int>> order;
	for(i=0;i<V;i++)
		order.push_back(make_pair(delay[i],i));
	sort(order.begin(),order.end());
	for(i=0;i<V;i++)
		for(j=0;j<V;j++)
				W[i][j]=adj[i][j];
	for(k=0;k<V;k++)
	{
		w=order[k].second;
		for(i=0;i<V;i++)
		{
			if(i==w||adj[i][w]==1<<30)continue;
			for(j=0;j<V;j++)
			{
				adj[i][j]=min(adj[i][j],adj[i][w]+adj[w][j]);
				W[i][j]=min(W[i][j],adj[i][w]+delay[w]+adj[w][j]);
			}
		}
	}
}

int main()
{
	int t,a,b,i,j;
	cin>>V>>E;
	for(i=0;i<V;i++)
		cin>>delay[i];

	for(i=0;i<V;i++)
		for(j=0;j<V;j++)
			adj[i][j]=((i==j)?0:1<<30);

	for(i=0;i<E;i++)
	{	
		cin>>a>>b>>t;
		adj[a-1][b-1]=adj[b-1][a-1]=t;
	}
	sol();
	cin>>t;
	while(t--)
	{
		cin>>a>>b;
		cout<<W[a-1][b-1]<<endl;
	}
}
#include <iostream>
#include <algorithm>
using namespace std;

int V,adj[200][200];

bool update(int a,int b,int c)
{
	if(adj[a][b]<=c)return false;
	for(int x=0;x<V;x++)
		for(int y=0;y<V;y++)
			adj[x][y]=min(adj[x][y],min(adj[x][a]+c+adj[b][y],adj[x][b]+c+adj[a][y]));
	return true;	
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int M,N;
		cin>>V>>M>>N;
		for(int i=0;i<V;i++)
			for(int j=0;j<V;j++)
				adj[i][j]=((i==j)?0:987654321);

		for(int i=0;i<M;i++)
		{
			int a,b,c;
			cin>>a>>b>>c;
			adj[a][b]=adj[b][a]=min(adj[a][b],c);
		}
		for(int k=0;k<V;k++)
			for(int i=0;i<V;i++)
				for(int j=0;j<V;j++)
					adj[i][j]=min(adj[i][j],adj[i][k]+adj[k][j]);
		int meaningless=0;
		for(int i=0;i<N;i++)
		{
			int a,b,c;
			cin>>a>>b>>c;
			if(!update(a,b,c))
				meaningless++;
		}
		cout<<meaningless<<endl;
	}
}
#include <iostream>
#include <vector>
using namespace std;

int V;
vector<int> adj[1000];
vector<bool> visited;

const int UNWATCHED=0;
const int WATCHED=1;
const int INSTALLED=2;

int installed;

int dfs(int here)
{
	visited[here]=true;
	int children[3]={0,0,0};
	for(int i=0;i<adj[here].size();i++)
	{
		int there=adj[here][i];
		if(!visited[there])
			children[dfs(there)]++;
	}
	if(children[UNWATCHED])
	{
		installed++;
		return INSTALLED;
	}
	if(children[INSTALLED])
		return WATCHED;
	return UNWATCHED;
}

int installcamera()
{
	installed=0;
	visited=vector<bool>(V,false);
	for(int i=0;i<V;i++)
		if(!visited[i]&&dfs(i)==UNWATCHED)
			installed++;
	return installed;
}

int main()
{
	int t,i,E,a,b;
	cin>>t;
	while(t--)
	{
		cin>>V>>E;
		for(i=0;i<V;i++)adj[i].clear();
		for(i=0;i<E;i++)
		{
			cin>>a>>b;
			adj[a].push_back(b);
			adj[b].push_back(a);
		}
		cout<<installcamera()<<endl;
	}
}
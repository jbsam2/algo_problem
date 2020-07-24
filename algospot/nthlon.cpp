#include <iostream>
#include <queue>
#include <vector>
#include <cmath>
using namespace std;

int V;
const int INF=987654321;

vector<pair<int,int>> adj[410];
const int START=401;

vector<int> dijkstra(int src)
{
	vector<int> dist(V,INF);
	dist[src]=0;
	priority_queue<pair<int,int>> pq;
	pq.push(make_pair(0,src));
	while(!pq.empty())
	{
		int cost=-pq.top().first;
		int here=pq.top().second;
		pq.pop();
		if(dist[here]<cost) continue;
		for(int i=0;i<adj[here].size();i++)
		{
			int there=adj[here][i].first;
			int nextDist=cost+adj[here][i].second;
			if(dist[there]>nextDist)
			{
				dist[there]=nextDist;
				pq.push(make_pair(-nextDist,there));
			}
		}
	}
	return dist;
}

int vertex(int delta)
{
	return delta+200;
}

int sol(const vector<int>& a,const vector<int>& b)
{
	V=402;
	for(int i=0;i<V;i++) adj[i].clear();
	for(int i=0;i<a.size();i++)
	{
		int delta=a[i]-b[i];
		adj[START].push_back(make_pair(vertex(delta),a[i]));
	}
	for(int delta=-200;delta<=200;delta++)
	{
		for(int i=0;i<a.size();i++)
		{
			int next=delta+a[i]-b[i];
			if(abs(next)>200)continue;
			adj[vertex(delta)].push_back(make_pair(vertex(next),a[i]));
		}
	}
	vector<int> shortest=dijkstra(START);
	int ret=shortest[vertex(0)];
	if(ret==INF)return -1;
	return ret;
}

int main()
{
	int t,ret,t1,t2,m,i;	
	cin>>t;
	while(t--)
	{
		cin>>m;
		vector<int> a,b;
		for(i=0;i<m;i++)
		{
			cin>>t1>>t2;
			a.push_back(t1);
			b.push_back(t2);
		}
		ret=sol(a,b);
		if(ret==-1)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ret<<endl;
	}
}

#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;
vector<pair<int,int>> j;
const int I=1<<30;
int dijkstra()
{
	int d[401],i;
	priority_queue<pair<int,int>> q;
	for(i=0;i<401;i++)d[i]=I;
	q.push(make_pair(0,200));
	bool c=true;
	while(!q.empty())
	{
		int h=q.top().second,l=-q.top().first;q.pop();
		if(l>d[h])continue;
		if(c)d[200]=I,c=false;
		else if(h==200)return l;
		for(i=0;i<j.size();i++)
		{
			int t=h+j[i].second,n=l+j[i].first;
			if(t<0||t>400)continue;
			if(n<d[t])d[t]=n,q.push(make_pair(-n,t));
		}
	}
	return -1;
}
int main()
{
	int t,m,i,a,b,r;scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&m);j.clear();j.resize(m);
		for(i=0;i<m;i++)scanf("%d%d",&a,&b),j[i]=make_pair(a,a-b);
		r=dijkstra();
		if(r==-1)printf("IMPOSSIBLE\n");
		else printf("%d\n",r);
	}
}

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <functional>

using namespace std;

// 두 선수중 왼쪽 선수의 기록과 (왼쪽 선수 기록) - (오른쪽 선수 기록)을 저장
// 왼쪽 선수의 기록만 저장하는 이유는 최종 답이 구해졌을 때 합이 같아야하므로 왼쪽 선수 기록의 합을 구하여도 된다.
vector<pair<int,int>> diff;
const int INF = 1 << 30;

int dijkstra()
{
	// 두 선수의 기록차이가 최대 199이므로 그 이상 차이가 나는 경우는 해답과 멀어질 뿐이다
	// 그러므로 정점이 기록차이를 나타낼 때 가질수 있는 범위는 -199 ~ 199 까지이다
	// 200으로 하는것이 깔끔해서 -200 ~ 200으로 정하였다.
	// d는 최단경로의 길이를 저장하는 배열
	int d[401];
	priority_queue<pair<int, int>> q;
	for (int i = 0; i < 401; i++)
		d[i] = INF;
	// -200 ~ 200을 표현하므로 시작정점은 200이고 cost는 0이다.
	q.push(make_pair(0, 200));
	// 다시 0으로 돌아오는 경로를 찾기위해 처음만 true로 해준다.
	bool chk = true;
	while (!q.empty()) {
		int here = q.top().second;
		// 아래에서 음수로 넣어주었기 때문에 다시 -를 붙여준다.
		int cost = -q.top().first;
		q.pop();
		if (cost > d[here])
			continue;
		// 시작 정점을 다시 INF로 바꿔줌으로써 시작정점으로 돌아오는 최단경로를 찾을 수 있다.
		if (chk) {
			d[200] = INF;
			chk = false;
		}
		else {
			// 다시 시작정점으로 돌아온 경우 답을 찾은 것이다.
			if (here == 200)
				return cost;
		}
		for (int i = 0; i < diff.size(); i++) {
			int there = here + diff[i].second;
			// there의 범위가 넘어가면 답이 되는 경로일 가능성이 없으므로 제외해준다/
			if (there < 0 || there >400) continue;
			int next = cost + diff[i].first;
			if (next < d[there]) {
				d[there] = next;
				// C++의 우선순위 큐는 큰수부터 반환하므로 음수로 넣어준다
				q.push(make_pair(-next, there));
			}
		}
	}
	// 큐가 빌 때까지 답을 찾지 못하면 경로가 존재하지 않는 것이다.
	return -1;
}

int main()
{
	int c;
	cin >> c;
	while (c--) {
		int m;
		scanf("%d", &m);
		diff.clear();
		diff.resize(m);
		for (int i = 0; i < m; i++) {
			int a, b;
			scanf("%d%d", &a, &b);
			diff[i] = make_pair(a,a - b);
		}
		int ret = dijkstra();
		if (ret == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ret);
	}
}
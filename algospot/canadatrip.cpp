#include <iostream>
#include <algorithm>
using namespace std;

int n,k,l[5000],m[5000],g[5000];

bool decision(int dist)
{
	int ret=0;
	for(int i=0;i<n;i++)
		if(dist>=l[i]-m[i])
			ret+=(min(dist,l[i])-(l[i]-m[i]))/g[i]+1;
	return ret>=k;
}

int opt()
{
	int lo=-1,hi=8030001;
	while(lo+1<hi)
	{
		int mid=(lo+hi)/2;
		if(decision(mid))hi=mid;
		else lo=mid;
	}
	return hi;
}

int main()
{
	int c;
	cin>>c;
	while(c--)
	{
		cin>>n>>k;
		for(int i=0;i<n;i++)
			cin>>l[i]>>m[i]>>g[i];
		cout<<opt()<<endl;
	}
	return 0;
}

#include <bits/stdc++.h>
#define X first
#define Y second
#define mp make_pair
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define rep(i, s, n) for (int i = s; i < n; ++i)
using namespace std;

using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;
using vi = vector<int>;

const int MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const int MAX = 200000;
const int dx[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
const int dy[] = { 0, 1, 0, -1, 1, 1, -1, -1 };

char buf[1 << 17];

inline char read()
{
	static int idx = 1 << 17;
	if (idx == 1 << 17)
	{
		fread(buf, 1, 1 << 17, stdin);
		idx = 0;
	}
	return buf[idx++];
}
inline int readInt()
{
	int sum = 0;
	bool flg = 1;
	char now = read();

	while (now == 10 || now == 32) now = read();
	if (now == '-') flg = 0, now = read();
	while (now >= 48 && now <= 57)
	{
		sum = sum * 10 + now - 48;
		now = read();
	}

	return flg ? sum : -sum;
}
int main()
{
	int t = readInt();

	int L[5000], M[5000], G[5000];
	while (t--)
	{
		int n = readInt(), k = readInt();

		rep(i, 0, n) L[i] = readInt(), M[i] = readInt(), G[i] = readInt();

		int s = 0, e = 10000000;
		while (s < e)
		{
			int mid = s + e >> 1;
			int cnt = 0;

			rep(i, 0, n)
			{
				if (mid >= L[i]) cnt += M[i] / G[i] + 1;
				else if (M[i] >= L[i] - mid) cnt += (M[i] - L[i] + mid) / G[i] + 1;
			}

			if (cnt >= k) e = mid;
			else s = mid + 1;
		}

		printf("%d\n", s);
	}

	return 0;
}

#include<stdio.h>
int t,n,w[5001][3],i,s,e,mm,m,p,c;
int main()
{
	scanf("%d",&t);
	while(t>0)
	{
		t--;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			scanf("%d%d%d",&w[i][0],&w[i][1],&w[i][2]);
		s=0,e=8030000;
		while(s<=e)
		{
			c=0;
			mm=(s+e+1)/2;
			for(i=0;i<n;i++)
			{
				if(w[i][0]<=mm)
					c+=w[i][1]/w[i][2]+1;
				else if(w[i][0]-w[i][1]<=mm)
					c+=(mm-w[i][0]+w[i][1])/w[i][2]+1;
			}
			if(c>=m)
				{
					p=mm;
					e=mm-1;
				}
			else 
				s=mm+1;
		}
		printf("%d\n",p);
	}
}
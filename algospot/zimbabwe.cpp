#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <bitset>
using namespace std;

string egg,digits;
int n,m,cache[1<<14][20][2];
const int mod=1000000007;

long long price(int idx,int taken,int md,int less)
{
	if(idx==n)return (less&&md==0)?1:0;
	int &ret=cache[taken][md][less];
	if(ret!=-1)return ret;
	ret=0;
	for(int next=0;next<n;next++)
		if((taken&(1<<next))==0)
		{
			if(!less&&egg[idx]<digits[next])continue;
			if(next>0&&digits[next-1]==digits[next]&&(taken&(1<<(next-1)))==0)continue;
			int nexttaken=taken|(1<<next);
			int nextmd=(md*10+digits[next]-'0')%m;
			int nextless=less||egg[idx]>digits[next];
			ret+=price(idx+1,nexttaken,nextmd,nextless);
			ret%=mod;
		}
	return ret;
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		n=0;
		vector<long long> v;
		cin>>egg>>m;
		memset(cache,-1,sizeof(cache));
		digits=egg;
		sort(digits.begin(),digits.end());
		n=egg.length();
		cout<<price(0,0,0,0)<<endl;
	}
	return 0;
}

#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
const int MOD = 1e9 + 7, MAX_M = 21;
int dp[2][1 << 14][MAX_M], L, m;
string e, t;
int rec(int p, int l, int s, int r)
{ 
	if(p==L)return l&&!r;
	int& ret=dp[l][s][r];
	if(ret!=-1)return ret;
	ret=0;
	for (int i = 0; i < L; i++) 
		if((s&(1<<i))==0)
		{
			if(!l&&t[i]>e[p])continue;
			if(i==0||(s&(1<<(i-1)))>0||t[i]!=t[i - 1])
				ret=(ret+rec(p+1,l||t[i]<e[p],s|(1<<i),(r*10+t[i]-'0')%m))%MOD;
		}
	return ret;
}
int main() {
	int c;
	scanf("%d", &c);
	while (c--) {
		memset(dp, -1, sizeof dp);
		cin >> e >> m;
		t = e;
		sort(t.begin(), t.end());
		L = e.length();
		printf("%d\n", rec(0, 0, 0, 0));
	}
	return 0;
}

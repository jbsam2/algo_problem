#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

int waystobuy(const vector<int> &psum,int k)
{
	const int mod=20091101;
	int ret=0;
	vector<long long> count(k,0);
	for(int i=0;i<psum.size();i++)
		count[psum[i]]++;
	for(int i=0;i<k;i++)
		ret=(ret+((count[i]*(count[i]-1))/2))%mod;
	return ret;
}

int maxbuy(const vector<int> &psum,int k)
{
	vector<int> ret(psum.size(),0);
	vector<int> prev(k,-1);
	for(int i=0;i<psum.size();i++)
	{
		if(i>0)ret[i]=ret[i-1];
		else ret[i]=0;
		int loc=prev[psum[i]];
		if(loc!=-1)ret[i]=max(ret[i],ret[loc]+1);
		prev[psum[i]]=i;
	}
	return ret.back();
}

int main()
{
	int t,n,k;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		vector<int> v(n);
		for(int i=0;i<n;i++)
			cin>>v[i];
		vector<int> psum(n+1);
		psum[0]=0;
		for(int i=1;i<=n;i++)
			psum[i]=(psum[i-1]+v[i-1])%k;
		cout<<waystobuy(psum,k)<<" "<<maxbuy(psum,k)<<endl;
	}
	return 0;
}



#include<stdio.h>

#define FM(i,a,b) for(int i=a;i<b;i++) //(b-a) times a ~ b-1
#define LL long long

const int MAXN = 100000;
const int MAXK = 100000;

char buf[60* 10 * MAXN];
char *p = buf;

int scan_int()
{	
	int output = 0;	
	while (*p<'0' || *p>'9') 
		p++;	
	while (!(*p<'0' || *p>'9')) 
		output = output * 10 + *p++ - '0';	
	return output;
}

int main()
{
	int N, K, psum;
	bool already[MAXK];
	int how_many[MAXK];
	LL answer1, answer2;

	fread(buf, 60 * 10 * MAXN, 1, stdin);
	
	int T = scan_int();
	
	FM(n, 0, T)
	{
		N = scan_int(), K = scan_int();
		answer1 = 0, answer2 = 0, psum = 0;
		
		FM(i, 1, K) already[i] = false; 
		FM(i, 1, K) how_many[i] = 0;
		already[0] = true, how_many[0] = 1;
		//regard sum[nothing] as 0
		//init	
		FM(i, 0, N)
		{
			psum += scan_int();
			psum %= K;
			//psum=psum mod K
			
			how_many[psum]++;
			//count how many times 'psum' shows up for each value(0 ~ K-1)
			
			if (already[psum])
			{
				answer2++;
				FM(j, 0, K) already[j] = false;
			}
			already[psum] = true;
			//answer2++ as santa buys whenever he can 
		
		}
		
		FM(i, 0, K) 
			if (how_many[i] > 1) 
				answer1 += (LL)how_many[i] * (how_many[i] - 1) / 2;

		answer1 %= 20091101;
		//get answer1
		printf("%lld %lld\n", answer1, answer2);	
	}
	return 0;
}
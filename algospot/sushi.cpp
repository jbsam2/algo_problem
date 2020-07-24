#include <iostream>
#include <algorithm>
using namespace std;

int n,m,price[20],pref[20],cache[201];
int sushi()
{
	int ret=0;
	cache[0]=0;
	for(int budget=1;budget<=m;budget++)
	{
		int cand=0;
		for(int dish=0;dish<n;dish++)
			if(budget>=price[dish])
				cand=max(cand,cache[(budget-price[dish])%201]+pref[dish]);
		cache[budget%201]=cand;
		ret=max(ret,cand);
	}
	return ret;
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>n>>m;
		m/=100;
		for(int i=0;i<n;i++)
		{
			cin>>price[i]>>pref[i];
			price[i]/=100;
		}
		cout<<sushi()<<endl;
	}
	return 0;
}

#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int INF=3000;

int cost[21];
int pref[21];
int dp[3001]; 

int C,n,m;
//INF 범위 내의 dp값을 구해서 m 내에 최대한 많이 들어가도록 한다?
int main()
{
	scanf("%d",&C);
	while(C--)
	{
		memset(dp,0,sizeof(dp));

		scanf("%d%d",&n,&m);
		m/=100;

		for(int i=0;i<n;++i)
		{ 
		    scanf("%d%d",&cost[i],&pref[i]);
		    cost[i]/=100;
	    }
	    //dp[i] : 각 가격의 최대 선호도
	    int mm = min(m,INF);
		for(int i=0;i<=mm;++i) 
    		for(int j=0;j<n;++j)
    		{
    			if(i>=cost[j]) 
    			    dp[i]=max(dp[i],dp[i-cost[j]]+pref[j]);
    		}

        //m이 INF보다 같거나 작으면 문제 해결
		if(m<=INF)
		{
			printf("%d\n",dp[m]);
			continue;
		}

		int ans=0;
		//i는 100원부터 INF까지의 가격, dp 범위
		for(int i=1;i<=INF;++i)
		{
			int cnt=m/i;
			//i원이 예산 m 내에 몇번들어갈수 있나
			//cnt*dp[i]는 i원으로 얻을수 있는 최대 선호도를 m원 내에 가능한만큼 반복하는것
			//나머지값의 최대 선호도도 더해준다.
			ans=max(ans,cnt*dp[i]+dp[m-cnt*i]);
		}
		printf("%d\n",ans);
	}
} 
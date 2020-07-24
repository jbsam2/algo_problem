#include <iostream>
#include <cstring>
using namespace std;

const int MOD=1000000007;
int cache[101];

int tiling(int n)
{
	if(n<=1)return 1;
	int& ret=cache[n];
	if(ret!=-1)return ret;
	return ret=(tiling(n-1)+tiling(n-2))%MOD;
}
int asymmetric(int width)
{
	if(width%2==1)
		return (tiling(width)-tiling(width/2)+MOD)%MOD;
	int ret=tiling(width);
	ret=(ret-tiling(width/2)+MOD)%MOD;
	ret=(ret-tiling(width/2-1)+MOD)%MOD;
	return ret;
}
int main()
{
	int test,n;
	cin>>test;
	while(test--)
	{
		cin>>n;
		memset(cache,-1,sizeof(cache));
		cout<<asymmetric(n)<<endl<<endl;
	}
	return 0;
}

#include <iostream>
#include <cstring>
using namespace std;

int mem[101];
const int mod=1000000007;

int func(int n)
{
	if(n<=1) return 1;
	int &ret=mem[n];
	if(mem[n]!=-1)
		return ret;
	return ret=(func(n-2)+func(n-1))%mod;
}

int main()
{
	int t,n,ret;
	cin>>t;
	while(t--)
	{
		memset(mem,-1,sizeof(mem));
		cin>>n;
		if(n%2==1)
			ret=(func(n)-func(n/2)+mod)%mod;
		else
		{
			ret=(func(n)-func(n/2)+mod)%mod;
			ret=(ret-func((n/2)-1)+mod)%mod;
		}
		cout<<ret<<endl;
	}
	return 0;
}
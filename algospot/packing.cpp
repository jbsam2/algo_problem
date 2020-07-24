#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
using namespace std;

int n,cap,volume[100],need[100],cache[1001][100];
string name[100];

int pack(int cap,int item)
{
	if(item==n)return 0;
	int& ret=cache[cap][item];
	if(ret!=-1)return ret;
	ret=pack(cap,item+1);
	if(cap>=volume[item])
		ret=max(ret,pack(cap-volume[item],item+1)+need[item]);
	return ret;
}

void reconstruct(int cap,int item,vector<string> &picked)
{
	if(item==n)return;
	if(pack(cap,item)==pack(cap,item+1))
	{
		reconstruct(cap,item+1,picked);
	}
	else
	{
		picked.push_back(name[item]);
		reconstruct(cap-volume[item],item+1,picked);
	}
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		vector<string> picked;
		cin>>n>>cap;
		for(int i=0;i<n;i++)
			cin>>name[i]>>volume[i]>>need[i];
		memset(cache,-1,sizeof(cache));
		reconstruct(cap,0,picked);
		cout<<pack(cap,0)<<" "<<picked.size()<<endl;
		for(int i=0;i<picked.size();i++)
			cout<<picked[i]<<endl;
	}
	return 0;
}

#include <cstdio>
#define MAX(a,b) ((a) > (b) ? (a) : (b))

void print(int (*dp)[1001], int *vol, char (*item)[21], int n, int w, int cnt)
{
	if (n == 0)
	{
		printf("%d\n", cnt);
		return;
	}

	int f = dp[n][w] != dp[n - 1][w];
	print(dp, vol, item, n - 1, f ? w - vol[n] : w, cnt + f);

	if (dp[n][w] != dp[n - 1][w]) puts(item[n]);
}
int main()
{
	int c;
	scanf("%d", &c);

	while (c--)
	{
		int n, w;
		scanf("%d %d", &n, &w);

		char item[101][21];
		int vol[101], urgent[101];
		for (int i = 1; i <= n; ++i)
			scanf("%s %d %d", item[i], vol + i, urgent + i);
		
		int dp[101][1001]{};
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= w; ++j)
				dp[i][j] = MAX(dp[i - 1][j], j >= vol[i] ? dp[i - 1][j - vol[i]] + urgent[i] : 0);
		
		printf("%d ", dp[n][w]);
		print(dp, vol, item, n, w, 0);
	}

	return 0;
}
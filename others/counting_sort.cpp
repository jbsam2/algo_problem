#include <iostream>
using namespace std;

int cnt[6];
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int x;
		cin>>x;
		cnt[x]++;
	}
	for(int i=1;i<=n;i++)
	{
		while(cnt[i]--)
			cout<<i;
	}
	return 0;
}

#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

typedef pair<int,int> intpair;
vector<intpait> sort(vector<intpair> &v)
{
	int n=v.size(),i;
	vector<intpair> ans(n);
	vector<int> cnt(n+1,0);
	vector<int> idx(n,0);

	for(i=0;i<n;i++)
		cnt[v[i].second]++;
	for(i=1;i<=n;i++)
		cnt[i]+=cnt[i-1];
	for(i=n-1;i>=0;i--)
		idx[--cnt[v[i].second]]=i;

	cnt.clear();
	cnt.resize(n+1,0);
	for(i=0;i<n;i++)
		cnt[v[i].first]++;
	for(i=1;i<=n;i++)
		cnt[i]+=cnt[i-1];
	for(i=n-1;i>=0;i--)
		ans[--cnt[v[idx[i]].first]]=v[idx[i]];

	return ans;
}
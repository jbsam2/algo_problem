#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

struct Comparator
{
	const vector<int>& group;
	int t;
	Comparator(const vector<int>& _group,int _t):group(_group),t(_t)
	{}
	bool operator()(int a,int b)
	{
		if(group[a]!=group[b])return group[a]<group[b];
		return group[a+t]<group[b+t];
	}
};

vector<int> getsuffixarray(const string& s)
{
	int n=s.size();
	int t=1;
	vector<int> group(n+1);
	for(int i=0;i<n;i++)
		group[i]=s[i];
	group[n]=-1;
	vector<int> perm(n);
	for(int i=0;i<n;i++)
		perm[i]=i;
	while(t<n)
	{
		Comparator compareusing2t(group,t);
		sort(perm.begin(),perm.end(),compareusing2t);
		t*=2;
		if(t>=n)break;
		vector<int> newgroup(n+1);
		newgroup[n]=-1;
		newgroup[perm[0]]=0;
		for(int i=1;i<n;i++)
			if(compareusing2t(perm[i-1],perm[i]))
				newgroup[perm[i]]=newgroup[perm[i-1]]+1;
			else
				newgroup[perm[i]]=newgroup[perm[i-1]];
		group=newgroup;
	}
	return perm;
}

int commonprefix(const string& s,int i,int j)
{
	int k=0;
	while(i<s.size()&&j<s.size()&&s[i]==s[j])
	{
		i++;
		j++;
		k++;
	}
	return k;
}

int longestfrequent(int k,const string& s)
{
	vector<int> a=getsuffixarray(s);
	int ret=0;
	for(int i=0;i+k<=s.size();i++)
		ret=max(ret,commonprefix(s,a[i],a[i+k-1]));
	return ret;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int k;
		string s;
		cin>>k>>s;
		cout<<longestfrequent(k,s)<<endl;
	}
	return 0;
}
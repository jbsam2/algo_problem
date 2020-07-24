#include <iostream>
#include <vector>
using namespace std;

vector<int> partsum(const vector<int>& a)
{
	vector<int> ret(a.size());
	ret[0]=a[0];
	for(int i=1;i<a.size();i++)
		ret[i]=ret[i-1]+a[i];
	return ret;
}
vector<vector<int>> pivot(vector<vector<int>> a)
{
	vector<vector<int>> ret(a[0].size(),vector<int>(a.size()));
	for(int i=0;i<a[0].size();i++)
		for(int j=0;j<a.size();j++)
			ret[i][j]=a[j][i];
	return ret;
}

vector<vector<int>> arrpartsum(const vector<vector<int>>& a)
{
	vector<vector<int>> tmp1,tmp2,ret(a[0].size(),vector<int>(a.size()));
	for(int i=0;i<a.size();i++)
		ret[i]=partsum(a[i]);
	tmp1=pivot(ret);
	for(int i=0;i<a[0].size();i++)
		tmp2[i]=partsum(tmp1[i]);
	ret=pivot(tmp2);
	return ret;
}

int main()
{
	int n,m,s;
	cin>>n>>m;
	vector<vector<int>> get(n,vector<int>(m)),ret(n,vector<int>(m));
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
		{
			cin>>s;
			get.push_back(s);
		}
	ret=arrpartsum(get);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cout<<ret[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}
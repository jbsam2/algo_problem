#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n,e[10000],m[10000];
int heat()
{
	vector<pair<int,int>> order;
	for(int i=0;i<n;i++)
		order.push_back(make_pair(-e[i],i));
	sort(order.begin(),order.end());
	int ret=0,begineat=0;
	for(int i=0;i<n;i++)
	{
		int box=order[i].second;
		begineat+=m[box];
		ret=max(ret,begineat+e[box]);
	}
	return ret;
}
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>m[i];
		for(int i=0;i<n;i++)
			cin>>e[i];
		cout<<heat()<<endl;
	}
	return 0;
}
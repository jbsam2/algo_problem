#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int INT_MAX=numeric_limits<int>::max();

struct RMQ
{
	int n;
	vector<int> rangeMin;
	RMQ(const vector<int>& array)
	{
		n=array.size();
		rangeMin.resize(n*4);
		init(array,0,n-1,1);
	}
	int init(const vector<int>&array,int left,int right,int node)
	{
		if(left==right)
			return rangeMin[node]=array[left];
		int mid=(left+right)/2;
		int leftMin=init(array,left,mid,node*2);
		int rightMin=init(array,mid+1,right,node*2+1);
		return rangeMin[node]=min(leftMin,rightMin);
	}
	int query(int left,int right,int node,int nodeleft,int noderight)
	{
		if(right<nodeleft||noderight<left)return INT_MAX;
		if(left<=nodeleft&&noderight<=right)return rangeMin[node];
		int mid=(noderight+nodeleft)/2;
		return min(query(left,right,node*2,nodeleft,mid),query(left,right,node*2+1,mid+1,noderight));
	}
	int query(int left,int right)
	{
		return query(left,right,1,0,n-1);
	}
	int update(int index,int newValue,int node,int nodeleft,int noderight)
	{
		if(index<nodeleft||noderight<index)
			return rangeMin[node];
		if(nodeleft==noderight) return rangeMin[node]=newValue;
		int mid=(nodeleft+noderight)/2;
		return rangeMin[node]=min(update(index,newValue,node*2,nodeleft,mid),update(index,newValue,node*2+1,mid+1,noderight));
	}
	int update(int index,int newValue)
	{
		return update(index,newValue,1,0,n-1);
	}
};

int main()
{
	int t,n,q,h,i,start,finish,low,high;
	cin>>t;
	while(t--)
	{
		cin>>n>>q;
		vector<int> height;
		vector<int> minusheight;
		for(i=0;i<n;i++)
		{
			cin>>h;
			height.push_back(h);
			minusheight.push_back(-h);
		}
		RMQ rmq(height);
		RMQ minusrmq(minusheight);
		for(i=0;i<q;i++)
		{
			cin>>start>>finish;
			low=rmq.query(start,finish);
			high=abs(minusrmq.query(start,finish));
			cout<<high-low<<endl;
		}
	}
	return 0;
}
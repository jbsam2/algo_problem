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

const int MAX_N=100000;

vector<int> child[MAX_N];
int no2serial[MAX_N],serial2no[MAX_N];
int locintrip[MAX_N],depth[MAX_N];
int nextserial;

void traverse(int here,int d,vector<int>& trip)
{
	no2serial[here]=nextserial;
	serial2no[nextserial]=here;
	nextserial++;
	depth[here]=d;
	locintrip[here]=trip.size();
	trip.push_back(no2serial[here]);
	for(int i=0;i<child[here].size();i++)
	{
		traverse(child[here][i],d+1,trip);
		trip.push_back(no2serial[here]);
	}
}

RMQ* prepareRMQ()
{
	nextserial=0;
	vector<int> trip;
	traverse(0,0,trip);
	return new RMQ(trip);
}

int distance(RMQ *rmq,int u,int v)
{
	int lu=locintrip[u],lv=locintrip[v];
	if(lu>lv) swap(lu,lv);
	int lca=serial2no[rmq->query(lu,lv)];
	return depth[u]+depth[v]-2*depth[lca];
}

int main()
{
	int t,n,q,i,a,b,parent;
	cin>>t;
	while(t--)
	{
		for(i=0;i<MAX_N;i++)
			child[i].clear();
		cin>>n>>q;
		for(i=1;i<n;i++)
		{
			cin>>parent;
			child[parent].push_back(i);
		}
		nextserial=0;
		RMQ *pRmq=prepareRMQ();
		for(i=0;i<q;i++)
		{
			cin>>a>>b;
			cout<<distance(pRmq,a,b)<<endl;
		}
	}
	return 0;
}

#include<stdio.h>
int X[100000],Y[100000],Z[100000],c,N,Q,i,j,I,J;
main()
{
	for(scanf("%d",&c);c--;)
	{
		for(scanf("%d%d",&N,&Q),i=1;i<N;i++)
			scanf("%d",X+i);
		while(Q--)
		{
			scanf("%d%d",&I,&J);
			i=j=0;
			for(;I;I=X[I])
				Y[i++]=I;
			for(;J;J=X[J])
				Z[j++]=J;
			for(;i&&j&&Y[i-1]==Z[j-1];i--,j--);
			printf("%d\n",i+j);
		}
	}
}
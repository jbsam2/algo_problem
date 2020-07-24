#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>
using namespace std;

const int MOD=20090711;

struct RNG
{
	int seed,a,b;
	RNG(int _a,int _b):a(_a),b(_b),seed(1983){}
	int next()
	{
		int ret=seed;
		seed=((seed*(long long)a)+b)%MOD;
		return ret;
	}
};

int runningmedian(int n,RNG rng)
{
	priority_queue<int,vector<int>,less<int>>maxheap;
	priority_queue<int,vector<int>,greater<int>>minheap;
	int ret=0;
	for(int cnt=1;cnt<=n;cnt++)
	{
		if(maxheap.size()==minheap.size())
			maxheap.push(rng.next());
		else
			minheap.push(rng.next());
		if(!minheap.empty()&&!maxheap.empty()&&minheap.top()<maxheap.top())
		{
			int a=maxheap.top(),b=minheap.top();
			maxheap.pop();
			minheap.pop();
			maxheap.push(b);
			minheap.push(a);
		}
		ret=(ret+maxheap.top())%MOD;
	}
	return ret;
}

int main()
{
	int t,n,a,b;
	cin>>t;
	while(t--)
	{
		cin>>n>>a>>b;
		RNG generator(a,b);
		cout<<runningmedian(n,generator)<<endl;
	}
	return 0;
}

void push_heap(vector<int>& heap,int newvalue)
{
	heap.push_back(newvalue);
	int idx=heap.size()-1;
	while(idx>0&&heap[(idx-1)/2]<heap[idx])
	{
		swap(heap[idx],heap[(idx-1)/2]);
		idx=(idx-1)/2;
	}
}

void pop_heap(vector<int>& heap)
{
	heap[0]=heap.back();
	heap.pop_back();
	int here=0;
	while(1)
	{
		int left=here*2+1,right=here*2+2;
		if(left>=heap.size())break;
		int next=here;
		if(heap[next]<heap[left])
			next=left;
		if(right<heap.size()&&heap[next]<heap[right])
			next=right;
		if(next==here)break;
		swap(heap[here],heap[next]);
		here=next;
	}
}
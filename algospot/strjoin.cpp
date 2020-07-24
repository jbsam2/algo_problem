#include <iostream>
#include <vector>
#include <functional>
#include <queue>
using namespace std;

int concat(const vector<int>& lengths)
{
	priority_queue<int,vector<int>,greater<int>>pq;
	for(int i=0;i<lengths.size();i++)
		pq.push(lengths[i]);
	int ret=0;
	while(pq.size()>1)
	{
		int min1=pq.top();pq.pop();
		int min2=pq.top();pq.pop();
		pq.push(min1+min2);
		ret+=min1+min2;
	}
	return ret;
}

int main()
{
	int test,n,l;
	cin>>test;
	while(test--)
	{
		cin>>n;
		vector<int> lengths;
		for(int i=0;i<n;i++)
		{
			cin>>l;
			lengths.push_back(l);
		}
		cout<<concat(lengths)<<endl;
	}
	return 0;
}

#include<ios>
#include<set>
int n,i;
int main()
{
	for(scanf("%*d");~scanf("%d",&n);)
		{
			std::multiset<int>s;
			for(;n--;s.insert(i))
				scanf("%d",&i);
			for(i=0;s.size()>1;s.insert(n))
				{
					auto p=s.begin();
					n=*p;
					p=s.erase(p);
					n+=*p;
					i+=n;
					s.erase(p);
				}
			printf("%d\n",i);
		}
}
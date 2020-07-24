#include <iostream>
#include <queue>
using namespace std;

const int MOD=10000;

struct RNG
{
	unsigned seed;
	RNG():seed(1983){}
	unsigned next()
	{
		unsigned ret=seed;
		seed=((seed*214013u)+2531011u);
		return ret%MOD+1;
	}
};

int countranges(int k,int n)
{
	RNG rng;
	queue<int> range;
	int ret=0,rangesum=0;
	for(int i=0;i<n;i++)
	{
		int newsignal=rng.next();
		rangesum+=newsignal;
		range.push(newsignal);
		while(rangesum>k)
		{
			rangesum-=range.front();
			range.pop();
		}
		if(rangesum==k)ret++;
	}
	return ret;
}

int main()
{
	int c,n,k;
	cin>>c;
	while(c--)
	{
		cin>>k>>n;
		cout<<countranges(k,n)<<endl;
	}
	return 0;
}
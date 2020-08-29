#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

bool cmp(pair<int,int> p1,pair<int,int> p2)
{
	return p1.second<p2.second;
}

int solution(vector<int> food_times, long long k)
{
    k++;
    int size=food_times.size();

    vector<pair<int,int>> v;
    for(int i=0;i<size;i++)
    	v.push_back(make_pair(food_times[i],i+1));

    sort(v.begin(),v.end());

    for(int i=0;i<size;i++)
    {
    	long long x=size-i;
    	if(i!=0)
    		x*=v[i].first-v[i-1].first;
    	else
    		x*=v[i].first;
    	if(x>=k)
    	{
    		sort(v.begin()+i,v.end(),cmp);
    		if(k%(size-i)==0)
    			return v[size-1].second;
    		else
    			return v[i+(k%(size-i))-1].second;
    	}
    	else
    		k-=x;
    }
    return -1;
}
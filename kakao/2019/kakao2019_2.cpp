#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const pair<double,int>&a,const pair<double,int>&b)
{
	if(a.first==b.first) return a.second<b.second;
	return a.first>b.first;
}

vector<int> solution(int N, vector<int> stages)
{
    vector<int> answer;
    vector<pair<double,int>> ret;
    int size=stages.size();
    for(int i=1;i<=N;i++)
    {
    	double cnt=0,fail=0;
    	for(int j=0;j<size;j++)
    	{
    		if(stages[j]>=i)
    			cnt++;
    		if(stages[j]==i)
    			fail++;
    	}
    	if(cnt!=0)
    		ret.push_back(make_pair(fail/cnt,i));
    	else if(cnt==0)
    		ret.push_back(make_pair(0,i));
    }
    sort(ret.begin(),ret.end(),cmp);
    for(int i=0;i<N;i++)
    	answer.push_back(ret[i].second);
    return answer;
}
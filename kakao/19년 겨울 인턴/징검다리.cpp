#include <string>
#include <vector>
using namespace std;

bool possi(int n,vector<int> stones,int k)
{
    int cnt=0;
    for(int i=0;i<stones.size();i++)
    {
        if(stones[i]<=n)
            cnt++;
        else
            cnt=0;
        if(cnt>=k)
            return false;
    }
    return true;
}

int solution(vector<int> stones,int k)
{
    int hi=200000000;
    int lo=0;
    while(lo<=hi)
    {
        int mid=(hi+lo)/2;
        if(possi(mid,stones,k))
            lo=mid+1;
        else
            hi=mid-1;
    }
    return lo;
}
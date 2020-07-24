#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> nextweak(vector<int> weak,int start,int n)
{
    vector<int> ret;
    for(int i=start;i<weak.size();i++)
        ret.push_back(weak[i]);
    for(int i=0;i<start;i++)
        ret.push_back(weak[i]+n);
    return ret;
}

int solution(int n, vector<int> weak, vector<int> dist)
{
    int answer=1<<30;
    sort(dist.begin(),dist.end());
    do
    {
        for(int i=0;i<weak.size();i++)
        {
            vector<int> new_weak=nextweak(weak,i,n);
            int idx=0;
            int cur=new_weak[0]+dist[idx];
            bool chk=true;
            
            for(int j=1;j<new_weak.size();j++)
            {
                if(new_weak[j]>cur)
                {
                    if(idx+1==dist.size())
                    {
                        chk=false;
                        break;
                    }
                    cur=new_weak[j]+dist[++idx];
                }
            }
            if(chk)answer=min(answer,idx+1);
        }
    }while(next_permutation(dist.begin(),dist.end()));
    return answer==1<<30?-1:answer;
}
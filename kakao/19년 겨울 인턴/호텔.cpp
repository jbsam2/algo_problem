#include <bits/stdc++.h>
using namespace std;

map<long long,long long> m;

long long find(long long x)
{
    if(!m[x])return x;
    else
    {
        m[x]=find(m[x]);
        return m[x];
    }
}

vector<long long> solution(long long k, vector<long long> room_number)
{
    vector<long long> answer;
    for(long long x:room_number)
    {
        long long y=find(x);
        answer.push_back(y);
        m[y]=y+1;
    }
    return answer;
}




#include <bits/stdc++.h>
using namespace std;

vector<long long> solution(long long k,vector<long long> room_number)
{
    vector<long long> answer;
    map<long long,long long> room_dic;
    for(auto i:room_number)
    {
        long long n=i;
        vector<long long> visit;
        visit.push_back(n);
        while(room_dic[n])
        {
            n=room_dic[n];
            visit.push_back(n);
        }
        answer.push_back(n);
        for(auto j:visit)
            room_dic[j]=n+1;
    }
    return answer;
}
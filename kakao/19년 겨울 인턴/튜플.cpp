#include <bits/stdc++.h>
using namespace std;

vector<int> solution(string s)
{
    int st[100001]={};
    vector<int> answer;
    string tmp;
    for(char i:s)
    {
        if(i-'0'>=0&&i-'0'<=9)
        {
            tmp+=i;
        }
        else
        {
            if(tmp.length())
                st[stoi(tmp)]++,tmp.clear();
        }
    }
    vector<pair<int,int>> v;

    for(int i=0;i<100001;i++)
        if(st[i])
            v.push_back({st[i],i});
    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());
    for(auto i:v)answer.push_back(i.second);
    return answer;
}
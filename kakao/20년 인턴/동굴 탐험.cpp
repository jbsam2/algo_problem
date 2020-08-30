#include <bits/stdc++.h>
using namespace std;

bool visited[200000];
int before[200000],wait[200000];
vector<int> edge[200000];

void visit(int num)
{
    if(visited[num])return;
    if(!visited[before[num]]){wait[before[num]]=num;return;}
    visited[num]=1;visit(wait[num]);
    for(int n:edge[num])visit(n);
}

bool solution(int n,vector<vector<int>> path,vector<vector<int>> order)
{
    for(auto i:path)edge[i[0]].push_back(i[1]),edge[i[1]].push_back(i[0]);
    for(auto i:order)before[i[1]]=i[0];
    if(before[0])return false;
    visited[0]=1;
    for(int i:edge[0])visit(i);
    for(int i=0;i<n;i++)if(!visited[i])return false;
    return true;
}
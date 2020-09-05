#include <string>
#include <vector>
using namespace std;

int wait[200000],before[200000];
bool visit[200000];
vector<int> connect[200000];

void find(int num)
{
    if (visit[num])return;
    if(!visit[before[num]]){wait[before[num]]=num;return;}
    visit[num]=1;find(wait[num]);
    for(int i:connect[num])find(i);
}

bool solution(int n, vector<vector<int>> path, vector<vector<int>> order) {
    for(auto i:path)connect[i[0]].push_back(i[1]),connect[i[1]].push_back(i[0]);
    for(auto i:order)before[i[1]]=i[0];
    if(before[0])return false;
    visit[0]=1;
    for(int i:connect[0])find(i);
    for(int i=0;i<n;i++)if(!visit[i])return false;
    return true;
}
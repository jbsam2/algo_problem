#include <string>
#include <vector>
#include <set>
using namespace std;

bool check[9];
int answer=0;
set<string> Set;

bool possible(string a,string b)
{
    if(a.size()!=b.size()) return false;
    for(int i=0;i<a.size();i++)
        if(a[i]!=b[i]&&b[i]!='*')
            return false;
    return true;
}

void combi(int n,vector<string> user_id, vector<string> banned_id)
{
    if(n==banned_id.size())
    {
        string tmp="";
        for(int i=0;i<user_id.size();i++)
            if(check[i])
                tmp+=(i+'0');
        if(Set.find(tmp)!=Set.end())
            return;
        Set.insert(tmp);
        answer++;
        return;
    }
    for(int i=0;i<user_id.size();i++)
        if(!check[i]&&possible(user_id[i],banned_id[n]))
        {
            check[i]=true;
            combi(n+1,user_id,banned_id);
            check[i]=false;
        }
}

int solution(vector<string> user_id, vector<string> banned_id)
{
    combi(0,user_id,banned_id);
    return answer;
}
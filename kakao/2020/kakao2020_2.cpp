#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool correct(string p)
{
    int cnt=0;
    for(int i=0;i<p.size();i++)
    {
        if(p[i]=='(')
            cnt++;
        else
        {
            if(!cnt) return false;
            cnt--;
        }
    }
    return true;
}

string solution(string p)
{
    string u,v;
    int rcnt=0,lcnt=0;
    if(p=="") return p;
    for(int i=0;i<p.size();i++)
    {
        if(p[i]=='(') lcnt++;
        else rcnt++;
        if(rcnt==lcnt)
        {
            u=p.substr(0,i+1);
            v=p.substr(i+1);
            break;
        }
    }
    if(correct(u)) return u+solution(v);
    else
    {
        string answer = "";
        answer+="("+solution(v)+")";
        string reversed=u.substr(1,u.length()-2);
        for(int i=0;i<reversed.size();i++)
        {
            if(reversed[i]=='(') answer+=")";
            else answer+="(";
        }
        return answer;
    }
}
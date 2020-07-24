#include <iostream>
#include <cstring>
using namespace std; 

int total;
bool areFriends[10][10];

int countPairings(bool taken[10])
{
    int firstStudent=-1;
    for (int i=0;i<total;i++)
    {
        if(!taken[i])
        {
            firstStudent=i;
            break;
        }
    }
    if(firstStudent==-1)
        return 1;
    int ret=0;
    for(int i=firstStudent+1;i<total;i++)
    {
        if(!taken[i]&&areFriends[firstStudent][i])
        {
            taken[firstStudent]=taken[i]=true;
            ret+=countPairings(taken);
            taken[firstStudent]=taken[i]=false;
        }
    }
    return ret;
}
int main()
{
    int t,pair,s1,s2;
    bool taken[10];
    cin>>t;
    while(t--)
    {
        cin>>total>>pair;
        memset(areFriends,false,sizeof(areFriends));
        memset(taken,false,sizeof(taken));
        for(int j=0;j<pair;j++)
        {
            cin>>s1>>s2;
            areFriends[s1][s2]=areFriends[s2][s1]=true;
        }
        cout<<countPairings(taken)<<endl;
    }
    return 0;
}
#include <iostream>
using namespace std;
int main()
{
    int t,n,c,r,m,i,p;cin>>t;
    for(c=1;c<=t;c++)
    {
        r=0,m=1<<30;cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>p;
            if(abs(p)<m)m=abs(p),r=1;
            else if (abs(p)==m)r++;
        }
        printf("#%d %d %d\n",c,m,r);
    }
}
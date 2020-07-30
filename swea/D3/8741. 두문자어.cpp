#include <string>
#include <iostream>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        string tmp1,tmp2,tmp3;
        cin>>tmp1>>tmp2>>tmp3;
        printf("#%d %c%c%c\n", t,tmp1[0]-32,tmp2[0]-32,tmp3[0]-32);
    }
}
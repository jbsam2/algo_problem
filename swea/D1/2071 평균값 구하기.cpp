#include<iostream>
#include<cmath>
 
using namespace std;
 
int main(int argc, char** argv)
{
    int test_case;
    int T;
 
    cin>>T;
 
    for(test_case = 1; test_case <= T; ++test_case)
    {
        float arr[10], ans = 0;
        for(int i=0;i<10;i++)
        {
            cin>>arr[i];
            ans += arr[i];
        }
        int avg = round(ans/10);
        printf("#%d %d\n",test_case,avg);
    }
    return 0;
}
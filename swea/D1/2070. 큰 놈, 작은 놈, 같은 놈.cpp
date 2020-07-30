#include<iostream>
 
using namespace std;
 
int main(int argc, char** argv)
{
    int test_case;
    int T;
 
    cin>>T;
     
    for(test_case = 1; test_case <= T; ++test_case)
    {
        int a,b;
        char c;
        cin>>a>>b;
        if(a>b)
            c='>';
        else if(a==b)
            c='=';
        else
            c='<';
        printf("#%d %c\n",test_case,c);
    }
    return 0;
}
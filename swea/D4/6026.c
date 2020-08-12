#include <stdio.h>
#include <memory.h>
#define MOD 1000000007
int N, M, choose[100];
long answer, pactorial[101], LOOKUP_TABLE[100][100][2];
long pow(long x,int n)
{
    long ret = 1;
    while(n)
    {
        if(n&1)
            ret = (ret*x)%MOD;
        x = (x*x)%MOD;
        n>>=1;
    }
    return ret;
}
void DFS(int setting, int left)
{
    if((N-setting)==left)
        answer = (answer + pactorial[left])%MOD;
    else if(!left)
        answer = (answer + pow(M,N-setting))%MOD;
    else
    {
        for (int i = 0; i < M; i++)
        {
            if (choose[i])
            {
                if (LOOKUP_TABLE[setting][left][0] == -1)
                {
                    LOOKUP_TABLE[setting][left][0] = answer;
                    choose[i] = 0;
                    DFS(setting + 1, left - 1);
                    LOOKUP_TABLE[setting][left][0] = (answer - LOOKUP_TABLE[setting][left][0] + MOD) % MOD;
                    choose[i] = 1;
                }
                else answer = (answer + LOOKUP_TABLE[setting][left][0]) % MOD;
            }
            else
            {
                if (LOOKUP_TABLE[setting][left][1] == -1)
                {
                    LOOKUP_TABLE[setting][left][1] = answer;
                    DFS(setting + 1, left);
                    LOOKUP_TABLE[setting][left][1] = (answer - LOOKUP_TABLE[setting][left][1] + MOD) % MOD;
                }
                else answer = (answer + LOOKUP_TABLE[setting][left][1]) % MOD;
            }
        }
    }
}

int main(int argc, char** argv)
{
    int T, tc;
    memset(choose, 1, sizeof(choose));
    choose[0] = 0;
    scanf("%d", &T);
    pactorial[1] = 1;
    for (int i = 2; i <= 100; i++) pactorial[i] = (pactorial[i - 1] * i) % MOD;
    for(tc = 1; tc<=T;tc++)
    {
        scanf("%d %d", &M, &N);
        if(M==N) printf("#%d %d\n",tc,pactorial[M]);
        else
        {
            answer = 0;
            memset(LOOKUP_TABLE,-1,sizeof(LOOKUP_TABLE));
            DFS(1, M-1 );
            printf("#%d %d\n", tc,(answer*M)%MOD);
        }
    }
    return 0;
}
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const long long NEGINF=numeric_limits<long long>::min();
int n,m,A[100],B[100];
int cache[101][101];

int jlis(int indexA,int indexB)
{
        int &ret=cache[indexA+1][indexB+1];
        if(ret!=-1)return ret;

        ret=0;
        long long a=(indexA==-1?NEGINF:A[indexA]);
        long long b=(indexB==-1?NEGINF:B[indexB]);
        long long maxElement=max(a,b);
        for(int nextA=indexA+1;nextA<n;nextA++)
                if(maxElement<A[nextA])
                        ret=max(ret,jlis(nextA,indexB)+1);
        for(int nextB=indexB+1;nextB<m;nextB++)
                if(maxElement<B[nextB])
                        ret=max(ret,jlis(indexA,nextB)+1);
        return ret;
}

int main(void)
{
        int test;
        cin>>test;
        while(test--)
        {
                memset(cache,-1,sizeof(cache));
                cin>>n>>m;
                for(int i=0;i<n;i++)
                        cin>>A[i];
                for(int i=0;i<m;i++)
                        cin>>B[i];
                cout<<jlis(-1,-1)<<endl<<endl;
        }
        return 0;
}


#include <iostream>
#include <cstring>
using namespace std;
#define FOR(v,n,l) for (int v=n;v<l;v++)

int dp[110][110],A[110],B[110],la,lb,t;

int req(int a,int b,int last){
        int& ret = dp[a][b];
        if (ret!=-1) return ret;
        ret = 0;
        FOR(i,a,la) if (A[i]>last || a+b==0) ret=max(ret,1+req(i+1,b,A[i]));
        FOR(i,b,lb) if (B[i]>last || a+b==0) ret=max(ret,1+req(a,i+1,B[i]));
        return ret;
}

int main(){
        scanf("%d",&t);
        while(t--){
                scanf("%d %d",&la,&lb);
                FOR(i,0,la) scanf("%d",&A[i]);
                FOR(i,0,lb) scanf("%d",&B[i]);
                memset(dp,-1,sizeof(dp));
                printf("%d\n\n",req(0,0,0));
        }
        return 0;
}
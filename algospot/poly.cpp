#include <iostream>
#include <cstring>
using namespace std;
const int MOD=10000000;
int cache[101][101];
int poly(int n,int first)
{
	if(n==first)return 1;
	int& ret=cache[n][first];
	if(ret!=-1)return ret;
	ret=0;
	for(int second=1;second<=n-first;second++)
	{
		int add=second+first-1;
		add*=poly(n-first,second);
		add%=MOD;
		ret+=add;
		ret%=MOD;
	}
	return ret;
}
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		int block,sum=0;
		cin>>block;
		memset(cache,-1,sizeof(cache));
		for(int i=1;i<=block;i++)
		{
			sum+=poly(block,i);
			sum%=MOD;
		}
		cout<<sum<<endl<<endl;
	}
}

#include<stdio.h>
int main()
{
    int arr[100]={1,2,6},i,cnum,add1,add2;
	for(i=3,add1=1,add2=3;i<100;i++)
	{
		arr[i]=(arr[i-1]*3+add1)%10000000;
		add1=(add1+add2)%10000000;
		add2=(add2+arr[i-1])%10000000;
	}
	scanf("%d",&cnum);
	for(;cnum>0;cnum--)
	{
		scanf("%d",&i);
		printf("%d\n",arr[i-1]);
	}
	return 0;
}
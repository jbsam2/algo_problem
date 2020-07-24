#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

const int M=1000000000+100;
int bino[201][201],skip;

void calcbino()
{
	memset(bino,0,sizeof(bino));
	for(int i=0;i<=200;i++)
	{
		bino[i][0]=bino[i][i]=1;
		for(int j=1;j<i;j++)
			bino[i][j]=min(M,bino[i-1][j-1]+bino[i-1][j]);
	}
}

string kth(int n,int m,int skip)
{
	if(n==0)return string(m,'o');
	if(skip<bino[n+m-1][n-1])return "-"+kth(n-1,m,skip);
	return "o"+kth(n,m-1,skip-bino[n+m-1][n-1]);
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		int c,p;
		//string ret;
		cin>>c>>p>>skip;
		calcbino();
		skip--;
		cout<<kth(c,p,skip)<<endl;
	}
	return 0;
}

#include <stdio.h>
typedef unsigned long long int u64;
int C,O,D,K;
u64 cm[210][110];
u64 c(int n,int m)
{
	if(cm[n][m]) return cm[n][m];
	return cm[n][m]=(!m||n==m)?1:c(n-1,m-1)+c(n-1,m);
}

void f(int d,int o,u64 k)
{
	if(!d||!o)for(int i=0;i<(d>o?d:o);++i)printf(d?"-":"o");
	else {
		u64 dn=c(o+d-1,d-1);
		if(k<=dn) printf("-"),f(d-1,o,k);
		else printf("o"),f(d,o-1,k-dn);}
}

int main() {
	scanf("%d",&C);
	while(C--) scanf("%d%d%d",&D,&O,&K),f(D,O,K),printf("\n");
}
#include <iostream>
using namespace std;
long long l=2000000000;

int need(long long game,long long win)
{
	if((win*100/game)==(win+l)*100/(game+l))return -1;
	long long lo=0,hi=l;
	while(lo+1<hi)
	{
		long long m=(lo+hi)/2;
		if((win*100/game)==(win+m)*100/(game+m))lo=m;
		else hi=m;
	}
	return hi;
}
int main()
{
	int t;
	long long n,win;
	cin>>t;
	while(t--)
	{
		cin>>n>>win;
		cout<<need(n,win)<<endl<<endl;
	}
	return 0;
}

#include<ios>
int main(){int n,m,q;for(scanf("%*d");~scanf("%d%d",&n,&m);printf("%d\n",q>0?(q-q*n+100*(n-m)-1)/q:-1))q=99-int(m*100.L/n);}

#include <stdio.h>

int main()
{
	int T,N,M,Z;
	for(scanf("%d", &T); T--;)
	{
		scanf("%d%d", &N,&M);
		Z=M*100LL/N+1;
		printf("%d\n",(Z>99)?-1:((N*Z-M*100+(99-Z))/(100-Z)));
	}
}

#include <ios>
int main(){int n,m,q;for(scanf("%*d");~scanf("%d%d",&n,&m);printf("%d ",q>99?-1:((n*q-m*100+99-q)/(100-q))))q=m*100L/n+1;}

main(n,m,q){for(scanf("%*d");~scanf("%d%d",&n,&m);printf("%d ",q>99?-1:((n*q-m*100+99-q)/(100-q))))q=m*100L/n+1;}
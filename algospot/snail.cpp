#include<iostream>
using namespace std;

const int MAX=1000;
int n,m;
double cache[MAX][2*MAX+1];

double climb(int days,int climbed)
{
	if(days==m)return climbed>=n?1:0;
	double& ret=cache[days][climbed];
	if(ret!=-1.0)
		return ret;
	return ret=(0.25*climb(days+1,climbed+1)+0.75*climb(days+1,climbed+2));
}
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>n>>m;
		for(int i=0;i<1000;i++)
			for(int j=0;j<2001;j++)
				cache[i][j]=-1.0;
		cout.precision(11);
		cout<<climb(0,0)<<endl<<endl;
	}
}

#include <stdio.h>
#include <math.h>

int C,N,M;

int main()
{
	scanf("%d",&C);
	while(C--)
	{
		scanf("%d%d",&N,&M);
		double sk=pow(0.75,M),r=0;
		for(int k=0;k<=M;++k)
		{
			if(2*M-k>=N)r+=sk,sk*=(M-k)/(k+1.)/3;
			else break;
		}
		printf("%.13f\n",r);}
}
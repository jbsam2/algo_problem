#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

const int M=10000000;

int minfactor[M+1],minfactorpower[M+1],factors[M+1];

void prime()
{
	minfactor[0]=minfactor[1]=-1;
	for(int i=2;i<=M;i++)
		minfactor[i]=i;
	int sn=int(sqrt(M));
	for(int i=2;i<=sn;i++)
		if(minfactor[i]==i)
			for(int j=i*i;j<=M;j+=i)
				if(minfactor[j]==j)
					minfactor[j]=i;
}

void getfactor()
{
	factors[1]=1;
	for(int n=2;n<=M;n++)
	{
		if(minfactor[n]==n)
		{
			minfactorpower[n]=1;
			factors[n]=2;
		}
		else
		{
			int p=minfactor[n];
			int m=n/p;
			if(p!=minfactor[m])
				minfactorpower[n]=1;
			else
				minfactorpower[n]=minfactorpower[m]+1;
			int a=minfactorpower[n];
			factors[n]=(factors[m]/a)*(a+1);
		}
	}
}

int main()
{
	int t,d,l,h;
	cin>>t;
	prime();
	getfactor();
	while(t--)
	{
		cin>>d>>l>>h;
		int ret=0;
		for(int i=l;i<=h;i++)
			if(factors[i]==d)
				ret++;
		cout<<ret<<endl;
	}
	return 0;
}

#include <ios>
#define O 10000001
int C,N,L,M,B,i,j,A[O];
int main()
{
	for(i=1;i<O;i++)
		for(j=i;j<O;j+=i)
			A[j]++;
	scanf("%d",&C);
	while(C--)
		{
			scanf("%d%d%d",&N,&L,&M);
			B=0;
			for(i=L;i<=M;i++)
				if(N==A[i])
					B++;
			printf("%d\n",B);
		}
}
#include <iomanip>
#include <iostream>
using namespace std;

double balance(double amount,int duration,double rates,double monthlypay)
{
	double balance=amount;
	while(duration--)
	{
		balance*=(1.0+rates/12.0/100.0);
		balance-=monthlypay;
	}
	return balance;
}

double payment(double amount,int duration,double rates)
{
	double lo=0,hi=amount*(1.0+rates/12.0/100.0);
	for(int i=0;i<100;i++)
	{
		double m=(lo+hi)/2.0;
		if(balance(amount,duration,rates,m)<=0)hi=m;
		else lo=m;
	}
	return hi;
}

int main()
{
	int t,month;
	double n,rate;
	cin>>t;
	while(t--)
	{
		cin>>n>>month>>rate;
		cout<<fixed<<setprecision(10);
		cout<<payment(n,month,rate)<<endl<<endl;
	}
	return 0;
}

#include<iostream>
#include<cmath>
int main()
{
	int t;
	std::cin>>t;
	while(t--)
		{
			double m,n,p,a;
			std::cin>>n>>m>>p;
			p=1+p/12*0.01;
			a=pow(p,m);
			printf("%.10f\n",n*a*(1-p)/(1-a));
		}
}
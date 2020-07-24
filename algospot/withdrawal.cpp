#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

int n,k,c[1000],r[1000];

bool decision(double x)
{
	vector<double> v;
	for(int i=0;i<n;i++)
		v.push_back(x*c[i]-r[i]);
	sort(v.begin(),v.end());
	double sum=0;
	for(int i=n-k;i<n;i++)
		sum+=v[i];
	return sum>=0;
}

double opt()
{
	double lo=-1e-9,hi=1;
	for(int i=0;i<100;i++)
	{
		double mid=(lo+hi)/2.0;
		if(decision(mid))hi=mid;
		else lo=mid;
	}
	return hi;
}

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		for(int i=0;i<n;i++)
			cin>>r[i]>>c[i];
		cout<<fixed<<setprecision(10);
		cout<<opt()<<endl<<endl;
	}
	return 0;
}
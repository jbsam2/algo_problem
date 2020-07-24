#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <cmath>
using namespace std;

const double L=25;

vector<double> differentiate(const vector<double>& poly)
{
	int n=poly.size()-1;
	vector<double> ret;
	for(int i=0;i<n;i++)
		ret.push_back((n-i)*poly[i]);
	return ret;
}

vector<double> solvenaive(const vector<double>& poly)
{
	int n=poly.size()-1;
	vector<double> ret;
	switch(n)
	{
		case 1:
		ret.push_back(-poly[1]/poly[0]);
		break;
		case 2:
		double a=poly[0],b=poly[1],c=poly[2];
		ret.push_back((-b+sqrt(b*b-4*a*c))/(2*a));
		ret.push_back((-b-sqrt(b*b-4*a*c))/(2*a));
		break;
	}
	sort(ret.begin(),ret.end());
	return ret;
}

double evaluate(const vector<double>& poly,double x)
{
	int n=poly.size()-1;
	double ret=0;
	for(int i=0;i<=n;i++)
		ret+=pow(x,n-i)*poly[i];
	return ret;
}

vector<double> solve(const vector<double>& poly)
{
	int n=poly.size()-1;
	if(n<=2)return solvenaive(poly);
	vector<double> derivative=differentiate(poly);
	vector<double> sols=solve(derivative);
	sols.insert(sols.begin(),-L-1);
	sols.insert(sols.end(),L+1);
	vector<double> ret;
	for(int i=0;i+1<sols.size();i++)
	{
		double x1=sols[i],x2=sols[i+1];
		double y1=evaluate(poly,x1),y2=evaluate(poly,x2);
		if(y1*y2>0)continue;
		if(y1>y2){swap(y1,y2);swap(x1,x2);}
		for(int i=0;i<100;i++)
		{
			double mx=(x1+x2)/2;
			double my=evaluate(poly,mx);
			if(y1*my>0){y1=my;x1=mx;}
			else {y2=my;x2=mx;}
		}
		ret.push_back((x1+x2)/2);
	}
	sort(ret.begin(),ret.end());
	return ret;
}

int main()
{
	int t,n;
	cin>>t;
	while(t--)
	{
		vector<double> poly;
		cin>>n;
		for(int i=0;i<=n;i++)
		{
			double p;
			cin>>p;
			poly.push_back(p);
		}
		vector<double> ret=solve(poly);
		cout<<fixed<<setprecision(12);
		for(int i=0;i<ret.size();i++)
			cout<<ret[i]<<" ";
		cout<<endl<<endl;
	}
	return 0;
}

#include <iostream>
#include <cmath>

using namespace std;

int main()
{	
	int c;
	cin >> c;
	while (c--)
	{
		int n;
		cin >> n;
		double* arr = new double[n + 1];
		double* diffarr = new double[n];

		for (int i = 0; i < n + 1; i++)
			cin >> arr[i];
		for (int i = 0; i < n; i++)
			diffarr[i] = arr[i] * (n - i);		
		
		double a;
		double b;
		double c;
		double diff;
		
		while (n)
		{
			a = -10;
			diff = -20;

			while (diff < -0.000000001)
			{

				b = 0;
				c = 0;
				for (int i = 0; i < n + 1; i++)
					b += arr[i] * pow(a, n - i);
				for (int i = 0; i < n; i++)
					c += diffarr[i] * pow(a, n - i - 1);

				diff = b / c;
				
				a = a - b / c;
				
			}
			cout.precision(10);
			cout << a << " ";
			
			for (int i = 1; i < n; i++)
				arr[i] = arr[i] + arr[i - 1] * a;
			n--;
			for (int i = 0; i < n; i++)
				diffarr[i] = arr[i] * (n - i);
		}
		cout << endl;
	}
	system("pause");
}



#include<stdio.h>
#include<algorithm>
#include<queue>

using namespace std;

double nums[6][6];
double res[6][6];
int alen;
int n;
int rlen;

double f(int d, double x)
{
	double ret = 0;
	for (int i = 0; i < d; ++i)
	{
		double temp = 1;
		for (int j = 0; j < d - i; ++j)
		{
			temp *= x;
		}
		ret += temp * nums[d][i];
	}
	ret += nums[d][d];
	return ret;
}

bool decision(int d, double a)
{
	return f(d,a)*f(d-1,a) < 0;
}

double bs(int d,double s, double e)
{
	double m;
	int cnt = 100;
	while (cnt--)
	{
		m = (s + e) / 2;
		if (decision(d,m))
		{
			s = m;
		}
		else e = m;
	}
	return m;
}
int main()
{
	int tc;
	scanf("%d", &tc);
	while (tc--)
	{
		rlen = 0;
		scanf("%d", &n);
		for (int i = 0; i < n+1; ++i)
		{
			scanf("%lf", &nums[n][i]);
		}

		for (int i = n - 1; i>=0; --i)
		{
			for (int j = 0; j < i+1; ++j)
			{
				nums[i][j] = nums[i + 1][j] * (i+1 - j);
			}
		}

		for (int i = 1; i <= n; ++i)
		{
			res[i-1][0] = -10;
			res[i-1][i] = 10;
			for (int j = 1; j <= i; ++j)
			{
				res[i][j] = bs(i, res[i - 1][j-1], res[i - 1][j]);
			}
		}

		for (int i = 1; i <=n ; ++i)
			printf("%.10lf ", res[n][i]);
		printf("\n");
	}
	return 0;
}
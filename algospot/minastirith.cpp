#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

const int INF=987654321;
const double pi=4.0*acos(0);
int n;
double y[100],x[100],r[100];
pair<double,double> ranges[100];

int linear(double ,double);

void convert()
{
	for(int i=0;i<n;i++)
	{
		double loc=fmod(pi+atan2(y[i],x[i]),pi);
		double range=2.0*asin(r[i]/16.0);
		ranges[i]=make_pair(loc-range,loc+range);
	}
}

int circle()
{
	int ret=INF;
	sort(ranges,ranges+n);
	for(int i=0;i<n;i++)
		if(ranges[i].first<=0||ranges[i].second>=pi)
		{
			double begin=fmod(ranges[i].second,pi);
			double end=fmod(ranges[i].first+pi,pi);
			ret=min(ret,1+linear(begin,end));
		}
	return ret;
}

int linear(double begin,double end)
{
	int used=0,idx=0;
	while(begin<end)
	{
		double maxcover=-1;
		while(idx<n&&ranges[idx].first<=begin)
		{
			maxcover=max(maxcover,ranges[idx].second);
			idx++;
		}
		if(maxcover<=begin)return INF;
		begin=maxcover;
		used++;
	}
	return used;
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>y[i]>>x[i]>>r[i];
		convert();
		cout.precision(8);
		if(circle()!=INF)cout<<circle()<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}

#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;
pair<double, double> ranges[100];

int main()
{
    int C;
    scanf("%d", &C);
    for (int c = 0; c < C; ++c)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            double y, x, r;
            scanf("%lf%lf%lf", &y, &x, &r);
            double loc = fmod(atan2(y, x) + 2 * M_PI, 2 * M_PI);
            double range = 2 * asin(r / 2 / 8);
            ranges[i] = make_pair(loc - range, loc + range);
        }
        sort(ranges, ranges + n);
        int r = numeric_limits<int>::max();
        for (int i = 0; i < n; ++i)
        {
            if (ranges[i].first <= 0 || ranges[i].second >= 2 * M_PI)
            {
                double begin = fmod(ranges[i].second, 2 * M_PI);
                double end = fmod(ranges[i].first + 2 * M_PI, 2 * M_PI);
                int current = 1;
                while (begin < end)
                {
                    double maximum = begin;
                    for (int j = 0; j < n; ++j)
                    {
                        if (ranges[j].first <= begin)
                        {
                            maximum = max(maximum, ranges[j].second);
                        }
                    }
                    if (maximum == begin)
                    {
                        current = numeric_limits<int>::max();
                        break;
                    }
                    begin = maximum;
                    ++current;
                }
                r = min(r, current);
            }
        }
        if (r == numeric_limits<int>::max())
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n", r);
        }
    }
}
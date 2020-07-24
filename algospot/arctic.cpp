#include <iostream>
#include <queue>
#include <vector>
#include <iomanip>
#include <cmath>
using namespace std;

int n;
double dist[100][100];

bool decision(double d)
{
	vector<bool> visited(n,false);
	visited[0]=true;
	queue<int> q;
	q.push(0);
	int seen=0;
	while(!q.empty())
	{
		int here=q.front();
		q.pop();
		seen++;
		for(int i=0;i<n;i++)
			if(!visited[i]&&dist[here][i]<=d)
			{
				q.push(i);
				visited[i]=true;
			}
	}
	return seen==n;
}

double opt()
{
	double lo=0,hi=1416.00;
	for(int i=0;i<100;i++)
	{
		double mid=(hi+lo)/2.00;
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
		cin>>n;
		vector<pair<double,double>> c;
		for(int i=0;i<n;i++)
		{
			double y,x;
			cin>>y>>x;
			c.push_back(make_pair(y,x));
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				pair<double,double> p1=c[i];
				pair<double,double> p2=c[j];
				dist[i][j]=sqrt(pow((p2.first-p1.first),2)+pow((p2.second-p1.second),2));
			}
		cout<<fixed<<setprecision(2);
		cout<<opt()<<endl;
	}
	return 0;
}

#include<stdio.h>
#include<math.h>
#define MAX 87654321

int N;
struct Base
{
    double x;
    double y;
};

Base base[100];

bool visit[100];
double dist[100];

void solution(int curr)
{
   
    visit[curr]=true;
    
    int next=curr;
    double next_dist=MAX;    
    // 나를 제외하고 visit 안된 애들 resolve
    for(int idx=0; idx<N; idx++)
    {
        if(visit[idx])
        {
            continue;
        }
        double d=sqrt(pow((base[curr].x-base[idx].x),2)+pow((base[curr].y-base[idx].y),2));
        // resolve
        if(d<dist[idx])
        {
            dist[idx]=d;
        }
        // resolve 된 애들 중에서 최소값이 다음으로 visit할 곳
        if (dist[idx]<next_dist)
        {
            next_dist=dist[idx];
            next=idx;
        }
    }
    if(next == curr)
    {
        return;
    }
    solution(next);
}
void init()
{
    for(int i=0; i<N; i++)
    {
        visit[i]=false;
        dist[i]=MAX;
    }
}
int main()
{
    int testcase;
    scanf("%d", &testcase);
    for(int tc=1; tc<=testcase; tc++)
    {
        
        scanf("%d", &N);
        init();
        for(int i=0; i<N; i++)
        {
            scanf("%lf %lf", &base[i].x, &base[i].y);
        }
        solution(0);
        double result=0;
        for(int i=1; i<N; i++)
        {
            if(dist[i]>result)
            {
                result = dist[i];
            }
        }
        printf("%.2lf\n", result);
    }
}


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

int T,N;

double d[100][100];
double x[100],y[100];

int main(void)
{
        scanf("%d", &T);
        while(T--)
        {
                scanf("%d", &N);
                for(int i=0;i<N;i++)
                	scanf("%lf %lf", &x[i], &y[i]);

                for(int i=0;i<N;i++)
                	for(int j=0;j<N;j++)
                	{
                        double dx = x[i]-x[j];
                        double dy = y[i]-y[j];
                        d[i][j] = dx*dx + dy*dy;
                    }

                for(int k=0;k<N;k++)
                	for(int i=0;i<N;i++)
                		for(int j=0;j<N;j++)
                			{
                				d[i][j]=min(d[i][j],max(d[i][k],d[k][j]));
                			}

                double res=0;
                for(int i=0;i<N;i++)
                	for(int j=0;j<N;j++)
                	{
                        res=max(res,d[i][j]);
                    }
                printf("%.2lf\n", sqrt(res));
        }
        return 0;
}
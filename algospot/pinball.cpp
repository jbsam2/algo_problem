#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const double pi=4.0*acos(0.0);
const double EPSILON=1e-9;
const double INF=1e200;

struct vector2
{
	double x,y;
	explicit vector2(double x_=0,double y_=0):x(x_),y(y_)
	{}
	//벡터 비교
	bool operator==(const vector2& rhs)const
	{
		return x==rhs.x&&y==rhs.y;
	}
	bool operator<(const vector2& rhs)const
	{
		return x!=rhs.x?x<rhs.x:y<rhs.y;
	}
	//벡터 연산
	vector2 operator+(const vector2& rhs)const
	{
		return vector2(x+rhs.x,y+rhs.y);
	}
	vector2 operator-(const vector2& rhs)const
	{
		return vector2(x-rhs.x,y-rhs.y);
	}
	vector2 operator*(double rhs)const
	{
		return vector2(x*rhs,y*rhs);
	}
	//벡터 길이
	double norm()const
	{
		return hypot(x,y);
	}
	//단위벡터
	vector2 normalize()const
	{
		return vector2(x/norm(),y/norm());
	}
	//x축에서 부터 각도
	double polar()const
	{
		return fmod(atan2(y,x)+pi,pi);
	}
	//내적, 외적
	double dot(const vector2& rhs)const
	{
		return x*rhs.x+y*rhs.y;
	}
	double cross(const vector2& rhs)const
	{
		return x*rhs.y-y*rhs.x;
	}
	//벡터가 rhs에 그림자 내릴때
	vector2 project(const vector2& rhs)const
	{
		vector2 r=rhs.normalize();
		return r*r.dot(*this);
	}
};

int n;
vector<int> r;
vector<vector2> center;

vector<double> solve2(double a,double b,double c)
{
	double d=b*b-4*a*c;
	if(d<-EPSILON)return vector<double>();
	if(d<EPSILON)return vector<double>(1,-b/(2*a));
	vector<double> ret;
	ret.push_back((-b-sqrt(d))/(2*a));
	ret.push_back((-b+sqrt(d))/(2*a));
	return ret;
}

double hitcircle(vector2 here,vector2 dir,vector2 center,int radius)
{
	double a=dir.dot(dir);
	double b=2*dir.dot(here-center);
	double c=here.dot(here)+center.dot(center)-2*here.dot(center)-radius*radius;
	vector<double> sols=solve2(a,b,c);
	if(sols.empty()||sols[0]<EPSILON) return INF;
	return sols[0];
}

vector2 reflect(vector2 dir,vector2 center,vector2 contact)
{
	return (dir-dir.project(contact-center)*2).normalize();
}

void simulate(vector2 here,vector2 dir)
{
	dir=dir.normalize();
	int hitcnt=0;
	while(hitcnt<100)
	{
		int circle=-1;
		double time=INF*0.5;
		for(int i=0;i<n;i++)
		{
			double cand=hitcircle(here,dir,center[i],r[i]+1);
			if(cand<time)
			{
				time=cand;
				circle=i;
			}
		}
		if(circle==-1)break;
		if(hitcnt++)cout<<" ";
		cout<<circle;
		vector2 contact=here+dir*time;
		dir=reflect(dir,center[circle],contact);
		here=contact;
	}
	cout<<endl;
}

int main()
{
	int t,tx,ty,tr;
	cin>>t;
	while(t--)
	{
		center.clear();
		r.clear();
		int x,y,dx,dy;
		cin>>x>>y>>dx>>dy>>n;
		vector2 here(x,y);
		vector2 dir(dx,dy);
		for(int i=0;i<n;i++)
		{
			cin>>tx>>ty;
			center.push_back(vector2(tx,ty));
			cin>>tr;
			r.push_back(tr);
		}
		simulate(here,dir);
	}
	return 0;
}


#include <cstdio>
#include <cmath>

double x[50], y[50], z[50];

void Norm(double &dX, double &dY)
{
	double Z = sqrt(dX * dX + dY * dY);
	dX /= Z;
	dY /= Z;
}

int main()
{
	int tcn;
	scanf("%d", &tcn);
	while (tcn--)
	{
		double X, Y, dX, dY;
		double tX, tY, tZ, Z;
		int i, j, k, n;
		scanf("%lf%lf%lf%lf%d", &X, &Y, &dX, &dY, &n);
		for (i = 0; i < n; i++)
		{
			scanf("%lf%lf%lf", &x[i], &y[i], &z[i]);
			z[i] += 1;
		}
		Norm(dX, dY);
		for (i = 0; i < 100; i++)
		{
			k = -1;
			Z = 11e11;
			for (j = 0; j < n; j++)
			{
				tZ = dX * (x[j] - X) + dY * (y[j] - Y);
				if (tZ < 0) continue;
				tX = tZ * dX - x[j] + X;
				tY = tZ * dY - y[j] + Y;
				if (tX * tX + tY * tY > z[j] * z[j]) continue;
				if (tZ < Z)
				{
					k = j;
					Z = tZ;
				}
			}
			if (k == -1) break;
			printf("%d ", k);
			tX = Z * dX - x[k] + X;
			tY = Z * dY - y[k] + Y;
			Z = sqrt(z[k] * z[k] - tX * tX - tY * tY);
			tX -= Z * dX;
			tY -= Z * dY;
			X = x[k] + tX;
			Y = y[k] + tY;
			Norm(tX, tY);
			Z = dX * tX + dY * tY;
			dX -= 2 * Z * tX;
			dY -= 2 * Z * tY;
		}
		puts("");
	}
}
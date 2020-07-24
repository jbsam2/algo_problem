#include <iostream>
#include <algorithm>
#include <bitset>
#include <cstring>
using namespace std;

int candidates[10][46][1024],n,color[20][20],value[20][20],hint[20][20][2],q,sum[400],length[400],known[400];

void put(int y,int x,int val)
{
	for(int h=0;h<2;h++)
		known[hint[y][x][h]]+=(1<<val);
	value[y][x]=val;
}

void remove(int y,int x,int val)
{
	for(int h=0;h<2;h++)
		known[hint[y][x][h]]-=(1<<val);
	value[y][x]=0;
}

int getcandhint(int hint)
{
	return candidates[length[hint]][sum[hint]][known[hint]];
}

int getcandcoord(int y,int x)
{
	return getcandhint(hint[y][x][0])&getcandhint(hint[y][x][1]);
}

int getsize(int set)
{
	int size=0,compare=1;
	for(int i=1;i<=9;i++)
	{
		compare=compare<<1;
		if(compare&set)size++;
	}
	return size;
}

int getsum(int set)
{
	int sum=0,compare=1;
	for(int i=1;i<=9;i++)
	{
		compare=compare<<1;
		if(compare&set)
			sum+=i;
	}
	return sum;
}

void generatecandidates()
{
	memset(candidates,0,sizeof(candidates));
	for(int set=0;set<1024;set+=2)
	{
		int l=getsize(set),s=getsum(set);
		int subset=set;
		while(1)
		{
			candidates[l][s][subset]|=(set&~subset);
			if(subset==0)break;
			subset=(subset-1)&set;
		}
	}
}

void printsol()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
			cout<<value[i][j]<<" ";
		cout<<endl;
	}
}

bool search()
{
	int y=-1,x=-1,mincands=1023;
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(color[i][j]==1&&value[i][j]==0)
			{
				int cands=getcandcoord(i,j);
				if(getsize(mincands)>getsize(cands))
				{
					mincands=cands;
					y=i;
					x=j;
				}
			}
	if(mincands==0)return false;
	if(y==-1)
	{
		printsol();
		return true;
	}
	for(int val=1;val<=9;val++)
		if(mincands&(1<<val))
		{
			put(y,x,val);
			if(search())return true;
			remove(y,x,val);
		}
	return false;
}

int main()
{
	int test;
	cin>>test;
	generatecandidates();
	while(test--)
	{
		memset(color,0,sizeof(color));
		memset(value,0,sizeof(value));
		memset(hint,0,sizeof(hint));
		memset(sum,0,sizeof(sum));
		memset(length,0,sizeof(length));
		memset(known,0,sizeof(known));
		cin>>n;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cin>>color[i][j];
		cin>>q;
		for(int i=0;i<q;i++)
		{
			int y,x,dir,total;
			int my,mx,ny,nx;
			int len=0;
			cin>>y>>x>>dir>>total;
			hint[y-1][x-1][dir]=i;
			sum[hint[y-1][x-1][dir]]=total;
			if(dir)my=1,mx=0;
			else my=0,mx=1;
			ny=y-1+my,nx=x-1+mx;
			while(1)
			{
				if(!color[ny][nx])break;
				hint[ny][nx][dir]=i;
				len++;
				ny+=my;
				nx+=mx;
			}
			length[hint[y-1][x-1][dir]]=len;
		}
		search();
	}
	return 0;
}

#include <iostream>
#include <vector>
using namespace std;

const int N = 20;

bool track(int t, const vector<pair<int, int> > & p, const int m[][N][2], int w[], bool v[][10], int u[], int h, int n, int a[][N])
{
    int i, j;

    if (t == p.size())
    {
        for (i = 0; i < h; ++i)
        {
            if (u[i] || w[i])
                return false;
        }

        for (i = 0; i < n; ++i)
        {
            for (j = 0; j < n; ++j)
                cout << a[i][j] << ' ';
            cout << endl;
        }
        return true;
    }

    int y = p[t].first;
    int x = p[t].second;
    int hh = m[y][x][0];
    int hv = m[y][x][1];
    --u[hh], --u[hv];
    for (int i = 1; i <= 9; ++i)
    {
        if ((u[hh] ? w[hh] > i : w[hh] == i) && !v[hh][i] && (u[hv] ? w[hv] > i : w[hv] == i) && !v[hv][i])
        {
            w[hh] -= i; v[hh][i] = true;
            w[hv] -= i; v[hv][i] = true;
            a[y][x] = i;
            if (track(t + 1, p, m, w, v, u, h, n, a))
                return true;
            w[hh] += i; v[hh][i] = false;
            w[hv] += i; v[hv][i] = false;
        }
    }
    ++u[hh], ++u[hv];
    return false;
}

void run()
{
    int n;
    cin >> n;

    int i, j, k;
    int a[N][N];
    for (i = 0; i < n; ++i)
        for (j = 0; j < n; ++j)
            cin >> a[i][j];

    int m[N][N][2];
    vector<pair<int, int> > p;
    for (i = 0; i < n; ++i)
    {
        for (j = 0; j < n; ++j)
        {
            m[i][j][0] = m[i][j][1] = -1;
            if (a[i][j])
                p.push_back(make_pair(i, j));
        }
    }

    int h;
    cin >> h;
    int y, x, d, w[N * N * 2], u[N * N * 2];
    bool v[N * N * 2][10];
    for (i = 0; i < h; ++i)
    {
        u[i] = 0;
        for (k = 1; k <= 9; ++k)
            v[i][k] = false;
        cin >> y >> x >> d >> w[i];
        --y, --x;
        if (d == 0)
            for (k = 1; x + k < n && a[y][x + k]; ++k)
                m[y][x + k][0] = i, ++u[i];
        else
            for (k = 1; y + k < n && a[y + k][x]; ++k)
                m[y + k][x][1] = i, ++u[i];
    }

    track(0, p, m, w, v, u, h, n, a);
}

int main()
{
    int n;
    cin >> n;
    while (n--)
        run();
}
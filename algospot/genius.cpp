#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n,k,length[50];
double t[50][50];

class squaremat
{
private:
	vector<vector<double>> v;
	int size;
public:
	squaremat(int n):size(n)
	{
		v.resize(size,vector<double>(size,0));
	}
	~squaremat()
	{
		for(int i=0;i<size;i++)
			v[i].clear();
		v.clear();
	}
	squaremat identity(int n)
	{
		squaremat ret=squaremat(n);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(i==j)ret.v[i][j]=1;else ret.v[i][j]=0;
		return ret;			
	}
	squaremat operator*(squaremat &b)
	{
		squaremat ret=squaremat(size);
		for(int i=0;i<size;i++)
			for(int j=0;j<size;j++)
				for(int l=0;l<size;l++)
					ret.v[j][l]+=v[j][i]*b.v[i][l];
		return ret;
	}
	squaremat pow(int k)
	{
		if(k==0)
			return identity(size);
		if(k%2==1)
			return pow(k-1)**this;
		squaremat half=pow(k/2);
		return half*half;
	}
	double *operator[](int i)
	{
		return &v[i][0];
	}
};

vector<double> getprob(void)
{
	squaremat w(4*n);
	for(int i=0;i<3*n;i++)
		w[i][i+n]=1.0;
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			w[3*n+i][(4-length[j])*n+j]=t[j][i];
	squaremat wk=w.pow(k);
	vector<double> ret(n);
	for(int song=0;song<n;song++)
		for(int start=0;start<length[song];start++)
			ret[song]+=wk[(3-start)*n+song][3*n];
	return ret;
}

int main()
{
	int test,fav,favsong;
	cin>>test;
	while(test--)
	{
		cin>>n>>k>>fav;
		for(int i=0;i<n;i++)
			cin>>length[i];
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cin>>t[i][j];
		vector<double> ret=getprob();
		for(int i=0;i<fav;i++)
		{
			cin>>favsong;
			cout.precision(8);
			cout<<ret[favsong]<<" ";
		}
		cout<<endl;
	}
	return 0;
}

#include <cstdio>
#define FF(x,e) for( x=0; x<e; ++x )

int N, K, M, L[50], Q[10], i , j;
double T[50][50];

int main()
{
    int CC; scanf("%d", &CC);
    while(CC--)
    {
        scanf("%d %d %d", &N, &K, &M);
        FF(i, N) scanf("%d", &L[i]);
        FF(i, N) FF(j, N) scanf("%lf", &T[i][j]);
        FF(i, M) scanf("%d", &Q[i]);
        
        double TT[5][50] = {0, };
        TT[L[0]][0] = 1;
        
        for(int t=0; t<=K; ++t)
        {
            FF(i, N)
            {
                double tmp = 0;
                FF(j, N) tmp += TT[t%5][j] * T[j][i];
                TT[(t+L[i])%5][i] += tmp;
            }
            FF(i, N)TT[t%5][i] = 0;
        }
        
        FF(i, M)
        {
            double tmp = 0;
            for(int j=1; j<=L[Q[i]]; ++j) tmp += TT[(K+j)%5][Q[i]];
            printf("%.8lf ",tmp);
        }
        printf("\n");
    }
}

#include<iostream>
using namespace std;
const int N = 51;
const int M = 11;
const int N4 = 4 * 50 + 1;
int n, k, m;
int n4;
int L[N];
int P[N + 1];
double T[N][N];
int favorite[M];

double Mat[N4][N4];
double(*A)[N4];
double Mat2[N4][N4];
double(*B)[N4];

double IMat[N4];
double(*C);
double IMat2[N4];
double(*D);

void mulMatrix()
{
	for (int a = 1; a <= n4; a++)
		D[a] = 0;
	for (int a = 1; a <= n4; a++)
	{
		for (int b = 1; b <= n4; b++)
		{
			D[a] += A[a][b] * C[b];
		}
	}
	double(*t) = C;
	C = D;
	D = t;
}

void powMatrix()
{
	for (int a = 1; a <= n4; a++)
		for (int c = 1; c <= n4; c++)
			B[a][c] = 0;
	for (int a = 1; a <= n4; a++)
	{
		for (int b = 1; b <= n4; b++)
		{
			for (int c = 1; c <= n4; c++)
			{
				B[a][c] += A[a][b] * A[b][c];
			}
		}
	}
	double (*t)[N4] = A;
	A = B;
	B = t;
	
}

void printA()
{
	for (int i = 1; i <= m; i++)
	{
		int playingSong = favorite[i] + 1;
		double ret = 0;
		for (int left = 0; left < L[playingSong]; left++)
		{
			ret += C[P[playingSong] + left];
		}
		cout << ret << " ";
	}
	cout << endl;
}

void play()
{
	for (int x = k; x; x >>= 1)
	{
		if (x & 1)
			mulMatrix();
		powMatrix();
	}
}


void build()
{
	int cur = 1;
	for (int playingSong = 1; playingSong <= n; playingSong++)
	{
		for (int left = 1; left <= L[playingSong]; left++, cur++)// 1분후 노래의 남은시간(현재 1~4남아 있는 노래들이 0~3남아있게된다)
		{
			for (int prev = 1; prev <= n4; prev++)
				Mat[cur][prev] = 0;
			if (left < L[playingSong])//cur is under playing song
			{
				Mat[cur][cur + 1] = 1;
			}
			else//cur is new start song
			{
				for (int endedSong = 1; endedSong <= n; endedSong++)
					Mat[cur][P[endedSong]] += T[endedSong][playingSong];
			}
		}
	}
	int debug = 1;
}

void init()
{
	A = Mat;
	B = Mat2;
	C = IMat;
	D = IMat2;

	cin >> n >> k >> m;
	
	P[1] = 1;
	for (int i = 1; i <= n; i++)
	{
		cin >> L[i];
		P[i + 1] = P[i] + L[i];
	}
	n4 = P[n + 1];
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> T[i][j];
	for (int i = 1; i <= m; i++)
		cin >> favorite[i];

	for (int i = 1; i <= n4; i++)
		IMat[i] = 0;

	IMat[L[1]] = 1;
}

int main()
{
	ios::sync_with_stdio(false);
	//freopen("input.txt","r",stdin);
	cout.setf(ios::fixed);
	cout.precision(8);
	int T;
	cin >> T;
	while (T--)
	{
		init();
		build();
		play();
		printA();
	}
	return 0;
}
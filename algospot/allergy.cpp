#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int n,m,best;
vector<int> caneat[50],eaters[50];

void search(vector<int>& edible, int chosen)
{
	if(chosen>=best)return;
	int first=0;
	while(n>first&&edible[first]>0)first++;
	if(first==n){best=chosen;return;}
	for(int i=0;i<caneat[first].size();i++)
	{
		int food=caneat[first][i];
		for(int j=0;j<eaters[food].size();j++)
			edible[eaters[food][j]]++;
		search(edible,chosen+1);
		for(int j=0;j<eaters[food].size();j++)
			edible[eaters[food][j]]--;
	}
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>n>>m;
		best=m;
		map<string,int> idx;
		for(int i=0;i<n;i++)
		{
			string name;
			cin>>name;
			idx[name]=i;
		}
		for(int i=0;i<m;i++)
		{
			int people;
			cin>>people;
			while(people--)
			{
				string name;
				cin>>name;
				eaters[i].push_back(idx[name]);
				caneat[idx[name]].push_back(i);
			}
		}
		vector<int> edible(n,0);
		search(edible,0);
		cout<<best<<endl;
		for(int i=0;i<m;i++)
			eaters[i].clear();
		for(int i=0;i<n;i++)
			caneat[i].clear();
	}
	return 0;
}

#include <cstdio>
#include <cstring>
#include <string>
#include <map>
typedef long long int I64;

int T,N,M,sfb;
I64 A[50];
char F[50][11],s[11];
std::map<std::string,int> p;

int f(int n,I64 bf,int sf)
{
	if(!bf||n>=M||sf>=sfb)
		return !bf?0:M;
	int a=f(n+1,bf,sf),b=bf&A[n]?1+f(n+1,bf&~A[n],sf+1):M,mn=a<b?a:b;
	return (!sf)?sfb=mn:mn;
}

int main()
{
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&N,&M),memset(A,0,sizeof(A)),sfb=M;
		for(int i=0;i<N;++i)
			scanf("%s",F[i]),p[F[i]]=i;
		for(int i=0,t;i<M;++i)
		{
			scanf("%d",&t);
			for(int j=0;j<t;++j)
				scanf("%s",s),A[i]|=1<<p[s];
		}
		printf("%d\n",f(0,(1LL<<N)-1,0));
	}
}

#include <cstdio>
#include <cstring>

int N, M; // 친구의 수, 음식의 수 (모두 50 이하)
char F[50][11];  // 친구의 이름
char AM[50][50]; // 관계 매트릭스 [친구][음식] : 1-먹음 0-못먹음
int Answer; // 만들어야 할 최소의 음식 수

// 재귀함수에서 사용되는 변수
int eatsN[50]; // 먹을 수 있는 음식의 수
int restN[50]; // 제공된 음식 중 먹을 수 있는 음식의 수 (0:추가제공필요, 1~:만족)
int provM[50]; // 제공된 음식 (1:제공됨, 0:제공안됨)

void chooseFood(int foodNo, int nM)
{ // 이번에 제공할 음식, 제공된 음식 수
	if (nM >= Answer) return; // 이미 최적해가 아님.

	// 해당 음식에 대해 만족하는 사람을 골라 냄.
	bool made(false);
	if (foodNo >= 0)
	{
		made = true;
		for (int n = 0; n < N; n++)
		{
			restN[n] += AM[n][foodNo];
			if (restN[n] == 0) made = false;
		}
	}
	if (made)
	{ // 메뉴 구성 완료, 모든 사람 만족
		Answer = nM; // 항상 실행됨.
		for (int n = 0; n < N; n++)
		{
			restN[n] -= AM[n][foodNo];
		}
		return;
	}

	// 이 시점에서 restN[n] == 0 인 n 이 적어도 하나 존재해야 함.

	// 아직 음식이 추가로 필요한 사람 중
	// 먹을 수 있는 음식의 수가 제일 적은 사람 택함.
	int tmpeat = 51, tmpn = -1;
	for (int n = 0; n < N; n++)
	{
		if (restN[n] == 0)
		{
			if (eatsN[n] < tmpeat)
			{
				tmpeat = eatsN[n];
				tmpn = n;
			}
		}
	}

	// 선택된 사람이 먹을 수 있는 음식 찾아내서 재귀호출.
	for (int m = 0; m < M; m++)
	{
		if (AM[tmpn][m]) chooseFood(m, nM + 1);
	}

	if (foodNo >= 0)
	{
		for (int n = 0; n < N; n++)
		{
			restN[n] -= AM[n][foodNo];
		}
	}
}

int main()
{
	int test_case, T;
	int tmp;
	char buffer[11];

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; test_case++)
	{
		// 입력
		memset(AM, 0, sizeof(AM));
		scanf("%d %d", &N, &M);
		for (int n = 0; n < N; n++)
		{
			scanf("%s", F[n]);
		}
		for (int m = 0; m < M; m++)
		{
			scanf("%d", &tmp);
			for (int i = 0; i < tmp; i++)
			{
				scanf("%s", buffer);
				for (int n = 0; n < N; n++)
				{
					if (strcmp(buffer, F[n])) continue;
					AM[n][m] = 1;
					break;
				}
			}
		}
		Answer = 100;

		// 재귀함수 사용 변수 초기화
		for (int n = 0; n < N; n++)
		{
			eatsN[n] = 0;
			for (int m = 0; m < M; m++) eatsN[n] += AM[n][m];
			restN[n] = 0;
		}
		memset(provM, 0, sizeof(provM));
		// 처리
		chooseFood(-1, 0);
		// 출력
		printf("%d\n", Answer);

	}

	return 0;
}
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int order(const vector<int> &rus,const vector<int> &kor)
{
	int n=rus.size(),win=0;

	multiset<int> rating(kor.begin(),kor.end());
	for(int r=0;r<n;r++)
	{
		if(*rating.rbegin()<rus[r])
			rating.erase(rating.begin());
		else
		{
			rating.erase(rating.lower_bound(rus[r]));
			win++;
		}
	}
	return win;
}

int main()
{
	int test,n,score;
	cin>>test;
	while(test--)
	{
		vector<int> rus;
		vector<int> kor;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>score;
			rus.push_back(score);
		}
		for(int i=0;i<n;i++)
		{
			cin>>score;
			kor.push_back(score);
		}
		cout<<order(rus,kor)<<endl;
	}
	return 0;
}

#include <cstdio>
#include <algorithm>
using std::sort;
int main()
{
	int c,n,i,en,win,rus[100],kor[100];
	scanf("%d",&c);
	while(c--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&rus[i]);
		for(i=0;i<n;i++)
			scanf("%d",&kor[i]);
		sort(rus,rus+n);
		sort(kor,kor+n);
		en=n-1;
		win=0;
		for(i=n-1;i>=0;i--)
			if(rus[i]<=kor[en])
				{
					en--;
					win++;
				}
		printf("%d\n",win);
	}
	return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
#ifdef _DEBUG
	freopen("matchorder.in", "r", stdin);
#endif
	
	int C, N;
	cin >> C;
	while (C--)
	{
		cin >> N;
		vector<int> R(N), K(N);
		for (auto& n : R) cin >> n;
		for (auto& n : K) cin >> n;
		sort(begin(R), end(R));
		sort(begin(K), end(K));
		int r = 0, k = 0;
		while (k < N)
		{
			if (R[r] <= K[k]) r++;
			k++;
		}
		cout << r << endl;
	}

	return 0;
}

#include <stdio.h>
#include <algorithm>
using namespace std;
int order[100];
int num[100];
bool chk[100];
int nsize = 0;

int main()
{
	int size = 0;
	scanf("%d", &size);
	while (size--)
	{
		scanf("%d", &nsize);
		int i = 0;
		while (i < nsize)
		{
			chk[i] = false;
			i++;
		}
		i = 0;
		while (i < nsize)
		{
			scanf("%d", &order[i]);
			i++;
		}
		i = 0; 
		while (i < nsize)
		{
			scanf("%d", &num[i]);
			i++;
		}
		sort(num, num + i);

		i = 0;
		int cnt = 0;
		while (i < nsize)
		{
			int j = 0;
			int cur = -1;
			while (j < nsize)
			{
				if (chk[j]==false && order[i] <= num[j])
				{
					cur = j;
					break;
				}
				j++;
			}
			if (cur != -1) cnt++;
			else
			{
				j = 0;
				while (j < nsize)
				{
					if (chk[j] == false)
					{
						cur = j;
						break;
					}
					j++;
				}
			}
			chk[cur] = true;
			i++;
		}
		printf("%d\n", cnt);
	}
	return 0;
}
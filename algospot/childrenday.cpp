#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;

int append(int here,int edge,int mod)
{
	int there=here*10+edge;
	if(there>=mod) return mod+there%mod;
	return there%mod;
}

string gifts(string digits,int n,int m)
{
	sort(digits.begin(),digits.end());
	vector<int> parent(2*n,-1),choice(2*n,-1);
	queue<int> q;
	parent[0]=0;
	q.push(0);
	while(!q.empty())
			if(parent[there]==-1)
			{
				parent[there]=here;
				choice[there]=digits[i]-'0';
	{
		int here=q.front();
		q.pop();
		for(int i=0;i<digits.size();i++)
		{
			int there=append(here,digits[i]-'0',n);
				q.push(there);
			}
		}
	}
	if(parent[n+m]==-1) return "IMPOSSIBLE";
	string ret;
	int here=n+m;
	while(parent[here]!=here)
	{
		ret+=char('0'+choice[here]);
		here=parent[here];
	}
	reverse(ret.begin(),ret.end());
	return ret;
}

int main()
{
	int t,n,m;
	cin>>t;
	while(t--)
	{
		string d;
		cin>>d>>n>>m;
		cout<<gifts(d,n,m)<<endl;
	}
	return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		string A; 
		int N, M;
		cin>>A>>N>>M;
		sort(begin(A), end(A));
		vector<string> C(N), D(N);
		queue<int> q;
		q.push(0);
		while(!q.empty())
		{
			int i=q.front();
			q.pop();
			bool f=false;
			string s;
			if(i<0) i=~i,s=D[i],f=true;
			else s=C[i];
			for(char c:A)
			{
				int j=i*10+c-'0';
				bool k=f;
				if(j>=N) j%=N, k=true;
				if(k && D[j].empty()) q.push(~j), D[j]=s+c;
				if(!k && C[j].empty()) q.push(j), C[j]=s+c;
			}
		}
		if(D[M].empty()) 
			cout<<"IMPOSSIBLE\n";
		else 
			cout<<D[M]<<'\n';
	}
}
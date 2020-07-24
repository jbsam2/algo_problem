#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAX=15;
int k,cache[MAX][(1<<MAX)+1],overlap[MAX+1][MAX+1];
string word[MAX+1];

int getoverlap(const string &s1,const string &s2)
{
	for(int length=min(s1.size(),s2.size());length>0;length--)
		if(s1.substr(s1.size()-length)==s2.substr(0,length))return length;
	return 0;
}

int restore(int last,int used)
{
	if(used==(1<<k)-1)return 0;
	int& ret=cache[last][used];
	if(ret!=-1)return ret;
	ret=0;
	for(int next=0;next<k;next++)
		if((used&(1<<next))==0)
		{
			int cand=overlap[last][next]+restore(next,used+(1<<next));
			ret=max(ret,cand);
		}
	return ret;
}

string reconstruct(int last,int used)
{
	if(used==(1<<k)-1)
		return "";
	for(int next=0;next<k;next++)
	{
		if(used&(1<<next))continue;
		int ifused=restore(next,used+(1<<next))+overlap[last][next];
		if(restore(last,used)==ifused)
			return (word[next].substr(overlap[last][next])+reconstruct(next,used+(1<<next)));
	}
	return "fuck!";
}

int main()
{
	int test;
	cin>>test;
	while(test--)
	{
		cin>>k;
		for(int i=0;i<k;i++)
			cin>>word[i];
		memset(cache,-1,sizeof(cache));
		while(true)
		{
			bool removed=false;
			for(int i=0;i<k&&!removed;i++)
				for(int j=0;j<k;j++)
					if(i!=j&&word[i].find(word[j])!=-1)
					{
						word[j]=word[k-1];
						k--;
						removed=true;
					}
			if(!removed)
				break;
		}
		word[k]="";
		for(int i=0;i<k;i++)
			for(int j=0;j<k;j++)
				overlap[i][j]=getoverlap(word[i],word[j]);
		cout<<reconstruct(k,0)<<endl;
	}
	return 0;
}

#include<ios>
#include<string>
using namespace std;
int T,N,M,D[1<<15][16],L[16][16];
char imsi[105];
string words[16],sol;
int main()
{
	int t,i,j,k,n,prev,tar,val,a;
	string str,str2;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for (i=1;i<=N;i++)
			scanf("%s",imsi),words[i]=imsi;
		for (i=1;i<=N;i++)
		{
			for (j=1;j<=N;j++) 
				if (i != j && words[j].find(words[i]) != string::npos)
				{
				words[i--] = words[N--]; break;
			    }
		}
		for (i=1;i<=N;i++) 
			for (j=1;j<=N;j++)
			{
			L[i][j]=words[i].size();
			while(words[i].substr(words[i].size()-L[i][j])!=words[j].substr(0,L[i][j])) 
				L[i][j]--;
		    }
		M = 1<<N;
		for (n=1;n<M;n++)
		{
			for (i=1;i<=N;i++) 
				if (n&(1<<(i-1)))
				{
				k = n-(1<<(i-1));
				D[n][i] = k?(int)1e9:words[i].size();
				for (j=1;j<=N;j++) 
					if (k&(1<<(j-1)))
					D[n][i] = min(D[n][i],(int)words[i].size()-L[i][j]+D[k][j]);
			    }
		}
		prev = 0; sol = "";
		for (n=M-1;n;)
		{
			val = 1e9;
			for (i=1;i<=N;i++) 
				if (n&(1<<(i-1)))
				{
				k = D[n][i];
				str2 = words[i];
				if (prev) 
					k -= L[prev][i], str2 = str2.substr(L[prev][i]);
				if (val > k || (val == k && str > str2))
					val = k, str = str2, tar = i;
			    }
			sol += str;
			prev = tar;
			n -= 1<<(tar-1);
		}
		puts(sol.c_str());
	}
	return 0;
}
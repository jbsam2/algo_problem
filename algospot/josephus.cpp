#include <iostream>
#include <list>
using namespace std;

void josephus(int n,int k)
{
	list<int> survivors;
	for(int i=1;i<=n;i++)
		survivors.push_back(i);
	list<int>::iterator kill=survivors.begin();
	while(n>2)
	{
		kill=survivors.erase(kill);
		if(kill==survivors.end())kill=survivors.begin();
		n--;
		for(int i=0;i<k-1;i++)
		{
			kill++;
			if(kill==survivors.end())kill=survivors.begin();
		}
	}
	cout<<survivors.front()<<" "<<survivors.back()<<endl;
}
int main()
{
	int t,n,k;
	cin>>t;
	while(t--)
	{
		cin>>n>>k;
		josephus(n,k);
	}
	return 0;
}

#include <iostream>
using namespace std;
int main()
{
	int C;
	cin>>C;
	while(C--)
		{
			int j=0,k=1,i=2,N,K;
			cin>>N>>K;
			for(;i<N;i++)
				{
					j=(j+K-1)%i+1;
					k=(k+K-1)%i+1;
				}
			cout<<min(j,k)+1<<" "<<max(j,k)+1<<endl;
		}
}
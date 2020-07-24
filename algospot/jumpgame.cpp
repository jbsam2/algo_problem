#include <iostream>
#include <cstring>
using namespace std;
int board[100][100],cache[100][100];
int solve(int y,int x,int max)
{
	if(y==max-1&&x==max-1)
		return 1;
	if(y>=max||x>=max)
		return 0;
	int &result=cache[y][x];
	if(result!=-1)
		return result;
	return result=(solve(y+board[y][x],x,max)||solve(y,x+board[y][x],max));
}
int main()
{
	int test,max;
	cin>>test;
	if(test>50||test<0)
		exit(-1);
	while(test--)
	{
		cin>>max;
		if(max<2||max>100)
			exit(-1);
		memset(cache,-1,sizeof(cache));
		for(int i=0;i<max;i++)
			for(int j=0;j<max;j++)
				cin>>board[i][j];
		if(solve(0,0,max)==1)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}

#include<ios>
#define S(w){w=0;while(*b&&*b<48)b++;while(*b>47)w=w*10+(*b++-'0');}
int C,n,i,V[999][999];char B[9999999],*b=B;
int M(int x,int y)
{
	int&v=V[x][y];
	return(v&&x<n&&y<n&&(M(x+v,y)||M(x,y+v)))||(x==y&&x==n-1)||(v=0);
}
int main()
{
	B[fread(B,1,9999999,stdin)]=0;
	S(C);
	while(C--)
		{
			S(n);
			for(i=0;i<n*n;i++)S(V[i%n][i/n]);puts(M(0,0)? "YES" : "NO");}}
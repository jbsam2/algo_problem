#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(vector<int> &fence,int left, int right)
{
  if(left==right)
    return fence[left];
  int mid=(left+right)/2;
  int result=max(solve(fence,left,mid),solve(fence,mid+1,right));
  int low=mid,high=mid+1;
  int height=min(fence[low],fence[high]);
  result=max(result,height*2);
  while(left<low||high<right)
  {
    if(high<right&&(low==left||fence[low-1]<fence[high+1]))
    {
      high++;
      height=min(height,fence[high]);
    }
    else
    {
      low--;
      height=min(height,fence[low]);
    }
    result=max(result,height*(high-low+1));
  }
  return result;
}
int main()
{
  int test,num;
  cin>>test;
  while(test--)
  {
    cin>>num;
    vector<int> fence(num,0);
    for(int i=0;i<num;i++)
    {
      cin>>fence[i];
    }
    cout<<solve(fence,0,fence.size()-1)<<endl;
  }
  return 0;
}

#include <stdio.h>
#include <algorithm>

int C,N,F[20000];

int f(int b,int e)
{
  if(b==e) return F[b];
  int p=std::min_element(F+b,F+e+1)-F;
  int alt[]={F[p]*(e-b+1),p!=b?f(b,p-1):0,p!=e?f(p+1,e):0};
  return *std::max_element(alt,alt+3);
}

int main()
{
  scanf("%d",&C);
  while(C--)
  {
    scanf("%d",&N);
    for(int i=0;i<N;++i) scanf("%d",F+i);
    printf("%d\n",f(0,N-1));}
}
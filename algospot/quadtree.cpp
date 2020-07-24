#include <iostream>
#include <string>
using namespace std;

string reverse(string::iterator &it)
{
  char head = *it;
  ++it;
  if(head=='b'||head=='w')
    return string(1, head);
  string upperLeft=reverse(it);
  string upperRight=reverse(it);
  string lowerLeft=reverse(it);
  string lowerRight=reverse(it);
    return string("x")+lowerLeft+lowerRight+upperLeft+upperRight;
}
int main(void)
{
  int test_case;
  string picture;
  cin >> test_case;
  if(test_case<0||test_case>50)
    exit(-1);
  for(int i=0;i<test_case;i++)
  {
    cin>>picture;
    if(picture.size()>1000)
      exit(-1);
    string::iterator it=picture.begin();
    cout<<reverse(it)<<endl;
  }
  return 0;
}

#include<iostream>
#include<string>
char A[9999];
int I;
std::string Z()
{
  I++;
  if(A[I]=='w')
    return "w";
  else if(A[I]=='b')
    return "b";
  else
    {
      std::string B=Z(),C=Z(),D=Z(),E=Z();
      return "x"+D+E+B+C;
    }
}
int main()
{
  int T;
  for(std::cin>>T;T>=1;T--)
    {
      std::cin>>A;
      I=-1;
      std::cout<<Z()<<'\n';
    }
}
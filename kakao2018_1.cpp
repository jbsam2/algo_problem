#include <iostream>
using namespace std;

int main()
{
	int size,i,a1[16],a2[16],ret[16],j;
	string result[16];
	cin>>size;
	for(i=0;i<size;i++)
		cin>>a1[i];
	for(i=0;i<size;i++)
		cin>>a2[i];
	for(i=0;i<size;i++)
	{
		ret[i]=a1[i]|a2[i];
		for(j=0;j<size;j++)
		{
			int target=(1<<(size-1));
			result[i]+=(ret[i]&(target>>j))>0?'#':' ';
		}
	}
	for(i=0;i<size;i++)
	{
		cout<<result[i]<<endl;
	}
	return 0;
}
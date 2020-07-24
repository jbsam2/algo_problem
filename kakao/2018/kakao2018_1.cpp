#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2)
{
    vector<string> answer;
    int ret[16],i,j;
    for(i=0;i<n;i++)
	{
        string tmp;
		ret[i]=arr1[i]|arr2[i];
		for(j=0;j<n;j++)
		{
			int target=(1<<(n-1));
			tmp+=(ret[i]&(target>>j))>0?'#':' ';
		}
        answer.push_back(tmp);
	}
    return answer;
}
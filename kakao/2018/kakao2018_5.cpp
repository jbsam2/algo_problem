#include <bits/stdc++.h>
using namespace std;
int a,b,c[676],d[676],i;

int solution(string str1,string str2)
{
	for(i=1;i<str1.size();i++)
		if(isalpha(str1[i-1])&&isalpha(str1[i]))
			c[((str1[i-1]&31)-1)*26+(str1[i]&31)-1]++;
	for(i=1;i<str2.size();i++)
		if(isalpha(str2[i-1])&&isalpha(str2[i]))
			d[((str2[i-1]&31)-1)*26+(str2[i]&31)-1]++;
	for(i=0;i<676;i++)
		a+=min(c[i],d[i]),b+=max(c[i],d[i]);
	return b?a*65536/b:65536;
}
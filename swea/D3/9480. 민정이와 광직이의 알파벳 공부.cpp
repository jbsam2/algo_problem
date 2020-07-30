#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;
int T, N;
const int correct = (1<<26)-1;
int map[26];
int word[15];
int answer;

void solution(int begin, int curWord) 
{
	if (curWord == correct) answer ++;
	for (int i = begin; i < N; i++) solution(i + 1, curWord | word[i]);
}
int main()
{
	for (int i = 0; i < 26; i++) map[i] = 1<<i;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++)
    {
		scanf("%d", &N);
		string str;
		for (int i = 0; i < N; i++)
        {
			cin >> str;
			int n = 0;
			for (int j = 0; j < str.length(); j++)	n |= map[str[j] - 'a'];
			word[i] = n;
		}
		answer = 0;
		solution(0, 0);
		printf("#%d %d\n",tc, answer);
	}
}
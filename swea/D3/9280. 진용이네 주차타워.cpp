#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;
int N, M;
int R[101] = { 0, };
int W[10001] = { 0, };
vector<int> park;
queue<int> wait;
queue<int> line;
int findNumberPark(int n) 
{
    for (int i = 0; i < park.size(); i++) 
        if (n == park[i]) 
        {
            park[i] = 0;
            return i;
        }
}

int findEmptyPark()
{
    for (int i = 0; i < park.size(); i++) if (!park[i]) return i;
    return -1;
}

int solution()
{
    int answer = 0;
    while (!line.empty() || !wait.empty())
    {
        int n;
        if (!line.empty()) n = line.front(), line.pop();
        else n = wait.front(), wait.pop();
        if (n > 0) 
        {
            int idx = findEmptyPark();
            if (idx == -1) wait.push(n);
            else
            {
                park[idx] = n;
                answer += R[idx] * W[n - 1];
            }
        }
        else
        {
            n = n * -1;
            int idx = findNumberPark(n);
            if (wait.size() > 0)
            {
                int n2 = wait.front(); wait.pop();
                park[idx] = n2;
                answer += R[idx] * W[n2 - 1];
            }
        }
    }
    return answer;
}
 
int main()
{
    int tc;
    scanf("%d", &tc);
    for (int t = 1; t <= tc; t++) 
    {
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++) scanf("%d", &R[i]);
        for (int i = 0; i < M; i++) scanf("%d", &W[i]);
        for (int i = 0; i < 2 * M; i++)
        {
            int n;
            scanf("%d", &n);
            line.push(n);
        }
        park.resize(N);
        printf("#%d %d\n", t, solution());
    }
}
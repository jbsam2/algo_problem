#include <stdio.h>
#include <queue>
using namespace std;
 
int main()
{
    int T;
    scanf("%d", &T);
    for (int test = 1; test<=T; test++)
    {    
        int n;
        scanf("%d", &n);
        printf("#%d",test);
 
        priority_queue<int> pq;
        for (int i = 0; i < n; i++) {
            int temp;
            scanf("%d", &temp);
            if (temp == 1) {
                int number;
                scanf("%d", &number);
                pq.push(number);
            }
            else if (temp == 2) {
                if (pq.empty()) {
                    printf(" -1");
                }
                else {
                    printf(" %d", pq.top());
                    pq.pop();
                }
            }
        }
        printf("\n");
    }
    return 0;
}
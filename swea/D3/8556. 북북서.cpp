#include<stdio.h>
#include<math.h>
 
int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++)
    {
        char temp[101];
        int nw[20] = { 0 }, nIdx = 0;
        scanf("%s", temp);
        for (int i = 0; temp[i] != '\0'; i++)
        {
            if (temp[i] == 'n') nw[nIdx++] = -90;
            if (temp[i] == 'w') nw[nIdx++] = 90;
        }
        int mot = pow(2, nIdx - 1);
        int num = (nw[--nIdx] == -90) ? 0 : 90 * pow(2, nIdx);
        for (int i = nIdx - 1; i >= 0; i--)
            num += nw[i] * pow(2, i);
        while (num % 2 == 0 && mot >= 2)
        {
            num /= 2;
            mot /= 2;
        }
        if(mot==1)
            printf("#%d %d\n", tc, num);
        else 
            printf("#%d %d/%d\n", tc, num, mot);
    }
}
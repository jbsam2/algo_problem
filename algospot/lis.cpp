#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int idx,length,arr[500],C[500];

void list(int num)
{
        if(idx==0||(idx>0&&C[idx-1]<=num))
        {
                C[idx++]=num;
                return;
        }
        int front=0,rear=idx-1;
        while(front<=rear)
        {
                int mid=(front+rear)/2;
                if(C[mid]<num)
                        front=mid+1;
                else
                        rear=mid-1;
        }
        C[rear+1]=num;
}
int main()
{
        int test;
        cin>>test;
        if(test<0||test>50)
                exit(-1);
        while(test--)
        {
                idx=0;
                cin>>length;
                if(length<1||length>500)
                        exit(-1);
                for(int i=0;i<length;i++)
                        cin>>arr[i];
                for(int i=0;i<length;i++)
                        list(arr[i]);
                cout<<idx<<endl<<endl;
        }
        return 0;
}

#include <stdio.h>

int main()
{
        int C, N, i, j, I[500], L[500], m, M;
        for (scanf("%d", &C); C--;)
        {
                scanf("%d", &N);
                M = 0;
                for (i = 0; i < N; i++)
                {
                        scanf("%d", I+i);
                        m = 0;
                        for (j = 0; j < i; j++)
                        {
                                if (I[j] < I[i] && L[j] > m)
                                        m = L[j];
                        }
                        L[i] = m + 1;
                        if (L[i] > M)
                                M = L[i];
                }
                printf("%d\n", M);
        }
}

#include <bits/stdc++.h>
using namespace std;
int a[501];
int main()
{
        ios_base::sync_with_stdio(false);
        cin.tie(NULL); // (a + K - 2) / K;
        int t;
        cin >> t;
        while (t--)
        {
                int n;
                cin >> n;
                for (int i = 0; i < n; i++)
                        cin >> a[i];
                vector<int> v;
                v.push_back(a[0]);
                for (int i = 1; i < n; i++)
                {
                        if (v[v.size() - 1] < a[i])
                        {
                                v.push_back(a[i]);
                        }
                        else
                        {
                                auto l = lower_bound(v.begin(), v.end(), a[i]);
                                *l = a[i];
                        }
                }
                cout << v.size() << '\n';
        }
}
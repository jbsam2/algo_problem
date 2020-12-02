from itertools import combinations as cb
for t in range(int(input())):
    n=int(input());l=[[*map(int,input().split())]for _ in range(n)];a=[sum(i)+sum(j)for i,j in zip(l,zip(*l))];b=sum(a)//2;p=[]
    for i in cb(a,n//2):p+=[abs(b-sum(i))]
    print(f'#{t+1}',min(p))


from itertools import combinations

for t in range(int(input())):
    N = int(input())
    DATA = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    for g1 in combinations(range(N), N//2):
        g2 = [i for i in range(N) if i not in g1]
        sum1 = sum2 = 0
        for i in range(N//2 - 1):
            for j in range(i + 1, N//2):
                sum1 += DATA[g1[i]][g1[j]] + DATA[g1[j]][g1[i]]
                sum2 += DATA[g2[i]][g2[j]] + DATA[g2[j]][g2[i]]

        sub_res = abs(sum1 - sum2)
        if sub_res < result:
            result = sub_res

    print(f'#{t+1}',result)
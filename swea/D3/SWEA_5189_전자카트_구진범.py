from itertools import permutations as p
for t in range(int(input())):
    n=int(input());b=[[*map(int,input().split())]for _ in range(n)];r=1<<32
    for i in p(range(1,n),n-1):
        k=0
        for j in range(1,n-1):k+=b[i[j-1]][i[j]]
        k+=b[0][i[0]]+b[i[-1]][0];r=min(k,r)
    print(f'#{t+1}',r)
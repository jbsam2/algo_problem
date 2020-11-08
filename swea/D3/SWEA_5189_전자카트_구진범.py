from itertools import permutations as p
for t in range(int(input())):
    n=int(input());b=[[*map(int,input().split())]for _ in range(n)];r=1<<32
    for i in p(range(1,n),n-1):
        k=0
        for j in range(1,n-1):k+=b[i[j-1]][i[j]]
        k+=b[0][i[0]]+b[i[-1]][0];r=min(k,r)
    print(f'#{t+1}',r)


def sol(i,idx,tmp,v):
    if i==n-1:
        global r
        r=min(r,tmp+b[idx][0])
    else:
        for j in range(1,n):
            if j!=idx and v&(1<<j)==0:sol(i+1,j,tmp+b[idx][j],v|(1<<j))            

for t in range(int(input())):
    n=int(input());b=[[*map(int,input().split())]for _ in range(n)];r=1<<32
    sol(0,0,0,0)
    print(f'#{t+1}',r)
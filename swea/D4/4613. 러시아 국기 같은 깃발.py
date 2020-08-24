for t in range(int(input())):
    n,m=map(int,input().split());f=[list(input())for _ in range(n)];c=[[m-x.count(T)for x in f]for T in 'WBR'];r=2**32
    for i in range(n-1):
        for j in range(i+1,n-1):r=min(sum(c[0][:i+1]+c[1][i+1:j+1]+c[2][j+1:]),r)
    print(f'#{t+1}',r)
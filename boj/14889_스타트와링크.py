from itertools import combinations as cb
n = int(input())//2;m = 2*n
stat = [list(map(int,input().split())) for _ in range(m)]
newscore = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
allscore = sum(newscore)//2;p=[]
for l in cb(newscore[:-1],n):
    p.append(abs(allscore-sum(l)))
print(min(p))


from itertools import combinations as cb
n=int(input())
r=range(n)
a=[list(map(int,input().split()))for _ in r]
cs=[set(c) for c in cb(r,n//2)]
p=[]
for c in cs[:len(cs)//2]:
    p.append(abs(sum([a[i][j]+a[j][i]for i,j in cb(c,2)])-sum([a[i][j]+a[j][i]for i,j in cb(set(r).difference(c),2)])))
print(min(p))


from itertools import combinations as cb
def f(c):
    i,j=c
    return m[i][j]+m[j][i]
n=int(input())
m=[[*map(int,input().split())]for _ in range(n)]
print(min(abs(sum(map(f,cb(i,2)))-sum(map(f,cb({*range(n)}-{*i},2)))) for i in cb(range(n),n//2)))
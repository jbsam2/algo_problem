from itertools import permutations as perm
def _rotate(a,r,c,s):
    for ss in range(1,s+1):
        x,y,tmp=r-ss,c-ss,a[r-ss][c-ss]
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            for _ in range(ss*2):a[x][y]=a[x+dx][y+dy];x,y=x+dx,y+dy
        a[r-ss][c-ss+1]=tmp
def rotate(a,q):
    a=[x[:]for x in a]
    for r,c,s in q:_rotate(a,r-1,c-1,s)
    return min(map(sum,a))
def l():return map(int,input().split())
n,m,k=l()
a=[[*l()]for _ in range(n)]
r=[[*l()]for _ in range(k)]
print(min(rotate(a,p)for p in perm(r)))
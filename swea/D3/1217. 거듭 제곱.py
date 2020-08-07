def c(n,m):
    if m==1:return n
    return n*c(n,m-1)
for t in range(10):
    a=input();n,m=map(int,input().split());print(f'#{t+1}',c(n,m))
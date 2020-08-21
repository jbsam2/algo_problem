def sol(h,i):
    global a
    if h>=b:a=min(a,h);return
    if i>n-1:return
    sol(h,i+1);sol(h+l[i],i+1)
for t in range(int(input())):
    a=1<<32;n,b=map(int,input().split());l=list(map(int,input().split()));sol(0,0);print(f'#{t+1}',a-b)
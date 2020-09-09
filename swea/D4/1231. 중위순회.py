def sol(n):
    global a
    if k[2*n]:sol(2*n)
    a+=k[n]
    if k[2*n+1]:sol(2*n+1)
for t in range(10):
    n=int(input());k=[0]*101;a=''
    for _ in range(n):l=input().split();k[int(l[0])]=l[1]
    sol(1);print(f'#{t+1}',a)
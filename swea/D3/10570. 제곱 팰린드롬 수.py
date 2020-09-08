def c(num):return 1 if num==int(num**(0.5))**2 else 0
for t in range(int(input())):
    a,b=map(int,input().split());ans=0
    for i in range(a,b+1):
        p=int(i**(0.5))
        if c(i) and str(i)==str(i)[::-1] and str(p)==str(p)[::-1]:ans+=1
    print(f'#{t+1}',ans)
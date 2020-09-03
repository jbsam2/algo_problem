def sol(k, used):
    global cnt
    if k==n:
    	cnt+=1
    	return
    for i in range(n):
        if used&(1<<i):
        	continue
        for j in range(k):
            if k-j==abs(i-c[j]):
            	break
        else:
            c[k]=i
            sol(k+1,used|(1<<i))

for t in range(int(input())):
    n=int(input())
    cnt=0
    c=[0]*n
    sol(0,0)
    print(f'#{t+1}',cnt)
def sol(i):
    global cnt
    if i<=n:sol(2*i);tree[i]=cnt;cnt+=1;sol(2*i+1)

for t in range(int(input())):n=int(input());tree=[0 for _ in range(n+1)];cnt=1;sol(1);print('#{}'.format(t+1),tree[1],tree[n//2])
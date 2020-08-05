def sol(n):
    if n==1:return 1
    if n==2:return 3
    return sol(n-1)+2*sol(n-2)
for t in range(int(input())):print(f'#{t+1}',sol(int(input())//10))
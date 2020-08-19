l=[list(map(int,input().split()))for i in range(int(input()))]
print(*[sum(c>a and b<d for c,d in l)+1for a,b in l])
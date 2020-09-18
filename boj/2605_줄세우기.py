a=[i+1 for i in range(int(input()))]
for i,j in enumerate(map(int,input().split())):a.insert(i-j,a.pop(i))
print(*a)
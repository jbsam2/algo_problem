n,m = map(int,input().split())
boxes = [*map(int,input().split())]
l = [i for i in range(n-1,-1,-1)]
for i in range(n-1):
    cnt = 0
    for j in range(i+1,n):
        if boxes[j] >= boxes[i]:
            cnt += 1
    l[i] -= cnt
print(max(l))
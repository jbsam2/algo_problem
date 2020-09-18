b=[[0]*101 for _ in range(101)]
for _ in range(int(input())):
    a,c=map(int,input().split())
    for i in range(a,a+10):
        for j in range(c,c+10):b[i][j]=1
print(sum(sum(b,[])))
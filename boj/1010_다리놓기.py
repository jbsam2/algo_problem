p=[[1 for a in range(i)] for i in range(1,32)]
for i in range(2,31):
    for j in range(1,i):p[i][j]=p[i-1][j-1]+p[i-1][j]
for t in range(int(input())):m,n=map(int,input().split());print(p[n][m])
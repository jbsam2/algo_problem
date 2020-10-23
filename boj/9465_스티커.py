for t in range(int(input())):
    n=int(input())
    s=[[0]*2 for _ in 'aa']
    for i in range(2):s[i]+=[*map(int,input().split())]
    for j in range(2,n+2):
        for i in range(2):s[i][j]+=max(s[(i+1)%2][j-1],s[0][j-2],s[1][j-2])
    print(max(s[0][n+1],s[1][n+1]))
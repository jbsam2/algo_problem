s,t=input(),input()
n,m=len(s),len(t)
d=[[0]*(m+1) for x in range(n+1)]
for i in range(n):
    for j in range(m):
        if s[i]==t[j]:d[i][j]=1+d[i-1][j-1]
        else:d[i][j]=max(d[i-1][j],d[i][j-1])
print(d[n-1][m-1])
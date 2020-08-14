p=[[1 for a in range(i)] for i in range(1,102)];d=1000000007
for i in range(2,101):
    for j in range(1,i):p[i][j]=p[i-1][j-1]+p[i-1][j]
c=[[0 for i in range(101)]for j in range(101)]
def s(m,n):
    if m==1:c[1][n]=1;return c[1][n]
    if c[m][n]:return c[m][n]
    c[m][n]=(m**n)%d;r=0
    for i in range(1,m):r=(r+p[m][i]*s(m-i,n)%d)%d
    c[m][n]=(c[m][n]-r)%d
    return c[m][n]
for t in range(int(input())):m,n=map(int,input().split());print(f'#{t+1}',s(m,n))
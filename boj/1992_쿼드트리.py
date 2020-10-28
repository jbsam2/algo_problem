def s(y,x,n):
    c=b[y][x]
    for i in range(n):
        for j in range(n):
            if c!=b[y+i][x+j]:c=2
    if c!=2:return c
    else:d=n//2;return '('+s(y,x,d)+s(y,x+d,d)+s(y+d,x,d)+s(y+d,x+d,d)+')'
n=int(input())
b=[input()for _ in range(n)]
print(s(0,0,n))
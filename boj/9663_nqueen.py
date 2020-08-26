c1=[0]*15;c2=[0]*30;c3=[0]*30
def sol(y):
    if y==n:return 1
    sum=0
    for i in range(n):
        if c1[i] or c2[y+i] or c3[y-i+n]:continue
        c1[i]=c2[y+i]=c3[y-i+n]=1
        sum+=sol(y+1)
        c1[i]=c2[y+i]=c3[y-i+n]=0
    return sum

n=int(input());print(sol(0))
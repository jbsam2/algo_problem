from itertools import combinations as cb
for t in range(int(input())):
    n=int(input());l=[[*map(int,input().split())]for _ in range(n)];a=[sum(i)+sum(j)for i,j in zip(l,zip(*l))];b=sum(a)//2;p=[]
    for i in cb(a,n//2):p+=[abs(b-sum(i))]
    print(f'#{t+1}',min(p))

##########################################################################################################################################

def sol(a,b,k):
    global r,A,B
    if k==n:r=min(r,abs(a-b))
    else:
        if len(A)<n//2:
            A+=[k];p=0
            for i in A:p+=l[i][k]+l[k][i]
            sol(a+p,b,k+1);A.pop()
        if len(B)<n//2:
            B+=[k];p=0
            for i in B:p+=l[i][k]+l[k][i]
            sol(a,b+p,k+1);B.pop()
for t in range(int(input())):n=int(input());l=[[*map(int,input().split())]for _ in range(n)];A=[];B=[];r=1<<32;sol(0,0,0);print(f'#{t+1}',r)

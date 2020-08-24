def vs(a,b):
    if l[a-1]<l[b-1]:
        if l[a-1]==1 and l[b-1]==3:return a
        else:return b
    else:
        if l[a-1]==3 and l[b-1]==1:return b
        else:return a

def sol(a, b):
    if a==b:return a
    f=sol(a,(a+b)//2)
    s=sol((a+b)//2+1,b)
    return vs(f,s)

for t in range(int(input())):
    input();l=list(map(int,input().split()));print(f'#{t+1}',sol(1,len(l)))
def chk(p,i):
    global r
    if p%2:tmp=a
    else:tmp=b
    if tmp[i]>2:r=p
    if i<8 and tmp[i] and tmp[i+1] and tmp[i+2]:r=p
    if i>1 and tmp[i] and tmp[i-1] and tmp[i-2]:r=p
    if 0<i<9 and tmp[i-1] and tmp[i] and tmp[i+1]:r=p

for t in range(int(input())):
    c=[*map(int,input().split())];a=[0]*10;b=[0]*10;r=0
    for i in range(12):
        if i%2:b[c[i]]+=1;chk(2,c[i])
        else:a[c[i]]+=1;chk(1,c[i])
        if r:break
    print(f'#{t+1}',r)
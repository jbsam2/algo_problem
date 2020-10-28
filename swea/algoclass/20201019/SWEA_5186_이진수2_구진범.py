def b(n):
    r='';cnt=0
    while 1:
        m=n*2;r+=str(int(m));n=m-int(m);cnt+=1
        if n==0.0:return r
        if cnt>13:return 'overflow'
for t in range(int(int(input()))):print('#{}'.format(t+1),b(float(input())))
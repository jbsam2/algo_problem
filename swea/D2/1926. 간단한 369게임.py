for n in range(1,int(input())+1):
    t=str(n);c=0
    for i in t:
        if i in '369':c+=1
    if c:print('-'*c,end=' ')
    else:print(t,end=' ')
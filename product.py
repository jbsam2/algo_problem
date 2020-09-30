def solution(n, need, make):
    store=0;cost=100;days=n;rev=0
    for i in range(n):
        if cost<25:days=i;break
        store+=make[i]
        if need[i]<=store:
            rev+=cost*need[i]
            cost=100
        else:cost//=2
    return '%0.2f'%(rev/days)
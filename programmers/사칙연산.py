def solution(arr):
    arrs=''.join(arr).split('-')
    val0=sum(list(map(int,arrs[0].split('+'))))
    if len(arrs)==1:return val0
    min_val=max_val=0
    for arr in arrs[:0:-1]:
        x=list(map(int,arr.split('+')))
        _min=-(sum(x))
        _max=sum(x[1:])-x[0]
        min_val,max_val=min(_min+min_val,_min-max_val),max(_max+max_val,_min-min_val)
    return val0+max_val
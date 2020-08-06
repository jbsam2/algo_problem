for t in range(10):
    n,s=input().split();r=[]
    for i in s:
        if len(r)==0:r.append(i)
        else:
            if i==r[-1]:r.pop()
            else:r.append(i)
    print(f'#{t+1}',''.join(r))
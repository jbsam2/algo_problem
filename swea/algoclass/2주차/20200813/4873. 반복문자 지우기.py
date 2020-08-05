for t in range(int(input())):
    s=input();p=[]
    for i in s:
        if len(p)==0:p.append(i)
        elif i!=p[-1]:p.append(i)
        else:p.pop()
    print(f'#{t+1}',len(p))
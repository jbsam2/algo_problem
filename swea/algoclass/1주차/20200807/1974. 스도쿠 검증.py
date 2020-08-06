def k(l) :
    for i in range(1,10) :
        if not l.count(i)==1:return 0
    return 1
for t in range(int(input())) :
    r=[];s=[];c=[];a=1
    for i in range(9):c.append([]);s.append([])
    for i in range(9):
        r.append(list(map(int,input().split())))
        for j in range(9):c[j].append(r[i][j]);s[j//3*3+i//3].append(r[i][j])
    for i in range(9):
        if k(c[i])and k(r[i])and k(s[i]):continue
        else:a=0;break
    print(f'#{t+1}',a)
    print()
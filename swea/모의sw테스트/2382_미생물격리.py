for t in range(int(input())):
    n,m,k = map(int,input().split());b = {}
    for _ in range(k):a = [*map(int,input().split())];b[(a[0],a[1])]=(a[2],a[3])
    for _ in range(m):
        new_b = {}
        over = {}
        for pos, val in b.items():
            y,x = pos[0], pos[1]
            num, d = val[0], val[1]
            if d == 1:y-=1
            elif d == 2:y+=1
            elif d == 3:x-=1
            else:x+=1
            
            if y == 0 or y == n-1 or x == 0 or x == n-1:
                num//=2
                if d == 1:d=2
                elif d == 2:d=1
                elif d == 3:d=4
                else:d=3
            if num==0:continue
            if new_b.get((y,x)):
                if over.get((y,x)):
                    over[(y,x)]+=[[num,d]]
                else:
                    over[(y,x)]=[[*new_b[(y,x)]],[num,d]]
            else:
                new_b[(y,x)] = (num,d)
        for i in over:
            num, d = zip(*over[i])
            new_b[i] = (sum(num),d[num.index(max(num))])
        b = new_b
    ret = 0
    for i in [*b.values()]:ret+=i[0]
    print(f'#{t+1}',ret)
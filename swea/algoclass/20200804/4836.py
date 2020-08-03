for t in range(int(input())):
    n = int(input());r = [];b = []
    for i in range(n):
        y1, x1, y2, x2, color = map(int,input().split())
        for y in range(y1,y2+1):
            for x in range(x1,x2+1):
                if color == 1:
                    r.append((y,x))
                elif color == 2:
                    b.append((y,x))

    result = []
    if len(r) > len(b):
        for i in b:
            if i in r:
                result.append(i)

    if len(r) < len(b):
        for i in r:
            if i in b:
                result.append(i)

    print('#{t+1}',len(result)))
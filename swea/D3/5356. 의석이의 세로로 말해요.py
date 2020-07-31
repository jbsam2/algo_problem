for t in range(1,int(input())+1):
    map = []
    for i in range(5):
        map.append(input())
    max_len = 0
    for i in map:
        if len(i) > max_len:
            max_len = len(i)
    b = ''
    for i in range(max_len):
        for j in map:
            if len(j) <= i:
                continue
            b += j[i]
    print(f'#{t} {b}')
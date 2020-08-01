for t in range(1,int(input())+1):
    map = []
    max_len = 0
    for i in range(5):
        tmp = input()
        map.append(tmp)
        if len(tmp) > max_len:
            max_len = len(tmp)
    b = ''
    for i in range(max_len):
        for j in map:
            if len(j) <= i:
                continue
            b += j[i]
    print(f'#{t} {b}')
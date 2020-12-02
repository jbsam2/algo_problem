def my_func(line):
    h = line[0]
    straight_before_up = 1
    straight_after_down = 0
    for i in range(1, len(line)):
        # 직진
        if line[i] == h:
            if straight_after_down:
                straight_after_down -= 1
            else:
                straight_before_up += 1
        # 오름
        elif line[i] == h + 1 and straight_before_up >= x:
            h += 1
            straight_before_up = 1
        # 내림
        elif line[i] == h - 1 and not straight_after_down:
            h -= 1
            straight_after_down = x - 1
            straight_before_up = 0
        else:  # 불가능
            return 0	
    # Fig.7처럼 맵 밖으로 삐져나옴
    if straight_after_down:
        return 0  # 불가능
    return 1  # 가능

for t in range(int(input())):
    n, x = map(int, input().split())
    b = [[*map(int, input().split())] for _ in range(n)]
    ret = 0
    # 가로
    for line in b:
        ret += my_func(line)
    # 세로
    for line in zip(*b):
        ret += my_func(line)

    print(f'#{t+1}',ret)
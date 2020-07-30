t = int(input())

for tc in range(1,t+1):
    n = input()
    tmp_set = set()
    tmp_num = int(n)
    while 1:
        for num in n:
            tmp_set.add(num)
        if len(tmp_set) == 10:
            break
        n = str(int(n) + tmp_num)
    print(f'#{tc} {n}')
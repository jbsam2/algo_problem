t = int(input())

for tc in range(1,t+1):
    num = int(input())
    ret = 0
    for i in range(1,num+1):
        if i % 2:
            ret += i
        else:
            ret -= i
    print(f'#{tc} {ret}')
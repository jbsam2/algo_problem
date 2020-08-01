for t in range(1,int(input())+1):
    ans = 0
    tmp = 0
    for i,j in enumerate(input()):
        if tmp >= i:
            tmp += int(j)
        elif int(j):
            ans += i-tmp
            tmp += i-tmp+int(j)
        else:
            continue
    print(f'#{t} {ans}')
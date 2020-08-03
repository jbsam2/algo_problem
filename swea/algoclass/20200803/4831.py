for t in range(int(input())):
    k,n,m=map(int,input().split())
    s=list(map(int,input().split()))
    s_lst = [0]*(n+1)

    for i in range(len(s)):
        s_lst[s[i]] = 1

    cnt=0
    pos=0
    pos2=k
    
    while 1:
        if pos2 >= n:
            print(f'#{t+1}',cnt)
            break
        if s_lst[pos2]:
            cnt += 1
            pos = pos2
            pos2 += k
        else:
            pos2 -= 1
            if pos2 == pos:
                print(f'#{t+1}',0)
                break
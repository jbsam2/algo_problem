for _ in range(int(input())):
    a=[*map(int,input().split())];b=[*map(int,input().split())]
    sa=[a[1:].count(i)for i in range(4,0,-1)];sb=[b[1:].count(i)for i in range(4,0,-1)]
    for i in range(4):
        if sa[i]>sb[i]:print('A');break
        elif sb[i]>sa[i]:print('B');break
    else:print('D')
for t in range(1,int(input())+1):
    n = int(input())
    c = list(input().split())
    if len(c)%2:
        c1 = c[:(len(c)//2)+1]
        c2 = c[(len(c)//2)+1:]
    else:
        c1 = c[:len(c)//2]
        c2 = c[len(c)//2:]
    ret = ''
    for i in range(len(c2)):
        ret += c1[i] + ' ' + c2[i] + ' '
    if len(c) % 2:
        ret += c1[-1]
    print(f'#{t}',ret)
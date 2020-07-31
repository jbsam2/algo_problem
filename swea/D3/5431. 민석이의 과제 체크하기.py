for t in range(1,int(input())+1):
    ret = ''
    n,k = map(int,input().split())
    good = list(map(int,input().split()))
    for i in range(1,n+1):
        if i not in good:
            ret += str(i) + ' '
    print(f'#{t} {ret}')
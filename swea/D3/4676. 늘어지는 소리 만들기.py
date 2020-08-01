for t in range(1,int(input())+1):
    s = list(input())
    h = int(input())
    posi = list(map(int,input().split()))
    posi.sort(reverse=True)
    for i in posi:
        s.insert(i,'-')
    print(f'#{t}',end=' ')
    for i in s:
        print(i,end='')
    print()
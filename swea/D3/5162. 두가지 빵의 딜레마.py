for t in range(1,int(input())+1):
    a,b,c = map(int,input().split())
    print(f'#{t} {c//min(a,b)}')
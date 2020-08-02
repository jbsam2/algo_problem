for t in range(1,int(input())+1):
    n=input().split()
    a=sum(sorted(list(map(int,input().split())))[-int(n[1]):])
    print(f'#{t} {a}')
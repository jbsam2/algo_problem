for t in range(int(input())):
    n=int(input())
    num=list(map(int,input().split()))
    print(f'#{t+1}',max(num)-min(num))
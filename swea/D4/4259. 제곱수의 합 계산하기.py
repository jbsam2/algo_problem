for t in range(int(input())):
    input();r=0
    for i in input().split():r+=int(i[:-1])**int(i[-1])
    print(f'#{t+1}',r)
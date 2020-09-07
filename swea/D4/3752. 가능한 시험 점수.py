for t in range(int(input())):
    input();a=1
    for i in map(int,input().split()):a|=a<<i
    print(f'#{t+1}',bin(a).count('1'))
for t in range(int(input())):
    input();s=map(int,input().split());a=1
    for i in s:a|=a<<i
    print(f'#{t+1}',bin(a).count('1'))
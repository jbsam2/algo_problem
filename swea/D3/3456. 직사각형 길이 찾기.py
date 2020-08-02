for t in range(1,int(input())+1):
    e=input().split()
    for i in e:
        if e.count(i)%2:print(f'#{t} {i}');break
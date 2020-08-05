for t in range(int(input())):
    c='0';a=0
    for i in input():
        if i!=c:a+=1;c=i
    print(f'#{t+1}',a)
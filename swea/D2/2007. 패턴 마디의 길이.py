for t in range(int(input())):
    s=input();r=0
    for i in range(1,11):
        a=s[0:i];b=s[i:2*i]
        if a==b:r=i;break
    print(f'#{t+1}',r)
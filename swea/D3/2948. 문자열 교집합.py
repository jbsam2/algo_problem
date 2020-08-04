for t in range(int(input())):
    n=input();a=sorted(list(input().split()));b=sorted(list(input().split()));c=0
    while 1:
        if len(a)*len(b)==0:break
        if a[-1]>b[-1]:a.pop();continue
        if a[-1]<b[-1]:b.pop();continue
        c+=1;a.pop();b.pop()
    print(f'#{t+1}',c)
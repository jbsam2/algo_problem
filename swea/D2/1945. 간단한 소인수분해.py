for t in range(int(input())):
    l=[2,3,5,7,11];r=[];n=int(input())
    for i in l:
        c=0
        while n%i==0:n/=i;c+=1
        r.append(c)
    print(f'#{t+1}',*r)
for t in range(int(input())):
    c='croak';l=[i for i in input()];r=0
    while l:
        i=j=0
        while i<=len(l)-1:
            if l[i]==c[j%5]:del l[i];j+=1
            else:i+=1
        if j%5 or j==0:r=-1;break
        else:r+=1
    print(f'#{t+1}',r)
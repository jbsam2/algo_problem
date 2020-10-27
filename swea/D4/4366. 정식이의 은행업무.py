for t in range(int(input())):
    b=[*input()];d=[*input()];c=0
    for i in range(2*len(b)):
        p=b[:];p[i//2]=str(i%2);a=''.join(p)
        for j in range(3*len(d)):
            e=d[:];e[j//3]=str(j%3);f=''.join(e)
            if int(a,2)==int(f,3):print(f'#{t+1}',int(a,2));c=1;break
        if c:break
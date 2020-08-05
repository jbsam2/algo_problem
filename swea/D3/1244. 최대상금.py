def sol(c):
    global r
    if c==0:p=int(''.join(s));r=max(r,p);return
    for i in range(l):
        for j in range(i+1,l):
            s[i],s[j]=s[j],s[i];p=''.join(s)
            if chk.get((p,c-1),1):chk[(p,c-1)]=0;sol(c-1)
            s[i],s[j]=s[j],s[i]


for t in range(int(input())):
    n,c=input().split();r=0;s=list(n);c=int(c);l=len(s);chk={};sol(c)
    print(f'#{t+1}',r)
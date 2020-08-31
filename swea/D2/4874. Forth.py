for t in range(int(input())):
    l=list(input().split());s=[];c=1
    for i in range(len(l)-1):  
        if l[i].isdigit():s.append(l[i])
        else:
            try:
                a,b=int(s.pop()),int(s.pop())
                if l[i]=='+':r=b+a
                elif l[i]=='-':r=b-a
                elif l[i]=='/':r=b//a
                elif l[i]=='*':r=b*a
                s.append(str(r))
            except:c=0;break
    if c and len(s)==1:
        print(f'#{t+1}',s[0])
    elif c==0 or len(s)>1:
        print(f'#{t+1} error')
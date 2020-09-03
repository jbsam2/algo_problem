for _ in range(int(input())):
    sm,sc,si=map(int,input().split());code=input();string=[*map(ord,input())]+[255];jump={};tmp=[];mem=[0]*sm;pm=pc=pi=cnt=0;st=[]
    for i in range(sc):
        if code[i]=='[':tmp.append(i)
        elif code[i]==']':s=tmp.pop();jump[i]=s;jump[s]=i    
    while cnt<50000000:
        cnt+=1
        if pc>=sc:break
        if code[pc]=='-':mem[pm]=(mem[pm]-1)%256;pc+=1
        elif code[pc]=='+':mem[pm]=(mem[pm]+1)%256;pc+=1
        elif code[pc]=='<':pm=(pm-1)%sm;pc+=1
        elif code[pc]=='>':pm=(pm+1)%sm;pc+=1
        elif code[pc]=='[':
            if mem[pm]==0:pc=jump[pc]+1
            else:st.append(pc);pc+=1
        elif code[pc]==']':
            if mem[pm]:pc=jump[pc]+1
            else:st.pop();pc+=1
        elif code[pc]=='.':pc+=1
        elif code[pc]==',':
            mem[pm]=string[pi]
            if pi<si:pi+=1
            pc+=1
    else:print(f'Loops {st[0]} {jump[st[0]]}');continue
    print('Terminates')
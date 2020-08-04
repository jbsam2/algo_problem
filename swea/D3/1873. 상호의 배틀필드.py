for t in range(int(input())):
    dx=[0,0,-1,1];dy=[-1,1,0,0];move='^v<>';key_dir={'U':0,'D':1,'L':2,'R':3};b=[]
    h,w=map(int,input().split())
    for i in range(h):
        b.append([*input()])
        for j in range(w):
            if b[i][j] in move:y,x=i,j;d=move.find(b[i][j])
    n=int(input()); opers=input()
    for oper in opers:
        if oper=='S':
            p,q=y+dy[d],x+dx[d]
            while -1<p<h and -1<q<w:
                if b[p][q]=='#':break
                if b[p][q]=='*':b[p][q]='.';break
                p+=dy[d];q+=dx[d]
        else:
            D=key_dir[oper];p,q=y+dy[D],x+dx[D]
            if -1<p<h and -1<q<w and b[p][q]=='.':b[y][x],b[p][q]='.',move[D];y,x=p,q;d=D
            else:b[y][x]=move[D];d=D
    print(f'#{t+1}',end=' ')
    for i in b:print(''.join(i))
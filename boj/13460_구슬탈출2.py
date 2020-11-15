n,m=map(int,input().split())
b=[input()for _ in range(n)]
def l(x,y,dx,dy,c=0):
    while b[y+dy][x+dx]!='#' and b[y][x]!='O':x+=dx;y+=dy;c+=1
    return y,x,c
def sol():
    for y,r in enumerate(b):
        for x,c in enumerate(r):
            if c=='R':rx,ry=x,y
            if c=='B':bx,by=x,y
    q=[[rx,ry,bx,by,1]];v=[(rx,ry,bx,by)];d=[(0,1),(0,-1),(-1,0),(1,0)]
    while q:
        t=q.pop(0);rx,ry,bx,by=t[0],t[1],t[2],t[3]
        if t[4]>10:break
        for i in d:
            rny,rnx,rcnt=l(rx,ry,i[0],i[1]);bny,bnx,bcnt=l(bx,by,i[0],i[1])
            if (rnx,rny,bnx,bny) in v:continue
            if b[bny][bnx]!='O':
                if b[rny][rnx]=='O':print(t[4]);return
                if bnx==rnx and bny==rny:
                    if rcnt>bcnt:rnx-=i[0];rny-=i[1]
                    else:bnx-=i[0];bny-=i[1]
                v+=[(rnx,rny,bnx,bny)];q+=[[rnx,rny,bnx,bny,t[4]+1]]
    print(-1)
sol()
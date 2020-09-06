def possi(x,y,is_b,b,p):
    if is_b:return (p[x][y-1] or p[x+1][y-1]) or (x>=1 and b[x-1][y] and b[x+1][y])
    else:return y==0 or (x>=1 and b[x-1][y]) or b[x][y] or p[x][y-1]
def install(x,y,is_b,b,p,is_install):
    if is_b:b[x][y]=is_install
    else:p[x][y]=is_install
def chk(res,b,p):
    for x,y,is_b in res:
        if not possi(x,y,is_b,b,p):return 0
    return 1
def solution(n,build_frame):
    res=[];b=[[0]*(n+1)for _ in range(n+1)];p=[[0]*(n+1)for _ in range(n+1)]
    for x,y,is_b,is_install in build_frame:
        if is_install:
            if possi(x,y,is_b,b,p):install(x,y,is_b,b,p,1);res.append([x,y,is_b])
        else:
            install(x,y,is_b,b,p,0)
            if chk(res,b,p):res.remove([x,y,is_b])
            else:install(x,y,is_b,b,p,1)
    return sorted(res,key=lambda x:(x[0],x[1],x[2]))
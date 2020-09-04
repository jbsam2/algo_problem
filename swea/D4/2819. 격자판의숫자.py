dx=[0,0,1,-1];dy=[1,-1,0,0]
def s(y,x,l):
    if len(l)==7:a.add(l);return
    for i in range(4):
        nx=x+dx[i];ny=y+dy[i]
        if -1<nx<4 and -1<ny<4:s(ny,nx,l+b[y][x])
for t in range(int(input())):
    b=[[*input().split()]for _ in '1'*4];a=set()
    for y in range(4):
        for x in range(4):s(y,x,'')
    print('#{}'.format(t+1),len(a))
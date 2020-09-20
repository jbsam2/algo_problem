for _ in range(4):
    l=[*map(int,input().split())];x1=max(l[0],l[4]);x2=min(l[2],l[6]);y1=max(l[1],l[5]);y2=min(l[3],l[7])
    if x1<x2 and y1<y2:print('a')
    elif x1<=x2 and y1<=y2:print('b' if (x1,y1)!=(x2,y2) else 'c')
    else:print('d')
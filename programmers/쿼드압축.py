def f(x,y,l,a):
    p=a[x][y];t=0
    for i in range(l):
        for j in range(l):
            if a[x+i][y+j]!=p:t=1;break
        if t:break
    if t:l//=2;return f(x,y,l,a)+f(x,y+l,l,a)+f(x+l,y,l,a)+f(x+l,y+l,l,a)
    else:return str(p)
def solution(arr):k=f(0,0,len(arr),arr);return [k.count('0'),k.count('1')]
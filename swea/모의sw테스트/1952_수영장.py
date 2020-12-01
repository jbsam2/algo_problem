def sol(prev,total):
    global ret
    if prev >= 12:
        ret = min(ret, total)
        return
    elif total >= ret:
        return
    for i, price in enumerate(pl):
        if i == 0:
            sol(prev+1, total+plan[prev]*price)
        elif i == 1:
            sol(prev+1, total+price)
        elif i == 2:
            sol(prev+3, total+price)

for t in range(int(input())):
    pl = [*map(int,input().split())]
    plan = [*map(int,input().split())]
    ret = 1<<32
    a = pl[3]
    pl = pl[:3]
    sol(0,0)
    print(f'#{t+1}',min(ret,a))
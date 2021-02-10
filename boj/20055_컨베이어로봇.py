n, k = map(int,input().split())
a = [*map(int,input().split())]
ret = cnt = up = 0
robot = [0] * n
while cnt < k:
    ret += 1
    up = (up - 1 + 2 * n) % (2 * n)
    robot.insert(0, 0)
    robot.pop()
    robot[-1] = 0
    for i in range(n-2, 0, -1):
        pos = (i + 1 + up) % (2 * n)
        if robot[i] and a[pos] and robot[i+1] == 0:
            a[pos] -= 1
            robot[i] = 0
            robot[i+1] = 1
            if a[pos] == 0:
                cnt += 1
    if a[up]:
        robot[0] = 1
        a[up] -= 1
        if a[up] == 0:
            cnt += 1
print(ret)
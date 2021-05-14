times = sorted([int(input())for _ in range(int(input()))])

left = len(times)
ret = 0
path = []
s = 0
e = left - 1
while left > 3:
    path.append([times[0],times[1]])
    left -= 2
    ret += times[1]

    path.append([times[0]])
    left += 1
    ret += times[0]

    path.append([times[e-1],times[e]])
    left -= 2
    ret += times[e]

    path.append([times[1]])
    left += 1
    ret += times[1]

    e -= 2

if left == 3:
    path.append([times[0],times[1]])
    path.append([times[0]])
    path.append([times[0],times[2]])
    left -= 3
    ret += times[1] + times[0] + times[2]

if left == 2:
    path.append([times[0],times[1]])
    ret += times[1]
    left -= 2

print(ret)
for i in path:print(*i)
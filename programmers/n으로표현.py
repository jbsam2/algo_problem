def solution(N, number):
    if N==number:return 1
    a=[set() for i in range(8)]
    for i in range(8):a[i].add(int(str(N)*(i+1)))
    for i in range(1,8):
        for j in range(i):
            for k in a[j]:
                for l in a[i-j-1]:
                    a[i].add(k+l);a[i].add(k-l);a[i].add(k*l)
                    if l:a[i].add(k//l)
        if number in a[i]:
            return i+1
    else:return -1
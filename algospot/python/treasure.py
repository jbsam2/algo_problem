epsilon = 1e-9


def cross(a, b):
    return a.real*b.imag - b.real*a.imag


def ccw(a, b, c):
    return cross(b-a, c-a)


def line_intersection(a, b, c, d):
    det = cross(b-a, d-c)
    if abs(det) < epsilon:
        return False
    return a + (b - a) * (cross(c-a, d-c) / det)


def cut_poly(p, a, b):
    n = len(p)
    inside = [ccw(a, b, p[i]) >= 0 for i in range(n)]
    ret = []
    for i in range(n):
        j = (i+1) % n
        if inside[i]:
            ret.append(p[i])
        if inside[i] != inside[j]:
            c = line_intersection(p[i], p[j], a, b)
            ret.append(c)
    return ret


def intersection(p, x1, y1, x2, y2):
    a, b, c, d = x1+y1*1j, x2+y1*1j, x2+y2*1j, x1+y2*1j
    ret = cut_poly(p, a, b)
    ret = cut_poly(ret, b, c)
    ret = cut_poly(ret, c, d)
    ret = cut_poly(ret, d, a)
    return ret


def area(p):
    ret = 0
    for i in range(len(p)):
        ret += cross(p[i], p[(i+1) % len(p)])
    return abs(ret) / 2


for case in range(int(input())):
    x1, y1, x2, y2, N = map(int, input().split())
    island = (map(int, input().split()) for _ in range(N))
    island = [x + y*1j for x, y in island]

    print(area(intersection(island, x1, y1, x2, y2)))
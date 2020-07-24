def min_x(points):
    return min(x for x, y in points)


def max_x(points):
    return max(x for x, y in points)


def between(seg, x):
    x1, y1 = seg[0]
    x2, y2 = seg[1]
    return x1 <= x <= x2 or x2 <= x <= x1


def at(seg, x):
    x1, y1 = seg[0]
    x2, y2 = seg[1]
    return y1 + (y2-y1)/(x2-x1) * (x-x1)


def vertical(x):
    min_up = min(at(seg, x) for seg in upper if between(seg, x))
    max_lo = max(at(seg, x) for seg in lower if between(seg, x))
    return min_up - max_lo


def decompose(hull, lower, upper):
    for i in range(len(hull)):
        if hull[i-1][0] < hull[i][0]:
            lower.append((hull[i-1], hull[i]))
        elif hull[i-1][0] > hull[i][0]:
            upper.append((hull[i-1], hull[i]))


for case in range(int(input())):
    n, m = map(int, input().split())
    hull1 = map(float, input().split())
    hull2 = map(float, input().split())
    hull1 = list(zip(hull1, hull1))
    hull2 = list(zip(hull2, hull2))

    lower, upper = [], []
    decompose(hull1, lower, upper)
    decompose(hull2, lower, upper)

    lo = max(min_x(hull1), min_x(hull2))
    hi = min(max_x(hull1), max_x(hull2))
    if hi < lo:
        print(0)
        continue

    for _ in range(100):
        aab = (lo*2 + hi) / 3
        abb = (lo + hi*2) / 3
        if vertical(aab) < vertical(abb):
            lo = aab
        else:
            hi = abb

    print(max(0, vertical(hi)))

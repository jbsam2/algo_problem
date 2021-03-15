from collections import deque, defaultdict

def solution(sales, links):
    count = [0] * (len(sales) + 1)
    parent = [-1] * (len(sales) + 1)
    child = defaultdict(list)

    for p, c, in links:
        parent[c - 1] = p - 1
        count[p - 1] += 1

    q = deque(i for i, v in enumerate(count[:-1]) if v == 0)

    while q:
        i = q.popleft()
        p = parent[i]
        if i in child:
            sumv = sum(npick for _, npick in child[i])
            minv = min(min(pick - npick for pick, npick in child[i]), sales[i])
        else:
            sumv, minv = 0, 0
        child[p].append((sales[i] + sumv, minv + sumv))
        count[p] -= 1
        if count[p] == 0:
            q.append(p)

    return min(child[-1][0])




import functools

def solution(sales, links):
    @functools.lru_cache(maxsize=None)
    def min_sales(node, should_include_root):
        children_sum = sum(min_sales(c, False) for c in children[node])
        sales_including_root = sales[node] + children_sum
        if should_include_root:
            return sales_including_root
        sales_without_root = children_sum + min(
            (min_sales(c, True) - min_sales(c, False) for c in children[node]),
            default=0)
        return min(sales_including_root, sales_without_root)

    children = [[] for _ in sales]
    for a, b in links:
        children[a - 1].append(b - 1)
    return min(min_sales(0, True), min_sales(0, False))

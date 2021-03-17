import functools

def solution(sales, links):
    @functools.lru_cache(maxsize=None)
    def min_sales(node, should_include_root):
        children_sum = sum(min_sales(c, False) for c in children[node])
        sales_including_root = sales[node] + children_sum
        if should_include_root:
            return sales_including_root
        sales_without_root = children_sum + min((min_sales(c, True) - min_sales(c, False) for c in children[node]), default=0)
        return min(sales_including_root, sales_without_root)

    children = [[] for _ in sales]
    for a, b in links:
        children[a - 1].append(b - 1)
    return min(min_sales(0, True), min_sales(0, False))

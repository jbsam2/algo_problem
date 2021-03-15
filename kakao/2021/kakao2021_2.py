from collections import Counter
from itertools import combinations as cb

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += cb(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]
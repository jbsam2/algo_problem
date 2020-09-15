from itertools import permutations as p
def solution(numbers):
    s=set()
    for i in p(numbers,2):s.add(sum(i))
    return sorted(s)
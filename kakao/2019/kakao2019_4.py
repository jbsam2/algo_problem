from copy import deepcopy
def solution(food_times, k):
    if sum(food_times) <= k :
        return -1

    sort = sorted(deepcopy(food_times))
    i = 0
    while i != 0:i += 1

    k -= sort[i] * (len(sort) - i)
    while k > 0 :
        i += 1
        k -= (sort[i] - sort[i-1]) * (len(sort) - i)

    rounds = sort[i]
    while k < 0:
        rounds -= 1
        k += len(sort) - i

    answer = 0
    for i, val in enumerate(food_times):
        if val > rounds :
            if k <= 0 :
                return i + 1
            else :
                k -= 1

    return answer
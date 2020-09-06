def solution(food_times, k):
    k+=1;foods=sorted(enumerate(food_times),key=lambda x:x[1]);l=len(foods)
    for i in range(l):
        x=(l-i)*foods[i][1]-(foods[i-1][1]if i else 0)
        if x>=k:foods=sorted(foods[i:],key=lambda x:x[0]);return 1+(foods[(k%(l-i))-1][0] if k%(l-i) else foods[-1][0])
        else:k-=x
    return -1
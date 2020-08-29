def solution(food_times, k):
    k+=1;l=len(food_times);foods=sorted(enumerate(food_times),key=lambda x:x[1])    
    for i in range(l):
        x=l-i;x*=foods[i][1]-(foods[i-1][1]if i else 0)
        if x>=k:
            foods=sorted(foods[i:],key=lambda x:x[0])
            if k%(l-i)==0:return foods[-1][0]+1
            else: return foods[(k%(l-i))-1][0]+1
        else: k-=x
    return -1
from itertools import combinations as c
def check(a,b,c): 
    t=a+b+c
    for i in range(2,t): 
        if t%i==0:return 0
    return 1
def solution(nums):
    answer = 0
    for i in c(nums,3): 
        if check(i[0],i[1],i[2]):answer+=1
    return answer
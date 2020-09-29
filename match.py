nums=[6,2,5,5,4,5,6,3,7,6]
ret1 = 0
def s1(t,k):
    global ret1
    if t==k:ret1+=1;return
    if t>k:return
    for i in range(10):s1(t+nums[i],k)
ret2 = 0
def s2(t,k):
    global ret2
    if t==k:ret2+=1;return
    if t>k:return
    for i in range(10):s2(t+nums[i],k)

def solution(k):
    if k==1:return 0
    if k<=3:return 1
    s1(0,k)
    s2(0,k-6)
    return ret1-ret2

print(solution(6))
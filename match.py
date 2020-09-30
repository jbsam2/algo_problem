def solution(k):
    ret = [0,0,1,1,2,5,6,12]+[0]*105
    for i in range(8,112):ret[i]=ret[i-2]+ret[i-3]+ret[i-4]+3*ret[i-5]+3*ret[i-6]+ret[i-7]
    return ret[k]

ret=[0]*51
def s1(t,k):
    if t>k:return
    ret[t]+=1
    for i in nums:
        s1(t+i,k)

nums=[6,2,5,5,4,5,6,3,7,6]
def solution2(k):
    if k<=1:return 0
    if k<=3:return 1
    s1(0,k)
    return ret[k]-ret[k-6] if k>=6 else ret[k]


print('sol1',solution(15))
print('sol2',solution2(15))
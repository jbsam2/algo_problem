def nhand(rhand,lhand,num,mhand):
    r=abs(rhand[0]-num[0])+abs(rhand[1]-num[1])
    l=abs(lhand[0]-num[0])+abs(lhand[1]-num[1])
    if l>r:return 'right'
    elif r>l:return 'left'
    else:return mhand

def solution(numbers,hand):
    answer='';r=(0,0);l=(0,2)
    nums=((0,1),(3,0),(3,1),(3,2),(2,0),(2,1),(2,2),(1,0),(1,1),(1,2))
    for i in numbers:
        if i in [1,4,7]:answer+='L';l=nums[i]
        elif i in [3,6,9]:answer+='R';r=nums[i]
        else:
            t=nhand(r,l,nums[i],hand)
            if t=='right':answer+='R';r=nums[i]
            else:answer+='L';l=nums[i]    
    return answer
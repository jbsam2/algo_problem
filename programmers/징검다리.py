def solution(distance, rocks, n):
    answer = 0;rocks.sort();rocks.append(distance);l,r=0,distance
    while l<=r:
        pre=0;mins=1<<32;remove=0;mid=(l+r)//2
        for i in range(len(rocks)):
            if rocks[i]-pre<mid:remove+=1
            else:mins=min(mins,rocks[i]-pre);pre=rocks[i]
        if remove>n:r=mid-1
        else:answer=mins;l=mid+1
    return answer
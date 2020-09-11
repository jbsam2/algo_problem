def solution(cookie):
    answer = 0;n=len(cookie)-1
    for i in range(n):
        s1_val=cookie[i];s1_idx=i
        s2_val=cookie[i+1];s2_idx=i+1
        while 1:
            if s1_val==s2_val and s1_val>answer:answer=s1_val
            if s1_idx>0 and s1_val<=s2_val:s1_idx-=1;s1_val+=cookie[s1_idx]
            elif s2_idx<n and s1_val>=s2_val:s2_idx+=1;s2_val+=cookie[s2_idx]
            else:break
    return answer
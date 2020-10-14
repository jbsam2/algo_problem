def solution(s):
    if len(s)==1:return 0
    ans=0;cnt=1
    for i in range(len(s)-1,0,-1):ans+=i*cnt;cnt+=1
    idx=[[]for _ in range(26)]
    for i in range(len(s)):idx[ord(s[i])-ord('a')].append(i)
    for i in range(26):
        if len(idx[i])<2:continue
        series=[0]*(len(idx[i])+1)
        prev=idx[i][0]
        cnt=1
        for j in range(1,len(idx[i])):
            curr=idx[i][j]
            if curr-prev == 1:cnt+=1
            else:
                series[cnt]+=1
                cnt=1
            prev=curr
        series[cnt]+=1
        for j in range(1,len(idx[i])):
            cnt=0
            for k in range(j,len(series)):cnt+=series[k]*(k-j+1)
            if cnt==0:continue
            ans-=cnt*(cnt-1)//2
    return max(ans,0)
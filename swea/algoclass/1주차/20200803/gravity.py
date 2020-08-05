box=list(map(int,input().split()));ans=0
for i in range(len(box)-1):
    cnt = 0
    for j in range(i,len(box)):
        if box[i] > box[j]:
            cnt+=1
    ans = max(ans,cnt)
print(ans)
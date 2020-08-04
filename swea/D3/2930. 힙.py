import heapq
for t in range(int(input())):
    h = [];ret=''
    for i in range(int(input())):
        a=input()
        if len(a)>1:
            a=int(a[-1])
            heapq.heappush(h,(-a,a))
        else:
            if len(h):ret+=str(heapq.heappop(h)[-1])+' '
            else:ret+='-1'
    print(f'#{t+1}',ret)
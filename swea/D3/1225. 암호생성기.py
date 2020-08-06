import collections
for t in range(10):
    n=input();l=collections.deque(list(map(int,input().split())));r=''
    while l[-1]!=0:
        for i in range(5):
            tmp=l.popleft()
            if tmp-1-i>0:l.append(tmp-i-1)
            else:l.append(0);break
    for i in l:r+=str(i)+' '
    print(f'#{t+1}',r)
from collections import Counter
for t in range(int(input())):
    input();s=Counter(list(map(int,input().split())));m=max(s.values());l=0
    for i,v in s.items():
        if v==m and i>l:l=i  
    print(f'#{t+1}',l)
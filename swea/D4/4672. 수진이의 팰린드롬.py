from collections import Counter
for t in range(int(input())):
    r=0
    for i in Counter(input()).values():r+=(i*(i+1))//2
    print(f'#{t+1}',r)
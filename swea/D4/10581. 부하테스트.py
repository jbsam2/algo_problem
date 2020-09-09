import math
for t in range(int(input())):
    l,p,c=map(int, input().split())
    if l*c>p:print(f'#{t+1}',0);continue
    print(f'#{t+1}',math.ceil(math.log2(math.log(p/l,c))))
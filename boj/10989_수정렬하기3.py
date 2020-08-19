import sys;input();l=[0]*(10001)
for i in sys.stdin:l[int(i)]+=1
for i in range(10001):print(f'%s '%i*l[i],end='')
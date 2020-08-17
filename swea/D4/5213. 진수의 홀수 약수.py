a=[0]*1000001
for i in range(1,1000001,2):
    for j in range(i,1000001,i):a[j]+=i
for i in range(1,1000001):a[i]+=a[i-1]
for t in range(int(input())):l,r=map(int,input().split());print(f'#{t+1}',a[r]-a[l-1])
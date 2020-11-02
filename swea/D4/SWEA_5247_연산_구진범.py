from collections import deque
def cal(num,op):
    if op==0:return num+1
    elif op==1:return num-1
    elif op==2:return num*2
    elif op==3:return num-10

def sol(n):
    q=deque();q.append((n,0));nums[n]=1
    while q:
        num,cnt=q.popleft()
        for i in range(4):
            n_num=cal(num,i)
            if n_num==m:return cnt+1
            elif 0<n_num<1000001 and nums[n_num]==0:q.append((n_num,cnt+1));nums[n_num]=1

for t in range(int(input())):n,m=map(int,input().split());nums=[0]*1000001;print(f'#{t+1}',sol(n))
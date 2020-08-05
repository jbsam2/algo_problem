num=list(range(1,13));L=len(num);lst=[]
for i in range(1<<L):
    sub_lst=[]
    for j in range(L):
        if i&(1<<j):sub_lst.append(num[j])
    lst.append(sub_lst)

for t in range(int(input())):
    n,k=map(int, input().split());ret=0
    for i in lst:
        if len(i)==n and sum(i)==k:ret+=1
    print(f'#{t+1}',ret)
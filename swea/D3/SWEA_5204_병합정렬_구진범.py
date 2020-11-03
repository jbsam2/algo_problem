def mergesort(arr):
    if len(arr)==1:return arr
    m=len(arr)//2
    return merge(mergesort(arr[:m]),mergesort(arr[m:]))
def merge(l,r):
    global cnt
    l_n=len(l);r_n=len(r);ret=[];l_i=r_i=0
    if l[-1]>r[-1]:cnt+=1
    while l_i<l_n and r_i<r_n:
        if l[l_i]<=r[r_i]:ret.append(l[l_i]);l_i+=1
        else:ret.append(r[r_i]);r_i+=1
    if l_i<l_n:
        while l_i<l_n:ret.append(l[l_i]);l_i+=1
    if r_i<r_n:
        while r_i<r_n:ret.append(r[r_i]);r_i+=1
    return ret

for t in range(int(input())):n=int(input());cnt=0;a=mergesort([*map(int,input().split())]);print(f'#{t+1}',a[n//2],cnt)
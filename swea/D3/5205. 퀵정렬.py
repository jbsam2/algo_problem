def qsort(arr,l,r):
    if l<r:p=partition(arr,l,r);qsort(arr,l,p-1);qsort(arr,p+1,r)
def partition(arr, l, r):
    p=(l+r)//2
    while l<r:
        while(arr[l]<arr[p] and l<r):l+=1
        while(arr[r]>=arr[p] and l<r):r-=1
        if l<r:
            if l==p:p=r
            arr[l],arr[r]=arr[r],arr[l]
    arr[p],arr[r]=arr[r],arr[p]
    return r
for t in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    qsort(arr,0,n-1)
    print(f'#{t+1}',arr[n//2])
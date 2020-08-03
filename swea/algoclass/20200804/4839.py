def count(p,a):
    s=1;f=p;page=a;cnt=0
    while s<=f:
        mid=(s+f)//2
        if mid==page:
            break
        elif mid<page:
            s=mid
            cnt+=1
        else:
            f=mid
            cnt+=1
    return cnt

for t in range(int(input())):
    p,a,b=map(int,input().split())
    ret_a = count(p,a)
    ret_b = count(p,b)

    if ret_a < ret_b:
        print(f'#{t+1}','A')
    elif ret_a>ret_b:
        print(f'#{t+1}','B')
    else:
        print(f'#{t+1}',0)
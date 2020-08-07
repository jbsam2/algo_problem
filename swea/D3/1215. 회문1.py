def c(l,n):
    k=0
    for i in l:
        for j in range(9-n):
            if i[j:j+n]==i[j:j+n][::-1]:k+=1
    return k
for t in range(10):n=int(input());l=[input()for _ in range(8)];l+=list(zip(*l));print(f'#{t+1}',c(l,n))
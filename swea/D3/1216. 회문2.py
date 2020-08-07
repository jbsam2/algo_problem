def c(l):
    for k in range(100,0,-1):
        for i in l:
            for j in range(101-k):
                if i[j:j+k]==i[j:j+k][::-1]:return k
for t in range(10):input();l=[input()for _ in range(100)];l+=list(zip(*l));print(f'#{t+1}',c(l))
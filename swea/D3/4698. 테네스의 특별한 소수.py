prime = list(range(2, 1000000))
n = 2
while n < 1000000:
    if prime[n - 2] != 0:
        p = 2 * n - 2
        while p < 999998:
            prime[p] = 0
            p += n
    n += 1

prime_list = []
for i in prime:
    if i:
        prime_list.append(i)

for t in range(1,int(input())+1):
    d, a, b = map(int,input().split())
    ans = 0
    for i in prime_list:
        if i < a:
            continue
        elif i > b:
            break
        else:
            if str(d) in str(i):
                ans += 1
    print(ans)
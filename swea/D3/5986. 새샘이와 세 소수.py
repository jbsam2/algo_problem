prime = list(range(2, 1000))
n = 2
while n < 1000:
    if prime[n - 2]:
        p = 2 * n - 2
        while p < 998:
            prime[p] = 0
            p += n
    n += 1

prime_list = []
for i in prime:
    if i:
        prime_list.append(i)
 
ret = {}
for i in range(len(prime_list)):
    for i2 in range(i, len(prime_list)):
        for i3 in range(i2, len(prime_list)):
            tmp = prime_list[i] + prime_list[i2] + prime_list[i3]
            if tmp not in ret:
                ret[tmp] = 1
            else:
                ret[tmp] += 1
 
for t in range(1,int(input())+1):
    n = int(input())
    print(f'#{t} {ret[n]}')
cache = [0,1]
n = int(input())
for i in range(2,n+1):
    cache.append(cache[-1]+cache[-2])
print(cache[n])
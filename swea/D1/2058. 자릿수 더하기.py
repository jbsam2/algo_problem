T = int(input())
ans = 0
while T > 1:
    ans += T % 10
    T //= 10
print(ans)
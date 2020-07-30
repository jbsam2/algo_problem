t = int(input())

for tc in range(1,t+1):
    nums = list(map(int,input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    avg = round(sum(nums)/len(nums))
    print(f'#{tc} {avg}')
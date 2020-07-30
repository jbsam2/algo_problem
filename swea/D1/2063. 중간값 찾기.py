N = int(input())
tmp_list = list(map(int,input().split()))
tmp_list.sort()
print(tmp_list[N//2])
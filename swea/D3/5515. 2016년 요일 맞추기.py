days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
week = ['월', '화', '수', '목', '금', '토', '일']
for t in range(1,int(input())+1):
    m, d = map(int,input().split())
    w = (((sum(days[:m]) + d - 1) % 7) + 4) % 7
    print(f'#{t} {w}')
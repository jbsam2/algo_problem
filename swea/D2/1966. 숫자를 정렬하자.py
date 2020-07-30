for tc in range(1,int(input())+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    print(f'#{tc}',end=' ')
    for i in num_list:
        print(i,end=' ')
    print()
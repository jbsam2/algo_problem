t = int(input())

for tc in range(1,t+1):
    n = int(input())
    tmp_str = ''
    for i in range(n):
        tmp_char, tmp_value = input().split()
        tmp_str += tmp_char * int(tmp_value)
        
    print(f'#{tc}')
    cnt = 1
    for chars in tmp_str:
        print(chars,end='')
        if cnt % 10 == 0:
            print()
        cnt += 1
    print()
t = int(input())
for tc in range(1,t+1):
    input_str = input()
    ret = 0
    for str_len in range(1,11):
        tmp_str1 = input_str[0:str_len]
        tmp_str2 = input_str[str_len:2*str_len]
        if tmp_str1 == tmp_str2:
            ret =str_len
            break
    print(f'#{tc} {ret}')
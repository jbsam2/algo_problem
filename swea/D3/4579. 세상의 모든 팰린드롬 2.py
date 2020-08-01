for t in range(1,int(input())+1):
    s = input()
    ret = ''
    for i in range(len(s)//2):
        if s[i] == '*':
            ret = 'Exist'
            break
        if s[len(s)-1-i] == '*':
            ret = 'Exist'
            break
        if s[i] != s[len(s)-1-i]:
            ret = 'Not exist'
            break
    else:
        ret = 'Exist'
    print(f'#{t} {ret}')
for t in range(1,int(input())+1):
    a, b, c, d = map(int,input().split())
    if not b and not c:
        if not d and a: tmp = '0'*(a+1)
        elif not a and d: tmp = '1'*(d+1)
        else: tmp = 'impossible'
    elif abs(b-c) > 1: tmp = 'impossible'
    elif b-c == 1: tmp = '0'*a + '01'*b + '1'*d
    elif c-b == 1: tmp = '1'*d + '10'*c + '0'*a
    else: tmp = '0'*a +'01'*b + '1'*d +'0'
    print(f'#{t} {tmp}')
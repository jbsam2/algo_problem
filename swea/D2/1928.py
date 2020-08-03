v = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
base = {val: i for i, val in enumerate(v)}
def decoding(s):
    ret = ''
    bit = ''
    for i in s:
        num = bin(base[i])[2:].zfill(6)
        bit += num
 
    for i in range(0,len(bit),8):
        ret += chr(int(bit[i:i+8],2))
 
    return ret

for t in range(int(input())):
    print(f'#{t+1} {decoding(input())}')
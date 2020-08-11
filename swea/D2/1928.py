v='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
def s(n):
    r='';d=''
    for i in n:d+=bin(v.find(i))[2:].zfill(6) 
    for i in range(0,len(d),8):r+=chr(int(d[i:i+8],2)) 
    return r
for t in range(int(input())):print(f'#{t+1}',s(input()))
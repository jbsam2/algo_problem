c=[0]*26
for i in input():c[ord(i)-65]+=1
o=0;a='';r=''
for i in range(26):
    if c[i]%2:o+=1;a=chr(i+65)
    r+=chr(i+65)*(c[i]//2)
if o>1:print("I'm Sorry Hansoo")
else:print(r+a+r[::-1])
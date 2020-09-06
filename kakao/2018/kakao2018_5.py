def solution(str1, str2):
    a=b=0;c=[0]*676;d=[0]*676
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            c[((ord(str1[i])&31)-1)*26+(ord(str1[i+1])&31)-1]+=1
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            d[((ord(str2[i])&31)-1)*26+(ord(str2[i+1])&31)-1]+=1
    for i in range(676):a+=min(c[i],d[i]);b+=max(c[i],d[i])
    return a*65536//b if b else 65536
def solution(s):
    cnt=z=0
    while s!='1':
        tmp=''
        for i in s:
            if i=='1':tmp+=i
            else:z+=1
        s=bin(len(tmp))[2:]
        cnt+=1
    return [cnt,z]
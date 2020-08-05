s= [1,1,3,2,4,2] # 모집합은 알아서 변환
ret = []

for i in range(1<<len(s)):
    tmp = []
    for j in range(len(s)):
        if 1<<j & i:tmp.append(s[j])
    if sum(tmp)==0:ret.append(tmp)
print(sorted(ret,key=lambda x: len(x)))
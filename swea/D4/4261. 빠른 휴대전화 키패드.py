def s(l,a,c=0):
    for i in l:
        if len(i)!=len(a):continue
        for j in range(len(a)):
            if a[j]!=str((ord(i[j])-1)//3-30-(1 if i[j] in 'svyz' else 0)):break
        else:c+=1
    return c
for t in range(int(input())):a=input().split()[0];print(f'#{t+1}',s(input().split(),a))
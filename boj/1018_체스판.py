n,m=map(int,input().split());b=[input()for _ in range(n)];a=64;s=('WB'*4+'BW'*4)*4
for i in range(n-7):
	for j in range(m-7):x=''.join(b[i+k][j:j+8]for k in range(8));t=sum(x[p]==s[p]for p in range(64));a=min(t,64-t,a)
print(a)
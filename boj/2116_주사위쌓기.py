f=[5,3,4,1,2,0];d=[];r=[]
n=int(input())
for i in range(n):d+=[[*map(int,input().split())]]
for i in range(6):
	t=[];t+=[d[0][i]];s=0
	for j in range(n):k=d[j].index(t[-1]);t+=[d[j][f[k]]]
	for j in range(n):
		if t[j]!=6 and t[j+1]!=6:s+=6
		elif t[j]!=5 and t[j+1]!=5:s+=5
		else:s+=4
	r+=[s]
print(max(r))
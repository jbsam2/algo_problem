n=int(input())
s=input()
l=len(s)
pi=[0]*l
matched,cur=0,1
while cur<l:
	if s[matched]==s[cur]:
		pi[cur]=matched+1
		matched,cur=matched+1,cur+1
	else:
		if matched:
			matched=pi[matched-1]
		else:
			cur+=1
print(n-pi[n-1])

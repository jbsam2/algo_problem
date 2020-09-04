def solution(msg):
	answer=[];d={}
	for i in range(26):d[chr(ord('A')+i)]=i+1
	i=0
	while i<len(msg):
		j=i
		while msg[i:j+1] in d and j<len(msg):j+=1
		if j==len(msg): break
		answer.append(d[msg[i:j]]);d[msg[i:j+1]]=len(d)+1;i=j
	answer.append(d[msg[i:j]])
	return answer
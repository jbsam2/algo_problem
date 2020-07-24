def solution(s):
	answer=len(s)
	for i in range(1,len(s)+1):
		output=''
		zip_str=s[0:i]
		zip_cnt=1
		for j in range(i,len(s)+1,i):
			if zip_str==s[j:j+i]:
				zip_cnt+=1
			else:
				output+="{}".format(zip_cnt if zip_cnt>1 else '')+zip_str
				zip_str=s[j:j+i]
				zip_cnt=1
		output+=zip_str
		if answer>len(output):
			answer=len(output)
	return answer
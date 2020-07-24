def split_string(string):
	ret=[]
	for i in range(len(string)-1):
		if string[i].isalpha() and string[i+1].isalpha():
			ret.append(string[i:i+2])
	return sorted(ret)

def solution(str1,str2):
	ret=[]
	str1=split_string(str1.lower())
	str2=split_string(str2.lower())
	if len(str1)==0 and len(str2)==0:
		return 65536
	else:
		for i in str1:
			if i in str2:
				str2.remove(i)
				ret.append(i)
		return int(len(ret)/len(str1+str2)*65536)
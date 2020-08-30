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
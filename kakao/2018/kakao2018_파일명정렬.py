import re
def solution(files):return sorted(sorted(files,key=lambda i:int(re.findall('\d+',i)[0])),key=lambda i:re.split('\d+',i.lower())[0])
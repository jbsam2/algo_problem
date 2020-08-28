import re

def solution(expression):
    ex_split = re.split(r'(\D)',expression)
    return ex_split    
    
x="100-200*300-500+20"
print(solution(x))
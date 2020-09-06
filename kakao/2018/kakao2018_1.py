def solution(n, arr1, arr2):
    answer=[]
    for i in map(lambda x:x[2:].zfill(n),map(bin,map(lambda x,y:x|y,arr1,arr2))):answer+=[i.replace('0',' ').replace('1','#')]
    return answer
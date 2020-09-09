def solution(x):
    answer = True;tmp=0
    for i in str(x):tmp+=int(i)
    if x%tmp:answer=False
    return answer
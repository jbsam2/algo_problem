def solution(n):
    t=''
    while n:t+=str(n%3);n//=3
    return int(t,3)
dx=[0,0,1,-1];dy=[-1,1,0,0];d={'U':0,'D':1,'R':2,'L':3}
def solution(dirs):
    answer = 0;v=[];p=(0,0)
    for i in dirs:
        D=d[i];np=(p[0]+dy[D],p[1]+dx[D])
        if abs(np[0])>5 or abs(np[1])>5:continue
        if (p,np) not in v:v.append((p,np));v.append((np,p));answer+=1
        p=np
    return answer
def c(m):return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
def c_time(t):return int(t[:2])*60+int(t[3:])
def solution(m,musicinfos):
    m=c(m);answer=[]
    for i,musicinfo in enumerate(musicinfos):
        tmp=musicinfo.split(',')
        p=c_time(tmp[1])-c_time(tmp[0])
        tmp[3]=c(tmp[3])
        pp=tmp[3]*(p//len(tmp[3]))+tmp[3][:(p%len(tmp[3]))]
        if m in pp:answer.append((tmp[2],p,i))
    answer=sorted(answer,key=lambda x:(-x[1],x[2]))
    return answer[0][0] if answer else '(None)'
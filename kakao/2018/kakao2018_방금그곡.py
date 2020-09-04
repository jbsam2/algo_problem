def change(m):
    return m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
def c_time(t):
    return int(t[:2])*60+int(t[3:])

def solution(m,musicinfos):
    m=change(m);answer=[]
    for i,musicinfo in enumerate(musicinfos):
        tmpinfo=musicinfo.split(',')
        start_time=c_time(tmpinfo[0])
        end_time=c_time(tmpinfo[1])
        play_time=end_time-start_time
        tmpinfo[3]=change(tmpinfo[3])
        song_leng=len(tmpinfo[3])
        playpart=tmpinfo[3]*(play_time//song_leng)+tmpinfo[3][:(play_time%song_leng)]
        if m in playpart:
            answer.append((tmpinfo[2],play_time,i))
    answer=sorted(answer,key=lambda x:(-x[1],x[2]))
    return answer[0][0] if answer else '(None)'
def t2s(time):
    h, m, s = [int(x) for x in time.split(':')]
    return (h * 60 + m) * 60 + s

def solution(play_time, adv_time, logs):
    pt, at = t2s(play_time), t2s(adv_time)
    d = [0]*360001

    for log in logs:
        st, en = map(t2s, log.split('-'))
        d[st] += 1
        d[en] -= 1

    for i in range(1, 360001):
        d[i] += d[i-1]

    mval, mtime = sum(d[:at]),0
    curval = mval
    for i in range(1, 360001-at):
        curval = curval - d[i-1] +d[i+at-1]
        if curval > mval:
            mval = curval
            mtime = i
    return f'{mtime//3600:02d}:{mtime%3600//60:02d}:{mtime%60:02d}'  
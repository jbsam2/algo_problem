def solution(play_time, adv_time, logs):
    c = lambda t: int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])
    play_time, adv_time = c(play_time), c(adv_time)
    logs = sorted([s for t in logs for s in [(c(t[:8]), 1), (c(t[9:]), 0)]])

    v, p, b = 0, 0, [0] * play_time
    for t, m in logs:
        if v > 0:
            b[p:t] = [v] * (t - p)
        v, p = v + (1 if m else -1), t

    s = sum(b[:adv_time])

    mv, mi = s, 0
    for i, j in zip(range(play_time - adv_time), range(adv_time, play_time)):
        s += b[j] - b[i]
        if s > mv:
            mv, mi = s, i + 1

    return f"{mi//3600:02d}:{mi%3600//60:02d}:{mi%60:02d}"
def solution(genres, plays):
    answer = []
    d={e:[] for e in set(genres)}
    for e in zip(genres,plays,range(len(plays))):
        d[e[0]].append([e[1],e[2]])
    genreSort=sorted(list(d.keys()),key=lambda x:sum(map(lambda y:y[0],d[x])),reverse=True)
    for g in genreSort:
        t=[e[1] for e in sorted(d[g],key=lambda x:(-x[0],x[1]))]
        answer+=t[:min(len(t),2)]
    return answer
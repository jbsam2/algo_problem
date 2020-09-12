from math import ceil as c
def solution(n, stations, w):
    d=[];a=0
    for i in range(1,len(stations)):d.append(stations[i]-w-1-stations[i-1]-w)
    d.append(stations[0]-w-1);d.append(n-stations[-1]-w)
    for i in d:
        if i<=0:continue
        a+=c(i/(2*w+1))
    return a
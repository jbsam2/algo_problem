def solution(n):
    fac=[1]+[*range(1,2*n+1)]
    for i in range(1,2*n+1):fac[i]*=fac[i-1]
    return fac[2*n]//(fac[n+1]*fac[n])
def solution(k):
    ret = [0,0,1,1,2,5,6,12]+[0]*105
    for i in range(8,112):ret[i]=ret[i-2]+ret[i-3]+ret[i-4]+3*ret[i-5]+3*ret[i-6]+ret[i-7]
    ret[6]=7
    return ret[k]
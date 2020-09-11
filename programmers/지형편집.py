def solution(land, P, Q):
    flatten=sorted([*sum(land,[])])
    n=len(land)
    layer=flatten[n*n*Q//(Q+P)]
    return sum([(layer-v)*P if v<layer else(v-layer)*Q for v in flatten])
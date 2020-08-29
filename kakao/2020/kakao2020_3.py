def solution(key, lock):
    n = len(lock);m = len(key);keys = [list(zip(*reversed(key)))];hom = sum(lock,[]).count(0)
    for _ in range(3):keys.append(list(zip(*reversed(keys[-1]))))    
    for d in range(4):
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                c_hom = 0;flag = 0
                for k in range(m):
                    for l in range(m):
                        if  0 <= (k + i) < n and 0 <= (l + j) < n:
                            if keys[d][k][l] + lock[k+i][l+j] != 1: flag = 1;break
                            else:
                                if lock[k+i][l+j]==0: c_hom += 1
                    if flag:break
                if flag==0 and c_hom == hom:return True
    return False
import sys
from statistics import*
n,*l=map(int,sys.stdin)
print('%.0f'%mean(l),median(l),sorted(multimode(l))[:2][-1],max(l)-min(l))
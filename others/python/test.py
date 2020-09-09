import heapq
l=[7,2,5,3,4,6]
heap=[]
for i in l:
    heapq.heappush(heap,i)
print(heap)
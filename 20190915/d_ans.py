import heapq
import time 
N,M = map(int, input().split())
A = list(-int(i) for i in input().split()) 
start = time.time()
heapq.heapify(A)
end = time.time()
print(end-start) 
for i in range(M):
    x=heapq.heappop(A)//(-2)
    heapq.heappush(A, -x)
 
print(-sum(A))

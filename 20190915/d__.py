
N, M = map(int,input().split())
A = list(-int(i) for i in input().split())
import heapq

heapq.heapify(A)
for _ in range(M):
    a = heapq.heappop(A)//(-2)
    heapq.heappush(A,-a)

print(-sum(A))

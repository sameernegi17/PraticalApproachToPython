"""
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]

"""

import heapq

x = [2,4,3,5,2,1,0,4,6,3]

heapq.heapify(x)
print(x)


heapq.heappush(x,-3)

print(x)

print(heapq.heappop(x)) # -3
print(x)
print(heapq.heappop(x)) # 0
print(x)
print(heapq.heappop(x)) # 1
print(x)
print(heapq.heappop(x)) # 2
print(x)


y = [2,4,3,5,2,1,0,4,6,3]

print(heapq.nlargest(3,y))

y = [2,4,3,5,2,1,0,4,6,3]

print(heapq.nsmallest(5,y))
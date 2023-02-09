import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,p):
        heapq.heappush(self._queue,(-p,self._index,item))
        self._index +=1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


pq = PriorityQueue()


pq.push("banana",1)
pq.push("apple",2)  

print(pq.pop())
    
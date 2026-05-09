import heapq

class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        

    def findMedian(self) -> float:
        medheap = self.heap[:]

        if len(medheap) % 2 == 0:
            for i in range(int(len(medheap) / 2) - 1):
                heapq.heappop(medheap)
            
            outcome = (heapq.heappop(medheap) + heapq.heappop(medheap))/2

        else:
            for i in range(len(medheap) // 2):
                heapq.heappop(medheap)
            
            outcome = heapq.heappop(medheap)
        
        return outcome

        
        
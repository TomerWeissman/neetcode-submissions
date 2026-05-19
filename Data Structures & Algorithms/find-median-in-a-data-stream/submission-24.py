import heapq

class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        

    def findMedian(self) -> float:
        
        
        length = len(self.heap)

        if length == 1:
            return self.heap[0]
        if length == 0:
            return None
        
        
        retain = []

        for _ in range(length//2 - 1):
            retain.append(heapq.heappop(self.heap))
        
        a = heapq.heappop(self.heap)
        retain.append(a)

        if length % 2 == 1:
            ans = heapq.heappop(self.heap)
            retain.append(ans)
        else:
            b = heapq.heappop(self.heap)
            retain.append(b)
            ans = (a+b)/2
        
        for num in retain:
            heapq.heappush(self.heap, num)
        
        return ans
        

        
        
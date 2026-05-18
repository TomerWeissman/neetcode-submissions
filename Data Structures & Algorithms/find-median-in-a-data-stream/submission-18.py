import heapq

class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:

        remainder = []
        length = len(self.heap)

        if length == 1:
            return self.heap[0]
        if length == 0:
            return None

        for _ in range(length//2 - 1):
            remainder.append(heapq.heappop(self.heap))
        
        a = heapq.heappop(self.heap)
        remainder.append(a)

        if length % 2 == 1:
            ans = heapq.heappop(self.heap)
            remainder.append(ans)
        else:
            b = heapq.heappop(self.heap)
            ans = (a + b)/2
            remainder.append(b)
        
        while remainder:
            heapq.heappush(self.heap, remainder.pop())
        
        return ans

        
        
        
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= self.maxHeap[0]:
            heapq.heappush_max(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, num)
    
    
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, val)      

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        return (self.maxHeap[0] + self.minHeap[0]) / 2
        
        
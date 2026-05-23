import heapq

class MedianFinder:

    def __init__(self):
        #create two heaps (min + max)
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            heapq.heappush(self.minHeap, num)
        
        #if larger than the maxheap, push into min.
        #otherwise, push into max
        elif num > self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)

        #if a heap is larger, reorder to equalize.
        while len(self.minHeap) > len(self.maxHeap) + 1:
            move = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, move)
        
        while len(self.maxHeap) > len(self.minHeap) + 1:
            move = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, move)
        
    def findMedian(self) -> float:
        #if sum of lengths is even, pull both
        print(self.minHeap)
        print(self.maxHeap)
        
        max_len = len(self.maxHeap)
        min_len = len(self.minHeap)

        if (max_len + min_len) % 2 == 0:
            print(self.maxHeap[0])
            print(self.minHeap[0])
            return (self.maxHeap[0] + self.minHeap[0])/2
        
        #else: pull larger
        elif max_len > min_len:
            return self.maxHeap[0]
        else:
            return self.minHeap[0]

        
        
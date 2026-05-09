import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        heap = []

        for key, value in freq.items():
            heapq.heappush_max(heap, (value, key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        
        return res



        
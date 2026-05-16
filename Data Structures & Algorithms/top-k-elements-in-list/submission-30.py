import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        heap = []
        for key, val in freq.items():
            heapq.heappush_max(heap, (val, key))
        
        res = []
        for _ in range(k):
            val, key = heapq.heappop_max(heap)
            res.append(key)
        
        return res

        
        
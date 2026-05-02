class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freq = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        i = len(freq) - 1
        while len(res) < k:
            res += freq[i]
            i -= 1

        
        return res






        

            
        

        
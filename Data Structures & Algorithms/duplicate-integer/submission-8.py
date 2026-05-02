class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = defaultdict(int)

        for num in nums:
            res[num] += 1
            if res[num] > 1:
                return True
        
        return False
        
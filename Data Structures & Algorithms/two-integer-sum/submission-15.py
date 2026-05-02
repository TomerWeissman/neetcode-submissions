class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in res:
                return [res[target - num], i]
            
            res[num] = i
        
        return False
    
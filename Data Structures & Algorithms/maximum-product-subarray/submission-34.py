class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float('-inf')

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            
            tmp = curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(n*tmp, n*curMin, n)
            res = max(res, curMax, curMin)
        
        return res
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        res = float('-inf')

        for n in nums:
            maxSum = max(maxSum+n, n)
            res = max(maxSum, res)
        
        return res






    
'''
store maxSum

1. loop through

2. maxSum = max(maxSum+curr, curr)

3. return maxSum

'''
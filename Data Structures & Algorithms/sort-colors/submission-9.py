class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dp = [0]*3

        for num in nums:

            dp[num] += 1
        

        i = 0

        while i < dp[0]:
            nums[i] = 0
            i += 1
        
        while i < (dp[0] + dp[1]):
            nums[i] = 1
            i += 1
        
        while i < (dp[0]+dp[1]+dp[2]):
            nums[i] = 2
            i += 1
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [float('-inf')]*len(nums)

        dp[-1] = 0


        for i in range(len(nums)-1, -1, -1):
            maxLen = 1
            for j in range(len(nums)-1,i,-1):
                if nums[i] < nums[j]:
                    maxLen = max(maxLen, dp[j] + 1)
                
            dp[i] = maxLen
        
        return max(dp)        

                


            



        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1]*len(nums)
        curr = 1

        for i in range(1, len(nums)):
            curr *= nums[i - 1]
            left[i] = curr
        
        curr = 1
        for i in range(len(nums) - 2, -1, -1):
            curr *= nums[i+1]
            left[i] *= curr
        
        return left

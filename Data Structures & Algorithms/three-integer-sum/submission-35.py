class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []

        while i < len(nums):
            
            target = -nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:

                if nums[l] + nums[r] == target:
                    res.append([nums[l], nums[r], -target])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    r -= 1

                elif nums[l] + nums[r] < target:
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    l += 1
                
                elif nums[l] + nums[r] > target:
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    r -= 1
            
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            i += 1
    
        return res

                
                
            
            

        
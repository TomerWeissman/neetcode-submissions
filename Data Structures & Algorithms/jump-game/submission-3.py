class Solution:
    def canJump(self, nums: List[int]) -> bool:

        land = 0

        for i, n in enumerate(nums):
            if i > land:
                return False
            
            land = max(land, i + n)
            
        
        return True






'''
1. initialize variable endpoint

2. loop through (i) 

    2a. if i + nums[i] > endpoint, endpoint == i + nums[i]

    2b. if endpoint > len(nums) -> True

3. return False

'''
        
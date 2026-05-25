class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = len(nums) - 1

        while p > 0 and nums[p] == 2:
            p -= 1
        
        for i in range(p-1,-1,-1):
            if nums[i] == 2:
                nums[i], nums[p] = nums[p], nums[i]
            
            while p > i and nums[p] == 2:
                p -= 1
        
        p = 0

        while p < len(nums)-1 and nums[p] == 0:
            p += 1
        
        for i in range(p+1,len(nums)):
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
            
            while p < i and nums[p] == 0:
                p += 1
        
        
            




'''
1. start from right, find twos, move them to the right


    1a. have a pointer on the right (find edge of twos)
    1b. have  pointer moving backwards
        1ba. if find a two, then switch, and push the pointer to edge of twos again

2. start from left, fnd ones, move them to the right



'''
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = r
        
        def binary(left, right):

            while left <= right:
                mid = (left + right)//2
                
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        ans_left = binary(0, pivot - 1)

        if ans_left > -1:
            return ans_left
        else:
            return binary(pivot, len(nums) - 1)

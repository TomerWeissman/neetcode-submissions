class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r)//2
            
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m
        
        print(r)
        pivot = r

        def binary(left, right):

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        ans = binary(0, pivot - 1)
        
        if ans >= 0:
            return ans
        
        ans = binary(pivot, len(nums) - 1)

        if ans >= 0:
            return ans
        
        return -1

        








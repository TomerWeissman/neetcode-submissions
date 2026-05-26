class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0, len(nums)-1

        def binSearch(nums, target, leftBias):

            l, r = 0, len(nums) - 1
            i = -1

            while l <= r:
                m = (l+r)//2

                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    i = m
                    if leftBias:
                        r = m - 1
                    else:
                        l = m + 1
            return i 
            
        start = binSearch(nums, target, True)
        end = binSearch(nums, target, False)
        
        return [start, end]

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
        
        l1 = 0
        r1 = r - 1
        l2 = r
        r2 = len(nums) - 1


        def binary_search(l, r, target):

            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1

        res1 = binary_search(l1, r1, target)
        res2 = binary_search(l2, r2, target)


        if res1 >= 0:
            return res1
        elif res2 >= 0:
            return res2
        else:
            return -1


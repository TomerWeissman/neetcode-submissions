class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2
            res = min(res, nums[m])
            print(f'mid: {nums[m]}; res {res}')

            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        
        return res
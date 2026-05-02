class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        a = 0

        while a < len(nums) - 2:
            target = 0 - nums[a]
            l = a + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[a], nums[l], nums[r]])
                    curr = nums[r]
                    while nums[r] == curr and l < r:
                        r -= 1
                    
                    curr = nums[l]
                    while nums[l] == curr and l < r:
                        l += 1
                elif nums[l] + nums[r] > target:
                    curr = nums[r]
                    while nums[r] == curr and l < r:
                        r -= 1
                else:
                    curr = nums[l]
                    while nums[l] == curr and l < r:
                        l += 1
            curr = nums[a]
            while nums[a] == curr and a < len(nums) - 2:
                a += 1
        
        return res






class Solution:
    def rob(self, nums: List[int]) -> int:

        gain = {}

        def backtrack(i):

            if i in gain:
                return gain[i]

            if i >= len(nums):
                return 0

            gain[i] = max(nums[i]+backtrack(i+2), backtrack(i+1))

            return gain[i]
        
        return backtrack(0)

        
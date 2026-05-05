class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):

            if sum(curr) > target:
                return
            
            elif sum(curr) == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i)

            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return res
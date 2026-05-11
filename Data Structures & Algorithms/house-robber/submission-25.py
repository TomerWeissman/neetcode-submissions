class Solution:
    def rob(self, nums: List[int]) -> int:

        hashmap = defaultdict(int)
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in hashmap:
                return hashmap[i]

            hashmap[i] = max(nums[i] + dfs(i+2), dfs(i+1))

            return hashmap[i]
        
        return dfs(0)

            


        
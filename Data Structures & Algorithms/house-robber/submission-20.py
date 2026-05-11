class Solution:
    def rob(self, nums: List[int]) -> int:

        hashmap = defaultdict(int)
        def dfs(i, gain):
            if i >= len(nums):
                hashmap[i] = gain
                return hashmap[i]
            
            if i in hashmap:
                return hashmap[i]

            gain = max(nums[i] + dfs(i+2, gain), dfs(i+1, gain))
            hashmap[i] = gain

            return hashmap[i]
        
        return dfs(0, 0)

            


        
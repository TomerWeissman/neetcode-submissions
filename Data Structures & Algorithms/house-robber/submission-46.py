class Solution:
    def rob(self, nums: List[int]) -> int:

        def backtrack(i, hashmap):
            if i > len(nums) - 1:
                return 0
            
            if i in hashmap:
                return hashmap[i]
            
            hashmap[i] = max(nums[i] + backtrack(i+2, hashmap), backtrack(i+1, hashmap))

            return hashmap[i]
        
        return backtrack(0, {})
        
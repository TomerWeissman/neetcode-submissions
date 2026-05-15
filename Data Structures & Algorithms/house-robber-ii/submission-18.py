class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def backtrack(i, end, curr, hashmap):

            if i in hashmap:
                return hashmap[i]
            
            if i > end:
                return curr
            
            curr += max(
                        nums[i] + backtrack(i+2, end, curr, hashmap),
                        backtrack(i+1, end, curr, hashmap)
                        )
            
            hashmap[i] = curr
            return hashmap[i]
        
        return max(
                    backtrack(1, len(nums) - 1, 0, {}), 
                    backtrack(0, len(nums) - 2, 0, {})
                    )
            
            
class Solution:
    def climbStairs(self, n: int) -> int:
        
        hashmap = {}

        def backtrack(i):

            if i > n:
                return 0
            
            if i == n:
                return 1
            
            if i in hashmap:
                return hashmap[i]
            
            hashmap[i] = backtrack(i+1) + backtrack(i+2)

            return hashmap[i]
        
        return backtrack(0)

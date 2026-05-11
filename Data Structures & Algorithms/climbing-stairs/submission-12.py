class Solution:
    def climbStairs(self, n: int) -> int:

        hashmap = defaultdict(int)
        
        def dfs(i):

            if i in hashmap:
                return hashmap[i]

            if i > n:
                hashmap[i] = 0
                return hashmap[i]
            
            if i == n:
                hashmap[i] = 1
                return hashmap[i]
            
            hashmap[i] = dfs(i+1) + dfs(i+2)

            return hashmap[i]
        
        return dfs(0)
            
        
        
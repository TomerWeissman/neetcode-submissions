class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i, count, hashmap):
            if i in hashmap:
                return hashmap[i]
            
            if i > n:
                return 0
            
            if i == n:
                return 1
            

            count += dfs(i+1, count, hashmap) + dfs(i+2, count, hashmap)
            hashmap[i] = count

            return hashmap[i]

        return dfs(0, 0, defaultdict(int))



        
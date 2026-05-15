class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        hashmap = {}

        def dfs(i, curr):
            if i in hashmap:
                return hashmap[i]

            if i >= len(cost):
                return curr

            curr += cost[i] + min(dfs(i+1, curr), dfs(i+2, curr))
            hashmap[i] = curr
            return hashmap[i]
        
        return min(dfs(0, 0), dfs(1,0))
        
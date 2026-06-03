class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        dp = [float('inf')]*(amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):

            for c in coins:

                if i - c >= 0:

                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1





'''
1. create a dp

2. cycle backwards through the thing

3. if the distance from the end is equal  or more to one of the coins, then set the current to the minimum of that plus one and what exists

4. take what is now at beginning




'''
        
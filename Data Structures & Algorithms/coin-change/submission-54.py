class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1                






'''
1. Create a dp -> holds all possible numbers len(amount+1)

2. set everything to false, except the last.

3. Loop backwards

    3a. for coin, when coin + i < lenghth

        3a.1 min option of 1 + couns[i+coin] and not equal None
    
    return dp[0]
'''



        
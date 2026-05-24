class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ROWS = len(text1) + 1
        COLS = len(text2) + 1

        dp = [[0 for i in range(COLS)] for j in range(ROWS)]

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

        
        



'''
1. init rows and columns

2. Make a dp grid

3. Ill loop through and say, if the letter is equal, then its diagonal + 1, 
otherwise, its max of above and next.

4. Fill out all the way to the end.

5. Return bottom right.
'''


        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        dp = [False]*(len(s)+1)
        dp[-1] = True


        #loop backwards
        for i in range(len(s)-1, -1, -1):

            #loop through words
            for word in wordDict:

                print(s[i:i+len(word)])
                if len(s) > (i + len(word)-1) and s[i:i+len(word)] == word:
                    
                    if dp[i + len(word)]:
                        dp[i] = dp[i + len(word)]
                    

        print(dp)
        return dp[0]
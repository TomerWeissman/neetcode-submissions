class Solution:
    def countSubstrings(self, s: str) -> int:

        total_count = 0
        for i in range(len(s)):
            count = 1

            l = i - 1
            r = i + 1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            l = i
            r = i + 1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            total_count += count
        
        return total_count


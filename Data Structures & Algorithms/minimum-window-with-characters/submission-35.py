class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        freq_t = defaultdict(int)
        freq_s = defaultdict(int)
        res = ''

        for c in t:
            freq_t[c] += 1
        
        need = len(freq_t)
        have = 0
        l = 0
        length = float('inf')

        for r in range(len(s)):

            if s[r] not in freq_t:
                continue
            
            freq_s[s[r]] += 1

            if freq_s[s[r]] == freq_t[s[r]]:
                have += 1
            
            if have == need:
                while have == need:
                    if s[l] not in freq_t:
                        l += 1
                        continue
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] < freq_t[s[l]]:
                        have -= 1
                    l += 1
                
                ans = s[l-1:r+1]

                if len(ans) < length:
                    length = len(ans)
                    res = ans
        
        return res
                    
            






        
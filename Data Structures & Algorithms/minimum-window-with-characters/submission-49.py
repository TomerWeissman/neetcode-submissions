class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT, window = defaultdict(int), defaultdict(int)

        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float('inf')
        l = 0

        for r in range(len(s)):
            if s[r] not in countT:
                continue
            
            window[s[r]] += 1

            if window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                length = r - l + 1

                if length < resLen:
                    resLen = length
                    res = [l, r]
                
                if s[l] in countT:
                    window[s[l]] -= 1

                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1

        l, r = res
        return s[l:r+1] if l >= 0 else ''






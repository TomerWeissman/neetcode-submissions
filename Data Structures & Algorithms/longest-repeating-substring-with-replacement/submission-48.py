class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hashmap = defaultdict(int)
        res = 0
        
        max_freq = 0
        l = 0

        for r in range(len(s)):
            hashmap[s[r]] += 1
            max_freq = max(max_freq, hashmap[s[r]])

            while r - l + 1 - max_freq > k:
                
                hashmap[s[l]] -= 1
                l += 1
        
            res = max(res, r - l + 1)
    
        return res



            


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        r = -1
        length = 0
        max_freq = 0

        while r < len(s) - 1:
            r += 1
            print(f'{l} -> {r}')
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            while r - l + 1 - max_freq > k and l < r:
                freq[s[l]] -= 1
                l += 1
            
            print(f'Valid: {l} -> {r}')
            length = max(length, r - l + 1)

        return length


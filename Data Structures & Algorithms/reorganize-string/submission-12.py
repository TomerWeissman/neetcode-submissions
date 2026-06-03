import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = defaultdict(int)

        for c in s:
            freq[c] += 1
        
        heap = []
        for char, frequency in freq.items():
            heapq.heappush_max(heap, [frequency, char])

        res = ''
        while heap:

            nxt = heapq.heappop_max(heap)

            if not heap:
                if nxt[0] == 1:
                    res += nxt[1]
                    return res
                else:
                    return ""
            else:
                nxt_nxt = heapq.heappop_max(heap)

                res += nxt[1]
                res += nxt_nxt[1]

                nxt[0] -= 1
                nxt_nxt[0] -= 1

                if nxt[0] > 0:
                    heapq.heappush_max(heap, nxt)
                
                if nxt_nxt[0] > 0:
                    heapq.heappush_max(heap, nxt_nxt)
        
        return res
            

                    




'''
1. make a dict of all the characters

2. find the one that has the most

3. start with that and move forward

4. if I start and I dont have enoug

'''

        
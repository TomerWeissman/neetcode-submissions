import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time_to_eat(m):
            count = 0

            for pile in piles:
                count += math.ceil(pile/m)

            return count
        
        n = max(piles)
        l = 1
        r = n
        res = n
        
        while l <= r:
            m = (l+r)//2

            if time_to_eat(m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

            



        
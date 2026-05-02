class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        gain = 0

        for price in prices:
            min_price = min(min_price, price)
            gain = max(gain, price - min_price)
        
        return gain
            



        
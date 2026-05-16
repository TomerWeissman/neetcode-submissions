class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        gain = float('-inf')

        for price in prices:
            min_price = min(price, min_price)
            gain = max(price - min_price, gain)
        
        return gain

        
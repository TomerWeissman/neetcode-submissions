class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gain = float('-inf')
        minprice = float('inf')

        for price in prices:
            minprice = min(price, minprice)
            gain  = max(gain, price - minprice)
        
        return gain

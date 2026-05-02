class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights) - 1):
            for x in range(i+1, len(heights)):
                h = min(heights[i], heights[x])
                water_capacity = h*(x - i)
                max_water = max(water_capacity, max_water)
        
        return max_water
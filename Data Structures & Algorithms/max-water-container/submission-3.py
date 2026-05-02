class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0

        while l < r:
            h = min(heights[l], heights[r])
            #fill ==> Amount of water
            fill = h*(r - l)
            max_water = max(fill, max_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return max_water

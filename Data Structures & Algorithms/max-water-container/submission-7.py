class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_water = 0

        while l < r:
            h = min(heights[l], heights[r])
            max_water = max((r - l)*h, max_water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_water

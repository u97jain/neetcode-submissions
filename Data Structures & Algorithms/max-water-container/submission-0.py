class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l = 0
        r = len(heights) - 1

        maxL, maxR = 0, 0
        while l < r:
            curHeight = min(heights[l], heights[r])
            curWater = curHeight * (r - l)
            maxWater = max(maxWater, curWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater

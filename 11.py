class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        currWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            currWater = width * h
            if currWater > maxWater:
                maxWater = currWater
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater

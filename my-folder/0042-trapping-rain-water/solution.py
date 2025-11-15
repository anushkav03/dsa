class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxLeft[0] = 0
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

        maxRight = [0] * len(height)
        maxRight[-1] = 0
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        water = [0] * len(height)
        for i in range(0, len(height)):
            min_i = min(maxLeft[i], maxRight[i])
            if min_i - height[i] > 0:
                water[i] = min_i - height[i]
            else:
                water[i] = 0

        return sum(water)
        

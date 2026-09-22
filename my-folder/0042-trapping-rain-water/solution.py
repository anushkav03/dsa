class Solution:
    def trap(self, height: list[int]) -> int:
        lefts = [0] * len(height)
        max_left = 0
        for i in range(0, len(height)):
            lefts[i] = max_left
            max_left = max(max_left, height[i])

        rights = [0] * len(height)
        max_right = 0
        for i in range(len(height)-1, -1, -1):
            rights[i] = max_right
            max_right = max(max_right, height[i])
        
        water = [0] * len(height)
        for i in range(0, len(height)):
            water[i] = max(min(lefts[i], rights[i]) - height[i], 0)

        return sum(water)
        

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while r > l:
            area = (r - l) * min(height[r], height[l])
            max_area = max(max_area, area)
            # print(r, l, "area: ", area, " max area: ", max_area)
            if height[r] <= height[l]:
                r -= 1
            else:
                l += 1
        return max_area
        

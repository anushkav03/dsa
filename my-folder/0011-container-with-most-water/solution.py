class Solution:
    def maxArea(self, height: List[int]) -> int:
        # logic: left pointer starts at left end, right pointer starts at right
        # of the two, whichever is shorter, move that one forward towards centre 
        # remember goal is to calculate max height => moving shorter height bar is
        # in a sense discarding it 
        left = 0
        right = len(height) - 1
        maxheight = 0
        while right > left:
            curr_height = (right-left) * min(height[left], height[right])
            maxheight = max(maxheight, curr_height)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxheight



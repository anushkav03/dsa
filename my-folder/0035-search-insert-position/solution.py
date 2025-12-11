class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums)
        while lower < upper:
            mid = ((upper - lower) // 2) + lower
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                upper -= 1
            else:
                lower += 1
        return lower

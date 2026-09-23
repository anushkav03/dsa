class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while True:
            mid = ((r - l) // 2) + l
            if nums[l] <= nums[mid] and nums[mid] <= nums[r]:
                return nums[l]
            elif nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        return -199
        

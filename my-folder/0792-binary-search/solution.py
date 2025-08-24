class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) - 1

        def helper(min, max):
            if max - min == 0:
                return max
            mid = min + ((max - min) // 2)
            return mid

        while max >= min:
            mid = helper(min, max)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                max = mid - 1
            else:
                min = mid + 1
        return -1
        

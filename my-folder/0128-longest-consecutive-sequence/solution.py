class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxlength = 1
        nums = set(nums)
        for num in nums:
            if ((num - 1) not in nums) and ((num + 1) in nums):
                curr_elem = num
                temp_length = 1
                while (curr_elem + 1) in nums:
                    curr_elem += 1
                    temp_length += 1
                if temp_length > maxlength:
                    maxlength = temp_length
        return maxlength
        

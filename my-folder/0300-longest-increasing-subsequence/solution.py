class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        memo = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]: 
                    memo[i] = max(memo[j] + 1, memo[i])
        return max(memo)
        

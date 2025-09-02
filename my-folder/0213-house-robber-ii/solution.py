class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 3:
            return max(nums)

        def helper(lst):
            # if len(lst) == 1:
            #     return lst[0]
            # if len(lst) <= 2:
            #     return max(lst)

            memo = list(range(len(lst)))
            memo[0] = lst[0]
            memo[1] = max(lst[0], lst[1])

            for i in range(2, len(lst)):
                memo[i] = max(lst[i] + max(memo[:i - 1]), memo[i-1])

            return max(memo)

        #return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
        #return helper([nums[-1]] + nums[:len(nums)-2])
        return max(helper(nums[:len(nums)-1]), helper([nums[-1]] + nums[:len(nums)-2]))
        

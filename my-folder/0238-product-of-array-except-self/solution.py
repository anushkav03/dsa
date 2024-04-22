class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize prefix, postfix, output lists
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = [0] * len(nums)

        # populate prefix, postfix
        for i in range(len(nums)):
            if i==0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
            
        for i in range(len(nums)):
            index = len(nums) - i - 1
            if index==len(nums) - 1:
                postfix[index] = nums[index]
            else:
                postfix[index] = postfix[index + 1] * nums[index]

        # calculate output
        for i in range(len(nums)):
            if i==0:
                output[i] = postfix[i + 1]
            elif i==len(nums)-1:
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i-1] * postfix[i+1]

        return output
        

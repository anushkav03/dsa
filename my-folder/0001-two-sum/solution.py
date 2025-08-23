class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## OPTIMIZATION 1 ##
        numindex = {}
        for i in range(len(nums)):
            # check if target in index
            subtarget = target - nums[i]
            if subtarget in numindex and numindex[subtarget] != i:
                # return answer
                return [numindex[subtarget], i]

            # add num to index
            if nums[i] in numindex:
                pass
            else:
                numindex[nums[i]] = i # num : index
        return []
            

        ## BRUTE FORCE: Time O(n^2) Space O(n) ##
        # #sortednums = nums[:]
        # #sortednums.sort() # make a copy and sort nums
        # for i in range(len(nums)): # pointer 1
        #     subtarget = target - nums[i]

        #     for j in range(len(nums)-1, -1, -1): # pointer 2
        #         if i != j:
        #             if nums[j] < subtarget:
        #                 continue
        #             if nums[j] == subtarget:
        #                 #return [nums.index(sortednums[i]), nums.index(sortednums[j])]
        #                 return [i, j]
        # return []
            

        

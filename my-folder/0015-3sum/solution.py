class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        triples = []
        for i in range(0, len(nums)):
            # avoid duplicates, skip i if same as prev
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            jk_nums = nums[i+1:]
            target = nums[i] * -1
            i_triples = []
            r = len(jk_nums) - 1
            l = 0
            while r > l:
                if jk_nums[r] + jk_nums[l] == target:
                    # preventing duplicates inner loop; see testcase [0,0,0,0]
                    if not ((l >= 1) and (jk_nums[l] == jk_nums[l-1])):
                        triple = [nums[i], jk_nums[r], jk_nums[l]]
                        i_triples.append(triple)
                    l += 1
                elif jk_nums[r] + jk_nums[l] > target:
                    r -= 1
                else:
                    l += 1
            triples.extend(i_triples)
        return triples
        

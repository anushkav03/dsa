class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fin = 0
        for i in nums:
            fin = fin ^ i
        return fin

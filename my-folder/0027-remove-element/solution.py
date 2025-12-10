class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        popped = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                popped.append(nums.pop(i))
        nums.extend(popped)
        return len(nums) - len(popped)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        med_index = size // 2
        i = 0
        both = []
        while i <= med_index:
            if len(nums1) == 0:
                both.append(nums2[0])
                nums2 = nums2[1:]
            elif len(nums2) == 0: 
                both.append(nums1[0])
                nums1 = nums1[1:] 
            elif nums2[0] <= nums1[0]: 
                both.append(nums2[0])
                nums2 = nums2[1:]
            else:
                both.append(nums1[0])
                nums1 = nums1[1:] 
            i += 1
        if size % 2 == 0:
            return (both[-1] + both[-2]) / 2
        else:
            return both[-1]

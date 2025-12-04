class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        # if len(haystack) == 1:
        #     if needle == haystack:
        #         return 0
        #     else:
        #         return -1
        
        for i in range(0, len(haystack)-needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
        

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        if '0' not in s:
            return True
        first = s.index('0')
        if '1' in s[first:]:
            return False
        else:
            return True


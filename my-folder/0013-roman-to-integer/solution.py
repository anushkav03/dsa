class Solution:
    def romanToInt(self, s: str) -> int:
        conv = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        prev = s[-1]
        for i in s[::-1]:
            if i == "I" and prev in "VX":
                num -= conv.get(i)
            elif i == "X" and prev in "LC":
                num -= conv.get(i)
            elif i == "C" and prev in "DM":
                num -= conv.get(i)
            else:
                num += conv.get(i)
            prev = i
        return num

        

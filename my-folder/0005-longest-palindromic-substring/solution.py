class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        def helper(s,start,fin):
            j = 0
            while start-j >= 0 and fin+j < len(s):
                if s[start - j] == s[fin + j]:
                    j += 1
                else:
                    j -= 1
                    return s[(start-j):(fin+j+1)]
            return s[(start-j+1):(fin+j)]

        # pals = []
        longest = ""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                pal = helper(s, i, i+1)
                # pals.append(pal)
                if len(pal) > len(longest):
                    longest = pal
            if i+2<len(s) and s[i] == s[i+2]:
                pal = helper(s, i, i+2)
                # pals.append(pal)
                if len(pal) > len(longest):
                    longest = pal
        if not longest:
            return s[0]
        return longest


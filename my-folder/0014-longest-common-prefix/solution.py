class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        if strs[0] == "":
            return ""
        longest = strs[-1]
        i = 0
        for i in range(0, len(longest)):
            ith = longest[i]
            try:
                if all([(ith == word[i]) for word in strs]):
                    pass
                else:
                    return longest[:i]
            except:
                return longest[:i]
        return longest

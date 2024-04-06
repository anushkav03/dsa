class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True 

        s = s.lower()
        s = re.sub(r'[^0-9a-z]+', '', s)

        # 0 1 2 3
        # 3 2 1 0

        for i in range(0, len(s)-1):
            if len(s)-i-1 < i:
                return True
            if s[i] != s[len(s)-i-1]:
                return False
        return True
        

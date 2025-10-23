class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower() 
        s = "".join([x for x in s if x in "0123456789qwertyuiopasdfghjklzxcvbnm"])

        return s == s[::-1]

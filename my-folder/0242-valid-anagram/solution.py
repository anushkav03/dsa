class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {} 

        for i in range(0, len(s)):
            if s[i] in sdict:
                sdict[s[i]] += 1
            else:
                sdict[s[i]] = 1 

            if t[i] in tdict:
                tdict[t[i]] += 1
            else:
                tdict[t[i]] = 1

        if sdict==tdict:
            return True
        else:
            return False
        """
        if len(s) != len(t):
            return False

        s = "".join(sorted(s))   
        t = "".join(sorted(t))

        #for i in range(0, len(s)):
        #    if s[i] != t[i]:
        #        return False
        
        return s==t


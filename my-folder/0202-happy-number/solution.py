class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        n_str = list(str(n))
        seen.add(n)
        while True:
            new = sum([int(x)**2 for x in n_str])
            if new == 1:
                return True
            if new in seen:
                return False
            seen.add(new)
            n_str = list(str(new))
        return -1
            
        

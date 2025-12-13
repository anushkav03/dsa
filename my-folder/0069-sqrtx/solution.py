class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        for i in range(0, x):
            if i*i == x:
                return i
            elif i*i < x and (i+1)*(i+1) > x:
                return i
        return -1
        

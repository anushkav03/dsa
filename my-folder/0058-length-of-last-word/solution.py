class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # TIL .split() by default just ignores all spaces
        # whereas .split(" ") which is what i did
        # complicates the situation
        # bc you may end up with "word", "word", "", ""
        return len(s.split()[-1])
        

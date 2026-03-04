class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        coords = 0
        for row in mat:
            if sum(row) == 1:
                ind = row.index(1)
                if sum([r[ind] for r in mat]) == 1:
                    coords += 1
        return coords
        

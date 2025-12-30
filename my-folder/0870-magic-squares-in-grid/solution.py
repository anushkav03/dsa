class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checkgrid(grid):
            # distinct
            distinct = set()
            for row in grid:
                if any([num > 9 or num < 1 for num in row]):
                    return False
                distinct.update(row)
            if len(distinct) < 9:
                return False

            # same sum
            magicsum = sum(grid[0])
            for i in range(0, 3):
                if not sum(grid[i]) == magicsum:
                    return False
                col_i = [row[i] for row in grid]
                if not sum(col_i) == magicsum:
                    return False
            diag_1 = grid[0][0] + grid[1][1] + grid[2][2]
            diag_2 = grid[0][2] + grid[1][1] + grid[2][0]
            if diag_1 != magicsum or diag_2 != magicsum:
                return False
            return True

        #lst = []
        valid = 0
        for col in range(0, len(grid[0])-2):
            for row in range(0, len(grid)-2):
                subgrid = [r[col:col+3] for r in grid]
                subgrid = subgrid[row:row+3]
                if checkgrid(subgrid):
                    valid += 1
                #lst.append(subgrid)
        #return lst
        return valid

            
        

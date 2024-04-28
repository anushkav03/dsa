class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # define helper to check if array is valid i.e. distinct and values in [1,9]
        def isvalid(subgrp):
            # remove "."
            subgroup = [x for x in subgrp if x!="."]
            # check distinct and in [1,9]
            inrange = all([x in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] for x in subgroup])
            distinct = (len(set(subgroup)) == len(subgroup)) 
            return inrange and distinct
        
        # check row
        for row in board:
            if not isvalid(row):
                return False
        
        # check column
        for i in range(0, 9):
            col = []
            for row in board:
                col.append(row[i])
            if not isvalid(col):
                return False

        # check 3x3 grid
        for istep in range(0, 9, 3):
            for jstep in range(0, 9, 3):
                grid = []
                for i in range(istep, istep+3):
                    grid += board[i][jstep:jstep+3]
                if not isvalid(grid):
                    return False

        return True
        

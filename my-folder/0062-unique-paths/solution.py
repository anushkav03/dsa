class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = {(0,0):1}

        for row in range(m):
            for col in range(n):
                if col+1 < n:
                    if (row,col+1) not in grid.keys():
                        grid[(row,col+1)] = 0
                    grid[(row,col+1)] = grid[(row,col+1)] + grid[(row,col)]
                        
                if row+1 < m:
                    if (row+1,col) not in grid.keys():
                        grid[(row+1,col)] = 0
                    grid[(row+1,col)] = grid[(row+1,col)] + grid[(row,col)]

        return grid[(m-1,n-1)]

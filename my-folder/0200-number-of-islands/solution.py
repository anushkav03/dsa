class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def gridtonum(row, col, grid):
            return int(grid[row][col])

        def explore(row, col, grid):
            if gridtonum(row, col, grid) <= 0:
                return 0
            grid[row][col] = '-1' #visit node i.e. set it to marked
            
            if row+1 < len(grid):
                explore(row+1, col, grid) #traverse bottom
            if col+1 < len(grid[0]):
                explore(row, col+1, grid) #traverse right
            if col-1 >= 0:
                explore(row, col-1, grid) #traverse left
            if row-1 >= 0:
                explore(row-1, col, grid)
            
            return 1

        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += explore(i, j, grid)

        return sum

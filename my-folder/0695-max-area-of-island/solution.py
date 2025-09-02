class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(row, col, grid, size):
            # visit node
            if grid[row][col] == 1:
                size += 1
                grid[row][col] = -1
            else:
                return size

            # traverse right, left
            if not row >= len(grid) - 1:
                size += explore(row+1, col, grid, 0)
            if row > 0:
                size += explore(row-1, col, grid, 0)

            # traverse down, up
            if not col >= len(grid[0]) - 1:
                size += explore(row, col+1, grid, 0)
            if col > 0:
                size += explore(row, col-1, grid, 0)

            return size

        max_size = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                size = explore(i, j, grid, 0)
                max_size = max(size, max_size)

        return max_size
        # return explore(3, 8, grid, 0)
            

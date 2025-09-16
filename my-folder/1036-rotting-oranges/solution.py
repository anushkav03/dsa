class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        max_mins = 0
        sum = 0
        queue = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j, 0)) # add all rotten oranges to queue (row,col,mins)
                if grid[i][j] == 1:
                    sum += 1
        if sum == 0:
            return 0

        while queue:
            curr = queue.pop(0) #pop
            row, col, mins = curr[0], curr[1], curr[2]
            max_mins = max(max_mins, mins)
            #grid[row][col] = -2 #mark visited 

            # for each unvisited neighbor: enqueue & mark visited
            if row+1 < len(grid) and grid[row+1][col] == 1:
                queue.append((row+1, col, mins+1))
                grid[row+1][col] = -2
                sum -= 1
            if row-1 >= 0 and grid[row-1][col] == 1:
                queue.append((row-1, col, mins+1))
                grid[row-1][col] = -2
                sum -= 1
            if col+1 < len(grid[0]) and grid[row][col+1] == 1:
                queue.append((row, col+1, mins+1))
                grid[row][col+1] = -2
                sum -= 1
            if col-1 >= 0 and grid[row][col-1] == 1:
                queue.append((row, col-1, mins+1))
                grid[row][col-1] = -2
                sum -= 1

        if sum > 0:
            return -1
        else:
            return max_mins
        

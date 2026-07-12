class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def destroyIsland(row, col, grid):
            ROWS = len(grid)
            COLS = len(grid[0])

            # Base case
            # B1: out of grid
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            # B2: grid[row][col] is a 0:
            if grid[row][col] == "0":
                return
            
            # Recursive case
            grid[row][col] = "0"
            destroyIsland(row + 1, col, grid)
            destroyIsland(row - 1, col, grid)
            destroyIsland(row, col + 1, grid)
            destroyIsland(row, col - 1, grid)


        ROWS = len(grid)
        COLS = len(grid[0])

        ans = 0

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if grid[i][j] == "1":

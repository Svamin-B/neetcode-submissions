class Solution:
    """
    Keep a record of what has been visited
    traverse the array
    once a "1" is seen, dfs on all neighbours with stack
    go through each "1" and append to visited
    """
    def dfs(self, r: int, c: int, grid: List[List[str]]) -> int:
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0"):
            return
        
        grid[r][c] = "0"

        self.dfs(r + 1, c, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r, c - 1, grid)
        




    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, grid)

        return count
class Solution:
    def dfs(self, r: int, c: int, grid: List[List[str]]) -> int:
        if(r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0"):
            return

        grid[r][c] = "0"

        self.dfs(r + 1, c, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r, c - 1, grid)



    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(i, j, grid)
                j +=1
            i += 1
        
        return islands

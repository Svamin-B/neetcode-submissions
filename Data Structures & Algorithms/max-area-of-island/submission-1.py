class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        loop through each element
        count = 0
        if its 1 then make zero and add to stack and add count
        while stack not empty:
            pop element
            check neighbours
                if 1 then add to count
                add to stack
                make zero
        highest = max(highest, count)
        
        """
        stack = []
        rows = len(grid)
        cols = len(grid[0])
        highest = 0
        for i in range(rows):
            for j in range(cols):

                count = 0
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    count += 1
                    stack = [(i, j)]

                while stack:
                    r, c = stack.pop()
                    for dr, dc  in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = dr + r, dc + c
                        if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == 0):
                            continue
                        else:
                            count += 1
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
                highest = max(count, highest)

        return highest


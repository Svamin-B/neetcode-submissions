from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        walk through each element
        if its fresh then increment fresh count
        else if its rotten
            append to queue

        minutes = 0
        while queue and fresh
            minutes += 1
            for _ in range(len(queue)):
                pop element
                for dr, dc in all directions
                    check if fresh:
                        make it 2
                        append to queue
                        decrement count

        return -1 or minutes
        """
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        while queue and fresh:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2

        if fresh > 0:
            return -1
        return minutes



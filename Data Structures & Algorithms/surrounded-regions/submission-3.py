from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Walk through each element
        if its on the border and O then label it B and append to queue

        while queue:
            for _ in range(len(queue)):
                pop element
                if its neighbours are valid (within grid)
                    if neighbour is "B" then current element is also B
                    append to queue

        walk through board again and change Bs to Os and change the rest to X
        
        """
        queue = deque()
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if i in (0, rows - 1) or j in (0, cols - 1):
                    if board[i][j] == "O":
                        board[i][j] = "B"
                        queue.append((i, j))

        while queue:
            # for _ in range(len(queue)): # This is for layers
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < rows and 0 <= nc < cols):
                        if board[nr][nc] == "O":
                            board[nr][nc] = "B"
                            queue.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "B":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


        


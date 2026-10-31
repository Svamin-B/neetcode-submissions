class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        go through each element and store value in hashmap
        map = {
            "rows" : [[],[],[], [],[],[], [],[],[]],
            "cols" : [[],[],[], [],[],[], [],[],[]],
            "grids" : [[],[],[], [],[],[], [],[],[]]
        }
        """
        map = {
            "rows" : [[],[],[], [],[],[], [],[],[]],
            "cols" : [[],[],[], [],[],[], [],[],[]],
            "grids" : [[],[],[], [],[],[], [],[],[]]
        }
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    map["rows"][i].append(board[i][j])
                    map["cols"][j].append(board[i][j])

                    if 0 <= i < 3 and 0 <= j < 3:
                        map["grids"][0].append(board[i][j])
                    if 0 <= i < 3 and 3 <= j < 6:
                        map["grids"][1].append(board[i][j])
                    if 0 <= i < 3 and 6 <= j < 9:
                        map["grids"][2].append(board[i][j])

                    if 3 <= i < 6 and 0 <= j < 3:
                        map["grids"][3].append(board[i][j])
                    if 3 <= i < 6 and 3 <= j < 6:
                        map["grids"][4].append(board[i][j])
                    if 3 <= i < 6 and 6 <= j < 9:
                        map["grids"][5].append(board[i][j])

                    if 6 <= i < 9 and 0 <= j < 3:
                        map["grids"][6].append(board[i][j])
                    if 6 <= i < 9 and 3 <= j < 6:
                        map["grids"][7].append(board[i][j])
                    if 6 <= i < 9 and 6 <= j < 9:
                        map["grids"][8].append(board[i][j])

        rows = map["rows"]
        for row in rows:
            if len(set(row)) != len(row):
                return False
        cols = map["cols"]
        for col in cols:
            if len(set(col)) != len(col):
                return False
        grids = map["grids"]
        for grid in grids:
            if len(set(grid)) != len(grid):
                return False
        return True

    
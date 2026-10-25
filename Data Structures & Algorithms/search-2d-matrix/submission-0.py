class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search on rows then on columns
        """
        cols = len(matrix[0]) - 1
        r_l = 0
        r_h = len(matrix) - 1
        row = None

        while (r_l <= r_h):
            mid = (r_l + r_h) // 2

            if target < matrix[mid][0]:
                r_h = mid - 1
            elif target > matrix[mid][cols]:
                r_l = mid + 1
            else:
                row = mid
                break
        if row == None:
            return False

        c_l = 0
        c_h = cols
        col = None
        rows = c_h

        while (c_l <= c_h):
            mid = (c_l + c_h) // 2

            if target < matrix[row][mid]:
                c_h = mid - 1
            elif target > matrix[row][mid]:
                c_l = mid + 1
            else:
                col = mid
                break
        if col == None:
            return False
        return True


        
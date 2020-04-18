class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        row = len(matrix)
        col = len(matrix[0])
        first_col, first_row = False, False

        for i in range(row):
            if matrix[i][0] == 0:
                first_col = True

        for j in range(col):
            if matrix[0][j] == 0:
                first_row = True

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(1, col):
                    matrix[i][j] = 0

        for j in range(1, col):
            if matrix[0][j] == 0:
                for i in range(1, row):
                    matrix[i][j] = 0

        if first_col:
            for i in range(row):
                matrix[i][0] = 0

        if first_row:
            for j in range(col):
                matrix[0][j] = 0
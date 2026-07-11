class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Find zeroes
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowsWithZeros = set()
        colsWithZeros = set()
        for i in range(0, ROWS):
            for j in range(0, COLS):
                if matrix[i][j] == 0:
                    rowsWithZeros.add(i)
                    colsWithZeros.add(j)
        
        # Set the rows to 0
        for row in rowsWithZeros:
            matrix[row] = [0] * COLS

        # Set the cols to 0
        for col in colsWithZeros:
            for i in range(0, ROWS):
                matrix[i][col] = 0

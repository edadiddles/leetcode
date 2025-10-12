from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, 0
        while i < len(matrix):
            while j < len(matrix[0]):
                if i > 0 and matrix[i-1][j] is None:
                    matrix[i-1][j] = 0

                if len(matrix) == i+1 and matrix[i][j] is None:
                    matrix[i][j] = 0
                    j += 1
                    continue
                if matrix[i][j] != 0:
                    j += 1
                    continue

                for k in range(len(matrix)):
                    if matrix[k][j] == 0:
                        continue
                    elif k < i:
                        matrix[k][j] = 0
                        continue

                    matrix[k][j] = None

                for k in range(len(matrix[i])):
                    if matrix[i][k] == 0:
                        continue
                    elif k < j:
                        matrix[i][k] = 0
                        continue

                    matrix[i][k] = None
                j += 1

            j = 0
            i += 1



from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        sum = 0
        for k in range(n):
            sum += mat[k][k]
            if k != n-k-1:
                sum += mat[k][n-k-1]

        return sum

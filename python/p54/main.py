from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pos = [0, 0]
        dir = [1, 0]

        spiral_arr = []
        while True:
            spiral_arr.append(matrix[pos[1]][pos[0]])
            matrix[pos[1]][pos[0]] = -999  # constraint is matrix vals are in the range [-100,100]

            x = pos[0]+dir[0]
            y = pos[1]+dir[1]

            if y >= len(matrix) or x >= len(matrix[0]) or matrix[y][x] == -999:
                dir = [-dir[1], dir[0]]
                x = pos[0]+dir[0]
                y = pos[1]+dir[1]
                if y >= len(matrix) or x >= len(matrix[0]) or matrix[y][x] == -999:
                    return spiral_arr

            pos = [x, y]

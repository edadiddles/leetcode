from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_provinces = 0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    num_provinces += 1
                    self.r_walk(isConnected, i, j)

                isConnected[i][j] = -1  # mark as visited

        return num_provinces

    def r_walk(self, isConnected: List[List[int]], i: int, j: int):
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]

        if i < 0 or j < 0 or i >= len(isConnected) or j >= len(isConnected[i]):
            return
        elif isConnected[i][j] in (-1, 0):
            return

        isConnected[i][j] = -1
        for dir in dirs:
            self.r_walk(isConnected, i+dir[0], j+dir[0])

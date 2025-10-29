from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nodes_visited = [0]*len(isConnected)

        num_provinces = 0
        for i in range(len(isConnected)):
            if nodes_visited[i] == 1:
                continue

            num_provinces += 1
            self.r_walk(isConnected, nodes_visited, i)

        return num_provinces


    def r_walk(self, isConnected: List[List[int]], nodes_visited: List[int], i: int):
        nodes_visited[i] = 1
        for j in range(len(isConnected[i])):
            if nodes_visited[j] == 1:
                continue

            if isConnected[i][j] == 1:
                self.r_walk(isConnected, nodes_visited, j)

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        nodes_visited = [0]*n

        num_provinces = 0
        for i in range(n):
            if nodes_visited[i] == 1:
                continue

            num_provinces += 1
            print(f"starting walk: {i}")
            self.r_walk(isConnected, nodes_visited, i)

        return num_provinces


    def r_walk(self, isConnected: List[List[int]], nodes_visited: List[int], i: int):
        nodes_visited[i] = 1
        for j in range(len(isConnected[i])):
            if nodes_visited[j] == 1:
                continue

            if isConnected[i][j] == 1:
                print(f"recursive walk: {j}")
                self.r_walk(isConnected, nodes_visited, j)

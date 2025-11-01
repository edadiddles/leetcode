from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        keys = [0]

        for room in range(len(rooms)):
            if room in keys:
                self.r_walk(room, rooms, keys, visited)

        for i in range(len(visited)):
            if not visited[i]:
                return False

        return True


    def r_walk(self, node: int, adj: List[List[int]], keys: List[int], visited: List[int]) -> bool:
        if visited[node]:
            return

        visited[node] = True
        keys += adj[node]
        while len(keys) > 0:
            key = keys.pop(0)
            self.r_walk(key, adj, keys, visited)

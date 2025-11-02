from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_map = {}
        for i in range(n):
            if manager[i] == -1:
                continue
            if manager[i] not in manager_map:
                manager_map[manager[i]] = []

            manager_map[manager[i]] += [i]

        self.r_walk(headID, informTime[headID], manager_map, informTime)
        return max(informTime)


    def r_walk(self, node: int, time: int, manager_map, informTime: List[int]):
        subordinates = manager_map[node] if node in manager_map else []
        for n in range(len(subordinates)):
            informTime[subordinates[n]] += time
            self.r_walk(subordinates[n], informTime[subordinates[n]], manager_map, informTime)

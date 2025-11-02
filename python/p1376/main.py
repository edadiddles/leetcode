from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.r_walk(headID, informTime[headID], manager, informTime)
        return max(informTime)


    def r_walk(self, node: int, time: int, manager: List[int], informTime: List[int]):
        subordinates = [i for i in range(len(manager)) if manager[i] == node]

        for n in subordinates:
            informTime[n] += time
            self.r_walk(n, informTime[n], manager, informTime)

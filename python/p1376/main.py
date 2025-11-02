from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        return self.r_walk(headID, 0, 0, manager, informTime)


    def r_walk(self, node: int, time: int, totalTime: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [(i, informTime[i]) for i in range(len(manager)) if manager[i] == node]
        subordinates.sort(key=lambda x: x[1], reverse=True)
        if len(subordinates) == 0:
            return time

        for (n, t) in subordinates:
            informTime[n] = 0
            if (tt := self.r_walk(n, time+t, totalTime, manager, informTime)) > totalTime:
                totalTime = tt

        return totalTime

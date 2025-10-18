from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = -1
        for k in range(1, len(coordinates)):
            m = (coordinates[k][1] - coordinates[k-1][1])/(coordinates[k][0] - coordinates[k-1][0])
            if slope == -1:
                slope = m
                continue

            if slope != m:
                return False

        return True

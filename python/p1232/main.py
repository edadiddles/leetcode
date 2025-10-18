from typing import List
import math


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = None
        for k in range(1, len(coordinates)):
            m = [coordinates[k][0] - coordinates[k-1][0], coordinates[k][1] - coordinates[k-1][1]]
            l = math.sqrt(m[0]**2 + m[1]**2)
            m = [m[0]/l, m[1]/l]
            if m[0] < 0 or (m[0] == 0 and m[1] < 0):
                m = list(map(lambda x: -x, m))
            if slope is None:
                slope = m
                continue

            print(f"slope: {slope} -- m: {m}")
            if slope != m:
                return False

        return True

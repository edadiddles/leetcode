from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        till = 0
        for bill in bills:
            till -= (bill-5)
            if till < 0:
                return False

            till += 5

        return True

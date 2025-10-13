from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        till = {"5": 0, "10": 0, "20": 0}
        for bill in bills:
            till[str(bill)] += 1
            bill -= 5
            while bill > 0:
                if bill >= 10 and till["10"] > 0:
                    till["10"] -= 1
                    bill -= 10
                elif till["5"] > 0:
                    till["5"] -= 1
                    bill -= 5
                else:
                    return False

        return True

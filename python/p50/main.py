import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        inverse = False
        if n < 0:
            inverse = True
            n *= -1

        pow = self._pow(x, n)

        if inverse:
            pow = 1/pow

        return pow

    def _pow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n % 2 > 0:
            return self._pow(x, n-1) * x

        p = self._pow(x, math.ceil(n/2))
        return p * p

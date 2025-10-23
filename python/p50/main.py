class Solution:
    def myPow(self, x: float, n: int) -> float:
        inverse = False
        if n < 0:
            inverse = True
            n *= -1

        pow = 1.0
        while n > 0:
            n -= 1
            pow *= x

        if inverse:
            pow = 1/pow

        return pow


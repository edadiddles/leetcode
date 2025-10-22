class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l = len(num1) if len(num1) > len(num2) else len(num2)
        num1_arr = list(num1.zfill(l)[::-1])
        num2_arr = list(num2.zfill(l)[::-1])

        sum = 0
        for k1, n1 in enumerate(num1_arr):
            for k2, n2 in enumerate(num2_arr):
                sum += (int(n1) * 10**k1) * (int(n2) * 10**k2)

        return str(sum)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l = len(num1) if len(num1) > len(num2) else len(num2)

        sum = 0
        for k1, n1 in enumerate(list(num1.zfill(l))):
            for k2, n2 in enumerate(list(num2.zfill(l))):
                sum += (int(n1) * 10**(l-1-k1)) * (int(n2) * 10**(l-1-k2))

        return str(sum)

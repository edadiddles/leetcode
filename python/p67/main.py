class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = len(a) if len(a) > len(b) else len(b)

        a = a.zfill(length+1)
        b = b.zfill(length+1)

        carry = False
        k = length
        output = ""
        while k >= 0:
            if carry and a[k] == "1" and b[k] == "1":
                output = "1" + output
                carry = True
            elif carry and (a[k] == "1" or b[k] == "1"):
                output = "0" + output
                carry = True
            elif carry:
                output = "1" + output
                carry = False
            elif a[k] == "1" and b[k] == "1":
                output = "0" + output
                carry = True
            elif a[k] == "1" or b[k] == "1":
                output = "1" + output
                carry = False
            else:
                output = "0" + output
                carry = False

            k -= 1

        while output.startswith("0"):
            if len(output) == 1:
                break

            output = output[1:]

        return output

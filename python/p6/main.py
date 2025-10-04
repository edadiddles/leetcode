class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []

        k = 0
        m = 1
        for c in s:
            if len(arr) < numRows:
                arr.append([])
            arr[k % numRows].append(c)
            if k == numRows-1:
                m = -1
            elif k == 0:
                m = 1

            k += m

        output = ""
        for a in arr:
            output += "".join(a)

        return output

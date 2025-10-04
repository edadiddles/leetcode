from main import Solution


def test_1():
    soln = Solution()
    assert soln.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

def test_2():
    soln = Solution()
    assert soln.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

def test_3():
    soln = Solution()
    assert soln.convert("A", 1) == "A"

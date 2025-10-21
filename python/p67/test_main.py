from main import Solution


def test1():
    soln = Solution()
    assert soln.addBinary("11", "1") == "100"


def test2():
    soln = Solution()
    assert soln.addBinary("1010", "1011") == "10101"

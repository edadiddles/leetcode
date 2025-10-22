from main import Solution


def test1():
    soln = Solution()
    assert soln.multiply("2", "3") == "6"


def test2():
    soln = Solution()
    assert soln.multiply("123", "456") == "56088"

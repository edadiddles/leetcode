from main import Solution


def test1():
    soln = Solution()
    assert soln.average([4000,3000,1000,2000]) == 2500.00000


def test2():
    soln = Solution()
    assert soln.average([1000,2000,3000]) == 2000.00000

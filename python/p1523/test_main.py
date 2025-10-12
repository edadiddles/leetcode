from main import Solution


def test1():
    soln = Solution()
    assert soln.countOdds(3, 7) == 3


def test2():
    soln = Solution()
    assert soln.countOdds(8, 10) == 1


def test3():
    soln = Solution()
    assert soln.countOdds(14, 17) == 2

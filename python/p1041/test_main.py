from main import Solution


def test1():
    soln = Solution()
    assert soln.isRobotBounded("GGLLGG")


def test2():
    soln = Solution()
    assert not soln.isRobotBounded("GG")


def test3():
    soln = Solution()
    assert soln.isRobotBounded("GL")

from main import Solution


def test1():
    soln = Solution()
    assert soln.numOfMinutes(1, 0, [-1], [0]) == 0


def test2():
    soln = Solution()
    assert soln.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]) == 0

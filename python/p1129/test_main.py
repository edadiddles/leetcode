from main import Solution


def test1():
    soln = Solution()
    assert soln.shortestAlternatingPaths(3, [[0,1], [1,2]], []) == [0, 1, -1]


def test2():
    soln = Solution()
    assert soln.shortestAlternatingPaths(3, [[0,1]], [[2,1]]) == [0, 1, -1]

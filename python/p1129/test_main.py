from main import Solution


def test1():
    soln = Solution()
    assert soln.shortestAlternatingPaths(3, [[0,1], [1,2]], []) == [0, 1, -1]


def test2():
    soln = Solution()
    assert soln.shortestAlternatingPaths(3, [[0,1]], [[2,1]]) == [0, 1, -1]


def test3():
    soln = Solution()
    assert soln.shortestAlternatingPaths(5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]]) == [0,1,2,3,7]

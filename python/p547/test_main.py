from main import Solution


def test1():
    soln = Solution()
    assert soln.findCircleNum([[1,1,0], [1,1,0], [0,0,1]])


def test2():
    soln = Solution()
    assert soln.findCircleNum([[1,0,0], [0,1,0], [0,0,1]])

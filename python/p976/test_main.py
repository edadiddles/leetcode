from main import Solution


def test1():
    soln = Solution()
    assert soln.largestPerimeter([2,1,2]) == 5

def test2():
    soln = Solution()
    assert soln.largestPerimeter([1,2,1,10]) == 0

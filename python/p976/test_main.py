from main import Solution


def test1():
    soln = Solution()
    assert soln.largestPerimeter([2,1,2]) == 5

def test2():
    soln = Solution()
    assert soln.largestPerimeter([1,2,1,10]) == 0

def test3():
    soln = Solution()
    assert soln.largestPerimeter([1,4,18,3,8,4,4]) == 12

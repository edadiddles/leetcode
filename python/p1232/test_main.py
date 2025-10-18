from main import Solution


def test1():
    soln = Solution()
    assert soln.checkStraightLine([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]]) == True


def test2():
    soln = Solution()
    assert soln.checkStraightLine([[1,1], [2,2], [3,4], [4,5], [5,6], [7,7]]) == False

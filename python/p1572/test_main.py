from main import Solution


def test1():
    soln = Solution()
    assert soln.diagonalSum([[1,2,3], [4,5,6], [7,8,9]]) == 25

def test2():
    soln = Solution()
    assert soln.diagonalSum([[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]) == 8

def test3():
    soln = Solution()
    assert soln.diagonalSum([[5]]) == 5

from main import Solution


def test1():
    soln = Solution()
    assert soln.spiralOrder([[1,2,3], [4,5,6], [7,8,9]]) == [1,2,3,6,9,8,7,4,5]

def test2():
    soln = Solution()
    assert soln.spiralOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

def test3():
    soln = Solution()
    assert soln.spiralOrder([[23,18,20,26,25], [24,22,3,4,4], [15,22,2,24,29], [18,15,23,28,28]]) == [23,18,20,26,25,4,29,28,28,23,15,18,15,24,22,3,4,24,2,22]

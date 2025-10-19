from main import Solution


def test1():
    soln = Solution()
    assert soln.checkStraightLine([[1,2], [2,3], [3,4], [4,5], [5,6], [6,7]]) == True


def test2():
    soln = Solution()
    assert soln.checkStraightLine([[1,1], [2,2], [3,4], [4,5], [5,6], [7,7]]) == False


def test3():
    soln = Solution()
    assert soln.checkStraightLine([[0,0], [0,1], [0,-1]]) == True


def test4():
    soln = Solution()
    assert soln.checkStraightLine([[-2,12],[2,-8],[6,-28],[-10,52],[-7,37],[4,-18],[7,-33],[1,-3],[-1,7],[8,-38]]) == True

from main import Solution


def test1():
    soln = Solution()
    assert soln.canVisitAllRooms([[1], [2], [3], []]) == True


def test2():
    soln = Solution()
    assert soln.canVisitAllRooms([[1,3], [3,0,1], [2], [0]]) == False

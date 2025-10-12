from main import Solution


def test1():
    soln = Solution()
    matrix = [[1,1,1], [1,0,1], [1,1,1]]
    soln.setZeroes(matrix)
    assert matrix == [[1,0,1], [0,0,0], [1,0,1]]

def test2():
    soln = Solution()
    matrix = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
    soln.setZeroes(matrix)
    assert matrix == [[0,0,0,0], [0,4,5,0], [0,3,1,0]]

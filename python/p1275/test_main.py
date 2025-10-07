from main import Solution


def test1():
    soln = Solution()
    assert soln.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == "A"

def test2():
    soln = Solution()
    assert soln.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == "B"

def test3():
    soln = Solution()
    assert soln.tictactoe([[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]) == "Draw"

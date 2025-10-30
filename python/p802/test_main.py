from main import Solution


def test1():
    soln = Solution()
    assert soln.eventualSafeNodes([[1,2], [2,3], [5], [0], [5], [], []]) == [2, 4, 5, 6]


def test2():
    soln = Solution()
    assert soln.eventualSafeNodes([[1,2,3,4], [1,2], [3,4], [0,4], []]) == [4]


def test3():
    soln = Solution()
    assert soln.eventualSafeNodes([[], [0,2,3,4], [3], [4], []]) == [0, 1, 2, 3, 4]

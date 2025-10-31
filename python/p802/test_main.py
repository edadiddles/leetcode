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


def test4():
    soln = Solution()
    assert soln.eventualSafeNodes([[], [2], [3,4], [4], []]) == [0, 1, 2, 3, 4]


def test5():
    soln = Solution()
    assert soln.eventualSafeNodes([[1,2,4], [0,2,4], [3,4], [4], [2]]) == []


def test6():
    soln = Solution()
    assert soln.eventualSafeNodes([[0,6,7,9], [], [], [], [2,6,8], [7,9], [7,8,9], [], [6,9], [7]]) == [1,2,3,5,7,9]

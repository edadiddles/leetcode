from main import Solution

def test1():
    soln = Solution()
    assert soln.maximumWealth([[1,2,3], [3,2,1]]) == 6

def test2():
    soln = Solution()
    assert soln.maximumWealth([[1,5], [7,3], [3,5]]) == 10

def test3():
    soln = Solution()
    assert soln.maximumWealth([[2,8,7], [7,1,3], [1,9,5]]) == 17

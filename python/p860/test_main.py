from main import Solution


def test1():
    soln = Solution()
    assert soln.lemonadeChange([5,5,5,10,20]) == True


def test2():
    soln = Solution()
    assert soln.lemonadeChange([5,5,10,10,20]) == False

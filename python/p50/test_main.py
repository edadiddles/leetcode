from main import Solution
from pytest import approx


def test1():
    soln = Solution()
    assert soln.myPow(2.00000, 10) == approx(1024.00000)


def test2():
    soln = Solution()
    assert soln.myPow(2.10000, 3) == approx(9.26100)


def test3():
    soln = Solution()
    assert soln.myPow(2.00000, -2) == approx(0.25000)


def test4():
    soln = Solution()
    assert soln.myPow(0.00001, 2147483647) == approx(0.0)

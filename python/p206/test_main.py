from main import Solution, ListNode


def test1():
    soln = Solution()

    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    actual = soln.reverseList(n1)

    assert actual is not None
    assert actual.val == 5
    assert actual.next.val == 4
    assert actual.next.next.val == 3
    assert actual.next.next.next.val == 2
    assert actual.next.next.next.next.val == 1
    assert actual.next.next.next.next.next is None


def test2():
    soln = Solution()

    n2 = ListNode(2)
    n1 = ListNode(1, n2)

    actual = soln.reverseList(n1)

    assert actual is not None
    assert actual.val == 2
    assert actual.next.val == 1
    assert actual.next.next is None


def test3():
    soln = Solution()

    actual = soln.reverseList(None)

    assert actual is None

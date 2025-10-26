from main import Solution, ListNode


def test1():
    soln = Solution()

    # List1
    l1n3 = ListNode(3)
    l1n2 = ListNode(4, l1n3)
    l1n1 = ListNode(2, l1n2)

    # List2
    l2n3 = ListNode(4)
    l2n2 = ListNode(6, l2n3)
    l2n1 = ListNode(5, l2n2)

    actual = soln.addTwoNumbers(l1=l1n1, l2=l2n1)

    assert actual is not None
    assert actual.val == 7
    assert actual.next.val == 0
    assert actual.next.next.val == 8
    assert actual.next.next.next is None


def test2():
    soln = Solution()

    # List1
    l1n1 = ListNode(0)

    # List2
    l2n1 = ListNode(0)

    actual = soln.addTwoNumbers(l1=l1n1, l2=l2n1)

    assert actual is not None
    assert actual.val == 0
    assert actual.next is None


def test3():
    soln = Solution()

    # List1
    l1n7 = ListNode(9)
    l1n6 = ListNode(9, l1n7)
    l1n5 = ListNode(9, l1n6)
    l1n4 = ListNode(9, l1n5)
    l1n3 = ListNode(9, l1n4)
    l1n2 = ListNode(9, l1n3)
    l1n1 = ListNode(9, l1n2)

    # List2
    l2n4 = ListNode(9)
    l2n3 = ListNode(9, l2n4)
    l2n2 = ListNode(9, l2n3)
    l2n1 = ListNode(9, l2n2)

    actual = soln.addTwoNumbers(l1=l1n1, l2=l2n1)

    assert actual is not None
    assert actual.val == 8
    assert actual.next.val == 9
    assert actual.next.next.val == 9
    assert actual.next.next.next.val == 9
    assert actual.next.next.next.next.val == 0
    assert actual.next.next.next.next.next.val == 0
    assert actual.next.next.next.next.next.next.val == 0
    assert actual.next.next.next.next.next.next.next.val == 1
    assert actual.next.next.next.next.next.next.next.next is None

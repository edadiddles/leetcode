from main import Solution, ListNode


def test1():
    soln = Solution()

    # List 1
    l1_n3 = ListNode(val=4)
    l1_n2 = ListNode(val=2, next=l1_n3)
    l1_n1 = ListNode(val=1, next=l1_n2)

    # List 2
    l2_n3 = ListNode(val=4)
    l2_n2 = ListNode(val=3, next=l2_n3)
    l2_n1 = ListNode(val=1, next=l2_n2)

    actual = soln.mergeTwoLists(l1_n1, l2_n1)

    assert actual is not None
    assert actual.val == 1
    assert actual.next.val == 1
    assert actual.next.next.val == 2
    assert actual.next.next.next.val == 3
    assert actual.next.next.next.next.val == 4
    assert actual.next.next.next.next.next.val == 4
    assert actual.next.next.next.next.next.next is None


def test2():
    soln = Solution()

    # List 1
    l1_n1 = None

    # List 2
    l2_n1 = None

    actual = soln.mergeTwoLists(l1_n1, l2_n1)

    assert actual is None


def test3():
    soln = Solution()

    # List 1
    l1_n1 = None

    # List 2
    l2_n1 = ListNode(val=0)

    actual = soln.mergeTwoLists(l1_n1, l2_n1)

    assert actual is not None
    assert actual.val == 0
    assert actual.next is None

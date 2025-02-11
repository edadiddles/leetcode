package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    nums := []int{1,2,2,3}
    expected := true

    actual := isMonotonic(nums)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    nums := []int{6,5,4,4}
    expected := true

    actual := isMonotonic(nums)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    nums := []int{1,3,2}
    expected := false

    actual := isMonotonic(nums)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase4(t *testing.T) {
    nums := []int{2,2,2,1,4,5}
    expected := false

    actual := isMonotonic(nums)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

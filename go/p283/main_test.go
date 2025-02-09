package leetcode

import (
    "testing"
    "slices"
)

func TestCase1(t *testing.T) {
    nums := []int{0,1,0,3,12}

    expected := []int{1,3,12,0,0}
    moveZeroes(nums)

    if !slices.Equal(nums,expected) {
        t.Fatalf("Test Case 1 failed: (%v,%v)", nums, expected)
    }
}

func TestCase2(t *testing.T) {
    nums := []int{0}

    expected := []int{0}
    moveZeroes(nums)

    if !slices.Equal(nums,expected) {
        t.Fatalf("Test Case 2 failed: (%v,%v)", nums, expected)
    }
}

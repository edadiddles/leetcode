package leetcode

import (
    "testing"
    "slices"
)

func TestCase1(t *testing.T) {
    digits := []int{1,2,3}
    
    expected := []int{1,2,4}
    actual := plusOne(digits)

    if !slices.Equal(actual, expected) {
        t.Fatalf("Test Case 1 failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    digits := []int{4,3,2,1}
    
    expected := []int{4,3,2,2}
    actual := plusOne(digits)

    if !slices.Equal(actual, expected) {
        t.Fatalf("Test Case 2 failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    digits := []int{9}
    
    expected := []int{1,0}
    actual := plusOne(digits)

    if !slices.Equal(actual, expected) {
        t.Fatalf("Test Case 3 failed: (%v,%v)", actual, expected)
    }
}

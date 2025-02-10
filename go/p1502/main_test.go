package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    arr := []int{3,5,1}
    expected := true

    actual := canMakeArithmeticProgression(arr)

    if actual != expected {
        t.Fatalf("Failed: (%v, %v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    arr := []int{1,2,4}
    expected := false

    actual := canMakeArithmeticProgression(arr)

    if actual != expected {
        t.Fatalf("Failed: (%v, %v)", actual, expected)
    }
}

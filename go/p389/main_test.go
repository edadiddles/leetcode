package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    s := "abcd"
    u := "abcde"

    expected := byte('e')

    actual := findTheDifference(s,u)

    if actual != expected {
        t.Fatalf("Case 1 failed: (%s,%s)", string(actual), string(expected))
    }
}

func TestCase2(t *testing.T) {
    s := ""
    u := "y"

    expected := byte('y')

    actual := findTheDifference(s,u)

    if actual != expected {
        t.Fatalf("Case 2 failed: (%v, %v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    s := "abcd"
    u := "aebdc"

    expected := byte('e')

    actual := findTheDifference(s,u)

    if actual != expected {
        t.Fatalf("Case 3 failed: (%v, %v)", actual, expected)
    }
}

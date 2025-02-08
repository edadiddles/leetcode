package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    s := "abab"
    expected := true
    actual := repeatedSubstringPattern(s)

    if actual != expected {
        t.Fatalf("Test Case 1 failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    s := "aba"
    expected := false
    actual := repeatedSubstringPattern(s)

    if actual != expected {
        t.Fatalf("Test Case 2 failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    s := "abcabcabcabc"
    expected := true
    actual := repeatedSubstringPattern(s)

    if actual != expected {
        t.Fatalf("Test Case 3 failed: (%v,%v)", actual, expected)
    }
}

package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    a := "anagram"
    b := "nagaram"

    expected := true
    actual := isAnagram(a,b)

    if actual != expected {
        t.Fatalf("Test Case 1 failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    a := "rat"
    b := "cat"

    expected := false
    actual := isAnagram(a,b)

    if actual != expected {
        t.Fatalf("Test Case 2 failed: (%v,%v)", actual, expected)
    }
}

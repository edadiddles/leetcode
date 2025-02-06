package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    word1 := "abc"
    word2 := "pqr"

    expected := "apbqcr"

    actual := mergeAlternately(word1, word2)

    if actual != expected {
        t.Fatalf("Case 1 failed: (%v, %v)", expected, actual)
    }
}

func TestCase2(t *testing.T) {
    word1 := "ab"
    word2 := "pqrs"

    expected := "apbqrs"
    
    actual := mergeAlternately(word1, word2)

    if actual != expected {
        t.Fatalf("Case 2 failed: (%v, %v)", expected, actual)
    }
}

func TestCase3(t *testing.T) {
    word1 := "abcd"
    word2 := "pq"

    expected := "apbqcd"

    actual := mergeAlternately(word1, word2)

    if actual != expected {
        t.Fatalf("Case 3 failed: (%v, %v)", expected, actual)
    }
}

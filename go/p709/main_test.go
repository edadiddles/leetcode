package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    s := "Hello"
    expected := "hello"

    actual := toLowerCase(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    s := "here"
    expected := "here"

    actual := toLowerCase(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    s := "LOVELY"
    expected := "lovely"

    actual := toLowerCase(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}


package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    ops := []string{ "5","2","C","D","+" }
    expected := 30

    actual := calPoints(ops)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    ops := []string{ "5","-2","4","C","D","9","+","+" }
    expected := 27

    actual := calPoints(ops)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    ops := []string{ "1","C" }
    expected := 0

    actual := calPoints(ops)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}


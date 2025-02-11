package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    s := "III"
    expected := 3

    actual := romanToInt(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    s := "LVIII"
    expected := 58

    actual := romanToInt(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    s := "MCMXCIV"
    expected := 1994

    actual := romanToInt(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    s := "Hello World"
    expected := 5

    actual := lengthOfLastWord(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    s := "   fly me  to   the moon "
    expected := 4

    actual := lengthOfLastWord(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    s := "luffy is still joyboy"
    expected := 6

    actual := lengthOfLastWord(s)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

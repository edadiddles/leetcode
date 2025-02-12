package leetcode

import (
    "testing"
)

func TestCode1(t *testing.T) {
    moves := "UD"
    expected := true

    actual := judgeCircle(moves)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

func TestCode2(t *testing.T) {
    moves := "LL"
    expected := false

    actual := judgeCircle(moves)

    if actual != expected {
        t.Fatalf("Failed: (%v,%v)", actual, expected)
    }
}

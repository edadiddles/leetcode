package leetcode

import (
    "testing"
)

func TestCase1(t *testing.T) {
    a := "sadbutsad"
    b := "sad"

    expected := 0

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 1 failed: (%v,%v)", actual, expected)
    }
}

func TestCase2(t *testing.T) {
    a := "leetcode"
    b := "leeto"

    expected := -1

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 2 failed: (%v,%v)", actual, expected)
    }
}

func TestCase3(t *testing.T) {
    a := "littlittle"
    b := "little"

    expected := 4

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 3 failed: (%v,%v)", actual, expected)
    }
}

func TestCase4(t *testing.T) {
    a := "mississippi"
    b := "issi"

    expected := 1

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 4 failed: (%v,%v)", actual, expected)
    }
}

func TestCase5(t *testing.T) {
    a := "mississippi"
    b := "issipi"

    expected := -1

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 5 failed: (%v,%v)", actual, expected)
    }
}

func TestCase6(t *testing.T) {
    a := "mississippi"
    b := "pi"

    expected := 9

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 6 failed: (%v,%v)", actual, expected)
    }
}

func TestCase7(t *testing.T) {
    a := "ababbbbaaabbbaaa"
    b := "bbbb"

    expected := 3

    actual := strStr(a,b)

    if actual != expected {
        t.Fatalf("Case 7 failed: (%v,%v)", actual, expected)
    }
}


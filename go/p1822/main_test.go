package leetcode

import (
    "testing"
    "fmt"
)

func TestCases(t *testing.T) {
    var tests = []struct {
        nums []int
        expected int
    }{
        { []int{-1,-2,-3,-4,3,2,1}, 1 },
        { []int{1,5,0,2,-3}, 0 },
        { []int{-1,1,-1,1,-1}, -1 },
    }

    for _, tt := range tests {
        testname := fmt.Sprintf("%v", tt.nums)
        t.Run(testname, func(t *testing.T) {
            actual := arraySign(tt.nums)
            if actual != tt.expected {
                t.Fatalf("Failed: (%v,%v)", actual, tt.expected)
            }
        })
    }
}

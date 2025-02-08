package leetcode

import (
    "math"
)


func repeatedSubstringPattern(s string) bool {
    primes := []int{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199}
    l := len(s)

    v := 0.0
    for p:=0; p < len(primes); p++ {
        v = float64(l)/float64(primes[p])

        if math.Ceil(v) == math.Floor(v) { // crude check if integer
            n := int(v)

            is_equal := true
            prev := ""
            for j:=0; j < primes[p]; j++ {
                k := j*n
                curr := s[k:k+n]
                if j != 0 && curr != prev {
                    is_equal = false
                    break
                }
                prev = curr
            }

            if is_equal {
                return true
            }
        }
    }

    return false
}

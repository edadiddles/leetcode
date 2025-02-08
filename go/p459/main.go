package leetcode

import (
    "math"
)


func repeatedSubstringPattern(s string) bool {
    primes := []int{2,3,5,7,11,13,17,19,23}
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

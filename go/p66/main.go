package leetcode

func plusOne(digits []int) []int {
    out := make([]int, len(digits)+1)

    carry := false
    if digits[len(digits)-1] == 9 {
        carry = true
    } else {
        out[len(digits)] = digits[len(digits)-1]+1
    }

    i := len(digits)-1
    for ; i > 0; i-- {
        if carry && digits[i-1] == 9 {
            if digits[i-1] == 9 {
                carry=true
            } else {
                out[i] = digits[i-1]+1
            }
        } else {
            out[i] = digits[i-1]
        }
    }

    if carry {
        i = -1
        out[0] = 1
    }

    return out[i+1:]
}

package leetcode

func strStr(haystack string, needle string) int {
    prev_idx := -1
    next_idx := -1

    for i,j:=0,0; i < len(haystack); i++ {
        if next_idx <= 0 && needle[0] == haystack[i] {
            next_idx = i-1
        }

        if haystack[i] != needle[j] {
            if next_idx != -1 && prev_idx != next_idx {
                i = next_idx
                prev_idx = next_idx
                next_idx = -1
            } else {
                i += j
            }

            j = 0
            continue
        }

        if j == len(needle)-1 {
            return i-j
        }
        j++
    }

    return -1
}

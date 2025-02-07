package leetcode

func strStr(haystack string, needle string) int {
    next_start_idx := -1
    for i,j:=0,0; i < len(haystack); i++ {
       if next_start_idx <= 0 && needle[0] == haystack[i] {
            next_start_idx = i-1
        }

        if haystack[i] != needle[j] {
            if next_start_idx != -1 {
                i = next_start_idx
                next_start_idx = -1
            } else {
                i += j+1
            }

            j = 0
            continue
        }

        j++
        if j >= len(needle) {
            return i-(j-1)
        }
    }

    return -1
}

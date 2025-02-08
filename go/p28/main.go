package leetcode

func strStr(haystack string, needle string) int {

    for i,j:=0,0; i < len(haystack); i++ {
        if haystack[i] == needle[j] {
            if j == len(needle)-1 {
                return i-j
            }

            j++
        } else {
            i = i-j
            j = 0
        }
    }
   

    return -1
}

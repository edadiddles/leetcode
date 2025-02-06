package leetcode

func findTheDifference(s string, t string) byte {
    for i:=0; i<len(t); i++ {
        has_match := false
        for j:=0; j<len(s); j++ {
            if t[i] == s[j] {
                has_match = true
            }
        }

        if !has_match {
            return t[i]
        }
    }

    // this should be dead code, but required for compilation
    // constraints of problem guarantee the return will be executed in above for-loop
    return t[0]
}

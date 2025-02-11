package leetcode

func toLowerCase(s string) string {
    a := make([]byte, len(s))
    for i:=0; i < len(s); i++ {
        // chk for uppercase ascii vals
        if s[i] >= 65 && s[i] <= 90 {
            // add offset value to lowercase vals
            a[i] = s[i] + 32
        } else {
            a[i] = s[i]
        }
    }

    return string(a)
}

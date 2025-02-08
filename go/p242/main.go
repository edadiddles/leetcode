package leetcode

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    s = bubbleSort([]byte(s))
    t = bubbleSort([]byte(t))

    for i:=0; i < len(s); i++ {
        if s[i] != t[i] {
            return false
        }
    }

    return true
}

func bubbleSort(s []byte) string {
    for i:=0; i < len(s)-1; i++ {
        for j:=i+1; j < len(s); j++ {
            if s[i] > s[j] {
                temp := s[i]
                s[i] = s[j]
                s[j] = temp
            }
        }
    }

    return string(s)
}


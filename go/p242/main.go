package leetcode

type charCount struct {
    A int
    B int
}

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    counts := make(map[byte]charCount)


    for i:=0; i < len(s); i++ {
        c := counts[s[i]]
        c.A += 1
        counts[s[i]] = c
        c = counts[t[i]]
        c.B += 1
        counts[t[i]] = c
    }

    for _, value := range counts {
        if value.A != value.B {
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


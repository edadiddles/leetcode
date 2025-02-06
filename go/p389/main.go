package leetcode

type CharCount struct {
    S int
    T int
}

func findTheDifference(s string, t string) byte {
    charHistogram := make(map[byte]CharCount)
    i:=0
    for ; i<len(t); i++ {
        h := charHistogram[t[i]]
        h.T += 1
        charHistogram[t[i]] = h

        if i < len(s) {
            h = charHistogram[s[i]]
            h.S += 1
            charHistogram[s[i]] = h
        }
    }

    var out byte
    for key, value := range charHistogram {
        if value.S != value.T {
            out = key
            break
        }
    }

    return out
}

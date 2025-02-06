package leetcode

func mergeAlternately(word1 string, word2 string) string {
    out := ""
    i := 0
    for ; i < len(word1) && i < len(word2); i++ {
        out += string(word1[i])
        out += string(word2[i])
    }
    if i < len(word1) {
        out += string(word1[i:])
    }
    if i < len(word2) {
        out += string(word2[i:])
    }


    return out
}

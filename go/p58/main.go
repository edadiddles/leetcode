package leetcode

func lengthOfLastWord(s string) int {
    word_length := 0
    for i:=len(s)-1; i >= 0; i-- {
        if s[i] != ' ' {
            word_length++
        } else if s[i] == ' ' && word_length > 0 {
            return word_length
        }
    }


    return word_length
}

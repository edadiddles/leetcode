package leetcode

func romanToInt(s string) int {
    sum := 0

    prev := resolveRoman(s[0])

    if len(s) == 1 {
        return prev
    }

    next := 0
    for i:=1; i < len(s); i++ {
        next = resolveRoman(s[i])
        if prev != 0 && next > prev {
            sum += (next-prev)
            prev = 0
            next = 0
        } else {
            sum += prev
            prev = next
        }
    }

    sum += next

    return sum
}


func resolveRoman(c byte) int {
    switch c {
    case 'I':
        return 1
    case 'V':
        return 5
    case 'X':
        return 10
    case 'L':
        return 50
    case 'C':
        return 100
    case 'D':
        return 500
    case 'M':
        return 1000
    }

    return 0
}

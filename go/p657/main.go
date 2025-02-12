package leetcode

func judgeCircle(moves string) bool {
    x := 0
    y := 0

    for i:=0; i < len(moves); i++ {
        switch moves[i] {
        case 'U':
            y++
        case 'D':
            y--
        case 'L':
            x--
        case 'R':
            x++
        }
    }

    return x == 0 && y == 0
}

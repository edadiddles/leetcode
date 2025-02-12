package leetcode

func judgeCircle(moves string) bool {
    pos := [2]int{ 0,0 }

    for i:=0; i < len(moves); i++ {
        switch moves[i] {
        case 'U':
            pos[1]++
        case 'D':
            pos[1]--
        case 'L':
            pos[0]--
        case 'R':
            pos[0]++
        }
    }

    return pos[0] == 0 && pos[1] == 0
}

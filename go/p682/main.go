package leetcode

import (
    "strconv"
)

func calPoints(operations []string) int {
    score_card := make([]int, 0)
    for i:=0; i < len(operations); i++ {
        switch operations[i] {
        case "C":
            score_card = score_card[0:len(score_card)-1]
        case "D":
            score_card = append(score_card, 2*score_card[len(score_card)-1])
        case "+":
            score_card = append(score_card, score_card[len(score_card)-1]+score_card[len(score_card)-2])
        default:
            s, _ := strconv.Atoi(operations[i])
            score_card = append(score_card, s)
        }
    }

    sum := 0
    for i:=0; i < len(score_card); i++ {
        sum += score_card[i]
    }

    return sum
}

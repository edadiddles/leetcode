package leetcode

import "fmt"

func canMakeArithmeticProgression(arr []int) bool {
    //bubble sort
    for i:=0; i < len(arr)-1; i++ {
        for j:=1; j < len(arr); j++ {
            if arr[i] > arr[j] {
                temp := arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            }
        }
    }

    // iterate checking the diff
    diff := arr[1] - arr[0]
    for i:=1; i < len(arr)-1; i++ {
        if diff != (arr[i+1] - arr[i]) {
            return false
        }
    }

    return true
}

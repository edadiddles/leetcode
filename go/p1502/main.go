package leetcode

func canMakeArithmeticProgression(arr []int) bool {
    // bubble sort
    for i:=0; i < len(arr)-1; i++ {
        for j:=i+1; j < len(arr); j++ {
            if arr[i] > arr[j] {
                temp := arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            }
        }
    }

    // interate calculating diffs
    diff := arr[1] - arr[0]
    for i:=1; i < len(arr)-1; i++ {
        if diff != (arr[i+1] - arr[i]) {
            return false
        }
    }

    return true
}

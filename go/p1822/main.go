package leetcode

func arraySign(nums []int) int {
    num_neg := 0
    for i:=0; i < len(nums); i++ {
        if nums[i] == 0 {
            return 0
        }

        if nums[i] < 0 {
            num_neg++
        }
    }

    if num_neg % 2 == 0 {
        return 1
    }

    return -1
}

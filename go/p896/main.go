package leetcode

func isMonotonic(nums []int) bool {
    chk := 0
    i:=0
    for ; chk == 0 && i < len(nums)-1; i++ {
        chk = nums[i] - nums[i+1]
    }

    for ; i < len(nums)-1; i++ {
        if chk * (nums[i] - nums[i+1]) < 0 {
            return false
        }
    }

    return true
}

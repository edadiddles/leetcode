package leetcode

func isMonotonic(nums []int) bool {
    chk := nums[0] - nums[1]

    for i:=1; i < len(nums)-1; i++ {
        if chk * (nums[i] - nums[i+1]) < 0 {
            return false
        }
    }

    return true
}

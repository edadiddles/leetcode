package leetcode

func moveZeroes(nums []int) {
    temp := make([]int, len(nums))
    for i,j:= 0,0; i < len(nums); i++ {
        if nums[i] != 0 {
            temp[j] = nums[i]
            j++
        }
    }

    for i:=0; i < len(nums); i++ {
        nums[i] = temp[i]
    }
}

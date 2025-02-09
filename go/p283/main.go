package leetcode

func moveZeroes(nums []int) {
    z_idx := len(nums)-1
    for i:=len(nums)-1; i >= 0; i-- {
        if nums[i] != 0 {
            z_idx = i
            break
        }
    }

    for i:=z_idx-1; i >= 0; i-- {
        if nums[i] == 0 {
            for j,k:=i,i+1; k <= z_idx; k++ {
                temp := nums[k]
                nums[k] = nums[j]
                nums[j] = temp
                j++
            }
            z_idx--
        }
    }
}

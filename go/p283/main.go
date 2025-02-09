package leetcode

func moveZeroes(nums []int) {
    // track idx of right most non-zero number
    z_idx := len(nums)-1
    for i:=len(nums)-1; i >= 0; i-- {
        if nums[i] != 0 {
            z_idx = i
            break
        }
    }

    // track idx of left most zero
    n_idx := 0
    for i:=0; i < z_idx; i++ {
        if nums[i] == 0 {
            n_idx = i
            break
        }
    }

    for i:=z_idx-1; i >= n_idx; i-- {
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

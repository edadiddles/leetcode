from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)

        max_perimeter = 0
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]

                    perimeter = a+b+c
                    if c >= a and c < a+b and max_perimeter < perimeter:
                        max_perimeter = perimeter

        return max_perimeter

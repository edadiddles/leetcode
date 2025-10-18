from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)

        i = len(nums) - 3
        while i >= 0:
            j = len(nums) - 2
            while j >= 1 and j > i:
                k = len(nums) - 1
                while k >= 2 and k > j:
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]

                    perimeter = a+b+c
                    if c < a+b:
                        return perimeter

                    k -= 1
                j -= 1
            i -= 1

        return 0

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        sorted_nums, n, res = sorted(nums), len(nums), 0
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] > sorted_nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res

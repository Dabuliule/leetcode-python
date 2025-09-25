import math
from collections import deque
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        queue = deque()

        for num in nums:
            while queue and math.gcd(queue[-1], num) > 1:
                num = math.lcm(queue.pop(), num)
            queue.append(num)

        return list(queue)


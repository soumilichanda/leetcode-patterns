"""
LeetCode 1696: Jump Game VI
Difficulty: Medium
Pattern: Monotonic Queue DP (Bounded-Step Sliding Window Maximum)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq: deque[int] = deque([0])

        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = nums[i] + dp[dq[0]]

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxResult([1, -1, -2, 4, -7, 3], 2) == 7
    assert sol.maxResult([10, -5, -2, 4, 0, 3], 3) == 17
    assert sol.maxResult([1, -5, -20, 4, -1, 3, -6, -3], 2) == 0
    print("LC 1696 verified successfully!")

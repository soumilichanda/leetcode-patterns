"""
LeetCode 1425: Constrained Subsequence Sum
Difficulty: Hard
Pattern: Monotonic Queue DP (Sliding-Window Maximum with Decreasing Deque)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dq: deque[int] = deque()
        max_sum = nums[0]

        for i in range(n):
            while dq and dq[0] < i - k:
                dq.popleft()

            best_prev = dp[dq[0]] if dq else 0
            dp[i] = nums[i] + max(0, best_prev)
            max_sum = max(max_sum, dp[i])

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()
            dq.append(i)

        return max_sum


if __name__ == "__main__":
    sol = Solution()
    assert sol.constrainedSubsetSum([10, 2, -10, 5, 20], 2) == 37
    assert sol.constrainedSubsetSum([-1, -2, -3], 1) == -1
    assert sol.constrainedSubsetSum([10, -2, -10, -5, 20], 2) == 23
    print("LC 1425 verified successfully!")

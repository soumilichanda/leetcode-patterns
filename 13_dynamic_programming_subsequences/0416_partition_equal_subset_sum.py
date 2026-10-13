"""
LeetCode 416: Partition Equal Subset Sum
Pattern: 0/1 Knapsack / Subset Sum Boolean DP
Time Complexity: O(n * target) where target = sum(nums) // 2
Space Complexity: O(target)
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for w in range(target, num - 1, -1):
                if dp[w - num]:
                    dp[w] = True
            if dp[target]:
                return True

        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([2, 2, 3, 5], False),
    ]

    for nums, expected in test_cases:
        res = sol.canPartition(nums)
        assert res == expected, f"Failed for {nums}: expected {expected}, got {res}"
        print(f"nums={nums} -> Can Partition: {res} (Passed)")

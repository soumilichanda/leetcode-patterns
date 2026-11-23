"""
LeetCode 698: Partition to K Equal Sum Subsets
Difficulty: Medium
Pattern: Bitmask DP (Subset-Sum Modulo Bucket Transition)

Time Complexity: O(n * 2^n)
Space Complexity: O(2^n)
"""

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort()
        if nums[-1] > target:
            return False

        n = len(nums)
        full_mask = (1 << n) - 1
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            rem = dp[mask]
            for i in range(n):
                if not (mask & (1 << i)):
                    if rem + nums[i] <= target:
                        nxt = mask | (1 << i)
                        dp[nxt] = (rem + nums[i]) % target
                    else:
                        break

        return dp[full_mask] == 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True
    assert sol.canPartitionKSubsets([1, 2, 3, 4], 3) is False
    print("LC 698 verified successfully!")

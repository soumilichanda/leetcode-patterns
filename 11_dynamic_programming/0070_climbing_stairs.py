"""
LeetCode 70: Climbing Stairs
Difficulty: Easy
Pattern: Cluster 11 — Dynamic Programming (1D Space-Optimized Fibonacci)

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(2) == 2, f"Expected 2, got {sol.climbStairs(2)}"
    assert sol.climbStairs(3) == 3, f"Expected 3, got {sol.climbStairs(3)}"
    assert sol.climbStairs(5) == 8, f"Expected 8, got {sol.climbStairs(5)}"
    print("LC 70 (Climbing Stairs): Verified successfully in O(1) space!")

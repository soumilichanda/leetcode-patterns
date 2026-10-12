"""
LeetCode 62: Unique Paths
Difficulty: Medium
Pattern: Cluster 12 ? 2D Dynamic Programming (Rolling Row Optimization)

Time Complexity: O(m * n)
Space Complexity: O(n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            curr_row = [1] * n
            for j in range(1, n):
                curr_row[j] = curr_row[j - 1] + row[j]
            row = curr_row

        return row[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28, f"Expected 28, got {sol.uniquePaths(3, 7)}"
    assert sol.uniquePaths(3, 2) == 3, f"Expected 3, got {sol.uniquePaths(3, 2)}"
    assert sol.uniquePaths(1, 1) == 1, f"Expected 1, got {sol.uniquePaths(1, 1)}"
    print("LC 62 (Unique Paths): Verified successfully in O(n) space!")

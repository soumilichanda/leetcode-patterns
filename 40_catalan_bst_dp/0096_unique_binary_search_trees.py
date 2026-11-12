"""
LeetCode 96: Unique Binary Search Trees
Difficulty: Medium
Pattern: Catalan Dynamic Programming (1D Subtree Structural Counting)

Invariant:
    For k distinct sorted keys, selecting key i (1 <= i <= k) as root
    partitions the tree into (i - 1) left keys and (k - i) right keys:
    G(k) = sum_{i=1}^{k} G(i - 1) * G(k - i), with G(0) = G(1) = 1.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                left_trees = dp[root - 1]
                right_trees = dp[nodes - root]
                dp[nodes] += left_trees * right_trees

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.numTrees(1) == 1
    assert sol.numTrees(3) == 5
    assert sol.numTrees(4) == 14
    print("LC 96 (Unique Binary Search Trees) verified successfully!")

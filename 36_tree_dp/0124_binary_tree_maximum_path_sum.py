"""
LeetCode 124: Binary Tree Maximum Path Sum
Difficulty: Hard
Pattern: Cluster 36 — Tree Dynamic Programming (Post-Order Branch Pruning)

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Prune negative paths by clamping to 0
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            # Price of new path rooted at this node
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Return maximum branch extending upwards to parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return int(max_sum)


if __name__ == "__main__":
    # Tree: [1, 2, 3] -> Expected: 6
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    sol = Solution()
    assert sol.maxPathSum(t1) == 6

    # Tree: [-10, 9, 20, None, None, 15, 7] -> Expected: 42
    t2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.maxPathSum(t2) == 42
    print("LC 124 verified successfully!")

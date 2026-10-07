"""
LeetCode 104: Maximum Depth of Binary Tree
Difficulty: Easy
Pattern: Trees (Divide-and-Conquer Post-Order Reduction)

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # Test Tree: [3, 9, 20, None, None, 15, 7] (Depth = 3)
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    depth = sol.maxDepth(root)

    print("=== LC 104: Maximum Depth ===")
    print(f"Computed Depth: {depth} (Expected: 3)")

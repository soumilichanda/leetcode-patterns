"""
LeetCode 226: Invert Binary Tree
Difficulty: Easy
Pattern: Trees (Recursive Post-Order Pointer Swap)

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Recursively swap child branches
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root


if __name__ == "__main__":
    # Test Tree: [4, 2, 7]
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    sol = Solution()
    inverted = sol.invertTree(root)

    print("=== LC 226: Invert Binary Tree ===")
    print(f"Root: {inverted.val}, Left: {inverted.left.val}, Right: {inverted.right.val}")
    print("Expected: Root: 4, Left: 7, Right: 2")

"""
LeetCode 543: Diameter of Binary Tree
Difficulty: Easy / Core Tree Pattern
Pattern: Tree DP / Post-Order Subtree Depth Propagation

Time Complexity: O(n)
Space Complexity: O(h) where h is the tree height
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def get_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)

            # Update the longest path passing through this node
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            # Return height of this subtree to parent
            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return self.max_diameter


if __name__ == "__main__":
    # Test Tree: [1, 2, 3, 4, 5] -> Diameter = 3 (Path: [4, 2, 1, 3] or [5, 2, 1, 3])
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    sol = Solution()
    res = sol.diameterOfBinaryTree(root)
    assert res == 3, f"Expected 3, got {res}"
    print("LC 543 (Diameter of Binary Tree) verified successfully!")

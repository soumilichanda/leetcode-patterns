"""
LeetCode 687: Longest Univalue Path
Difficulty: Medium
Pattern: Tree DP / Single-Branch Directional Propagation

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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def post_order(node: Optional[TreeNode]) -> int:
            nonlocal max_path
            if not node:
                return 0

            left_len = post_order(node.left)
            right_len = post_order(node.right)

            left_arrow = 0
            right_arrow = 0

            # Directional branch invariants
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1

            # Update diameter-style univalue path rooted at this node
            max_path = max(max_path, left_arrow + right_arrow)

            # Propagate the single longest univalue branch to the parent
            return max(left_arrow, right_arrow)

        post_order(root)
        return max_path


if __name__ == "__main__":
    # Test Tree: [5, 4, 5, 1, 1, None, 5] -> Longest univalue path is 2 (5-5-5)
    root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))
    sol = Solution()
    res = sol.longestUnivaluePath(root)
    assert res == 2, f"Expected 2, got {res}"
    print("LC 687 (Longest Univalue Path) verified successfully!")

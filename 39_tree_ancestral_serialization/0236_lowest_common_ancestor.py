"""
LeetCode 236: Lowest Common Ancestor of a Binary Tree
Difficulty: Medium / Core Tree Ancestral Pattern
Pattern: Tree DP / Post-Order Subtree State Bubbling

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
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # Base case: empty node or found one of the targets
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Invariant: If both subtrees yield a non-null match, current root is the LCA split point
        if left and right:
            return root

        # Otherwise, bubble up whichever non-null reference was discovered
        return left if left else right


if __name__ == "__main__":
    # Tree: [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node2 = TreeNode(2, node7, node4)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node6, node2)

    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node1 = TreeNode(1, node0, node8)

    root = TreeNode(3, node5, node1)

    sol = Solution()
    # LCA of 5 and 1 should be 3
    lca1 = sol.lowestCommonAncestor(root, node5, node1)
    assert lca1 and lca1.val == 3, f"Expected 3, got {lca1.val if lca1 else None}"

    # LCA of 5 and 4 should be 5
    lca2 = sol.lowestCommonAncestor(root, node5, node4)
    assert lca2 and lca2.val == 5, f"Expected 5, got {lca2.val if lca2 else None}"

    print("LC 236 (Lowest Common Ancestor) verified successfully!")

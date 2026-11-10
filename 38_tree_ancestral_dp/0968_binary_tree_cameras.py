"""
LeetCode 968: Binary Tree Cameras
Difficulty: Hard / Core Tree DP
Pattern: Tree DP / Post-Order 3-State Greedy Coverage

States:
  0: Node is uncovered (needs camera)
  1: Node has camera installed
  2: Node is covered by child camera

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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        cameras = 0

        # State 0: uncovered, State 1: has camera, State 2: covered without camera
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal cameras
            if not node:
                return 2  # Null nodes are considered covered

            left_state = dfs(node.left)
            right_state = dfs(node.right)

            # Invariant 1: If either child is uncovered, place camera here
            if left_state == 0 or right_state == 0:
                cameras += 1
                return 1

            # Invariant 2: If either child has a camera, this node is covered
            if left_state == 1 or right_state == 1:
                return 2

            # Invariant 3: Both children are covered (state 2), so this node is uncovered
            return 0

        # Root edge case: if root itself remains uncovered, place 1 final camera
        if dfs(root) == 0:
            cameras += 1

        return cameras


if __name__ == "__main__":
    # Test Tree 1: [0, 0, None, 0, 0] -> min cameras = 1
    root1 = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)), None)
    sol = Solution()
    res1 = sol.minCameraCover(root1)
    assert res1 == 1, f"Expected 1, got {res1}"

    # Test Tree 2: [0, 0, None, 0, None, 0, None, None, 0] -> min cameras = 2
    # Chain of 4 nodes: 0 -> 0 -> 0 -> 0
    root2 = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0))))
    res2 = sol.minCameraCover(root2)
    assert res2 == 2, f"Expected 2, got {res2}"
    print("LC 968 (Binary Tree Cameras) verified successfully!")

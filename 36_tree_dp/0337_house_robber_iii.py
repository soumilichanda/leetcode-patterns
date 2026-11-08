"""
LeetCode 337: House Robber III
Difficulty: Medium
Pattern: Cluster 36 — Tree Dynamic Programming (Two-State State Transitions)

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height
"""

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            """Returns (rob_this_node, skip_this_node)"""
            if not node:
                return (0, 0)

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # If we rob this node, children must be skipped
            rob_curr = node.val + left_skip + right_skip

            # If we skip this node, children can either be robbed or skipped
            skip_curr = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob_curr, skip_curr)

        return max(dfs(root))


if __name__ == "__main__":
    # Tree: [3, 2, 3, None, 3, None, 1] -> Expected: 7 (3 + 3 + 1)
    t1 = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    sol = Solution()
    assert sol.rob(t1) == 7

    # Tree: [3, 4, 5, 1, 3, None, 1] -> Expected: 9 (4 + 5)
    t2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    assert sol.rob(t2) == 9
    print("LC 337 verified successfully!")

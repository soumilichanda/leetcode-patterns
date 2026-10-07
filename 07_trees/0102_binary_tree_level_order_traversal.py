"""
LeetCode 102: Binary Tree Level Order Traversal
Difficulty: Medium
Pattern: Trees (Breadth-First Search with Level Snapshot Queue)

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result: List[List[int]] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_size = len(queue)
            current_level: List[int] = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            result.append(current_level)

        return result


if __name__ == "__main__":
    # Test Tree: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    levels = sol.levelOrder(root)

    print("=== LC 102: Level Order Traversal ===")
    print(f"Levels: {levels}")
    print("Expected: [[3], [9, 20], [15, 7]]")

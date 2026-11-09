"""
LeetCode 834: Sum of Distances in Tree
Difficulty: Hard
Pattern: Tree DP / Two-Pass Tree Re-rooting

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        count = [1] * n
        ans = [0] * n

        # Pass 1: Post-order traversal to compute subtree sizes and root (0) distance sum
        def dfs_post(node: int, parent: int) -> None:
            for child in tree[node]:
                if child != parent:
                    dfs_post(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        # Pass 2: Pre-order traversal to re-root to each child in O(1)
        def dfs_pre(node: int, parent: int) -> None:
            for child in tree[node]:
                if child != parent:
                    # Reroot from node to child
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs_pre(child, node)

        dfs_post(0, -1)
        dfs_pre(0, -1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    out = sol.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
    assert out == [8, 12, 6, 10, 10, 10], f"Unexpected output: {out}"
    print("LC 834 (Sum of Distances in Tree) verified successfully!")

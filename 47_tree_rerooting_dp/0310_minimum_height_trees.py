"""
LeetCode 310: Minimum Height Trees
Difficulty: Medium
Pattern: Cluster 47 — Topological Leaf-Peeling Centroid DP

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return list(range(n))

        adj: list[set[int]] = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque(i for i in range(n) if len(adj[i]) == 1)
        remaining = n

        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)


if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])) == [1]
    assert sorted(sol.findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])) == [3, 4]
    print("LC 310 verified successfully!")

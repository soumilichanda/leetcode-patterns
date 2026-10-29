"""
LeetCode 684: Redundant Connection
Difficulty: Medium
Pattern: Disjoint Set Union (DSU / Union-Find) with Path Compression & Rank

Time Complexity: O(E * alpha(V)) ≈ O(E)
Space Complexity: O(V)
"""

from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]

        return []


if __name__ == "__main__":
    sol = Solution()
    print("LC 684 Test 1:", sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2, 3]
    print("LC 684 Test 2:", sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # [1, 4]

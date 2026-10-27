"""
LeetCode 1584: Min Cost to Connect All Points
Difficulty: Medium
Pattern: Kruskal's Minimum Spanning Tree (MST) + DSU

Time Complexity: O(N^2 log N)
Space Complexity: O(N^2)
"""

from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))

        edges.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        total_cost = 0
        edges_used = 0

        for dist, u, v in edges:
            if uf.union(u, v):
                total_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break

        return total_cost

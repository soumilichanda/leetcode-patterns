"""
LeetCode 547: Number of Provinces
Difficulty: Medium
Pattern: Disjoint Set Union (Connected Component Counting)

Time Complexity: O(n^2 * alpha(n))
Space Complexity: O(n)
"""

from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.components = size

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

        self.components -= 1
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.components


if __name__ == "__main__":
    sol = Solution()
    print("LC 547 Test 1:", sol.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
    print("LC 547 Test 2:", sol.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))  # 3

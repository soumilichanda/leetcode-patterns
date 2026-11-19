"""
LeetCode 834: Sum of Distances in Tree
Difficulty: Hard
Pattern: Cluster 47 — Two-Pass Tree Rerooting DP

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        adj: dict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = [1] * n
        ans = [0] * n

        def post_order(node: int, parent: int) -> None:
            for child in adj[node]:
                if child != parent:
                    post_order(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def pre_order(node: int, parent: int) -> None:
            for child in adj[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    pre_order(child, node)

        post_order(0, -1)
        pre_order(0, -1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert sol.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == [8, 12, 6, 10, 10, 10]
    assert sol.sumOfDistancesInTree(1, []) == [0]
    print("LC 834 verified successfully!")

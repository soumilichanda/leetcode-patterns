"""
LeetCode 943: Find the Shortest Superstring
Difficulty: Hard
Pattern: Cluster 46 — Traveling Salesperson Bitmask DP with Path Reconstruction

Time Complexity: O(n^2 * 2^n + n^2 * L)
Space Complexity: O(n * 2^n)
"""

from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlap = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                max_k = min(len(words[i]), len(words[j]))
                for k in range(max_k, 0, -1):
                    if words[i].endswith(words[j][:k]):
                        overlap[i][j] = k
                        break

        num_masks = 1 << n
        dp = [[-1] * n for _ in range(num_masks)]
        parent = [[-1] * n for _ in range(num_masks)]

        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1, num_masks):
            for last in range(n):
                if dp[mask][last] < 0:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    next_mask = mask | (1 << nxt)
                    cand = dp[mask][last] + overlap[last][nxt]
                    if cand > dp[next_mask][nxt]:
                        dp[next_mask][nxt] = cand
                        parent[next_mask][nxt] = last

        full_mask = num_masks - 1
        curr = max(range(n), key=lambda i: dp[full_mask][i])

        order: List[int] = []
        mask = full_mask
        while curr != -1:
            order.append(curr)
            prev = parent[mask][curr]
            mask ^= 1 << curr
            curr = prev
        order.reverse()

        res = [words[order[0]]]
        for idx in range(1, n):
            prev_w, curr_w = order[idx - 1], order[idx]
            ov = overlap[prev_w][curr_w]
            res.append(words[curr_w][ov:])

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    assert sol.shortestSuperstring(["alex", "loves", "leetcode"]) == "alexlovesleetcode"
    res2 = sol.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])
    assert len(res2) == 16 and res2 == "gctaagttcatgcatc"
    print("LC 943 verified successfully!")

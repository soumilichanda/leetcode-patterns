"""
LeetCode 688: Knight Probability in Chessboard
Difficulty: Medium
Pattern: Markov State DP (2D Grid Transition Probability Distribution)

Time Complexity: O(k * n^2)
Space Complexity: O(n^2)
"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = (
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1),
        )

        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            next_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    prob = dp[r][c]
                    if prob == 0.0:
                        continue
                    step_prob = prob / 8.0
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            next_dp[nr][nc] += step_prob
            dp = next_dp

        return sum(sum(r_vals) for r_vals in dp)

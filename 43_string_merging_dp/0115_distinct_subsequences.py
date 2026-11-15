"""
LeetCode 115: Distinct Subsequences
Difficulty: Hard
Pattern: Cluster 43 — Dynamic Programming / Combinatorial Subsequence Counting

Time Complexity: O(m * n)
Space Complexity: O(n) auxiliary space via backward-sweeping 1D DP
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if n > m:
            return 0
        if n == 0:
            return 1

        # dp[j] = number of distinct subsequences of s[:i] equal to t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            # Sweep j backward so dp[j - 1] strictly reflects state (i - 1, j - 1)
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.numDistinct("rabbbit", "rabbit") == 3
    assert sol.numDistinct("babgbag", "bag") == 5
    assert sol.numDistinct("abc", "abcd") == 0
    print("LC 115 (Distinct Subsequences) verified successfully!")

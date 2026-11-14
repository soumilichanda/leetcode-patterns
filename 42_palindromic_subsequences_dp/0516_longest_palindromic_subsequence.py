"""
LeetCode 516: Longest Palindromic Subsequence
Difficulty: Medium
Pattern: Cluster 42 — Dynamic Programming / Diagonal Interval DP (Space-Compressed)

Time Complexity: O(n^2)
Space Complexity: O(n) auxiliary space via 1D rolling row + diagonal state register
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        if s == s[::-1]:
            return n

        # dp[j] represents the LPS length for substring s[i...j] at outer iteration i
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            prev_diag = 0  # Stores dp[i + 1][j - 1] before overwrite
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp

        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindromeSubseq("bbbab") == 4
    assert sol.longestPalindromeSubseq("cbbd") == 2
    assert sol.longestPalindromeSubseq("a") == 1
    assert sol.longestPalindromeSubseq("racecar") == 7
    print("LC 516 (Longest Palindromic Subsequence) verified successfully!")

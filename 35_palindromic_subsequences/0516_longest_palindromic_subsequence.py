"""
LeetCode 516: Longest Palindromic Subsequence
Difficulty: Medium
Pattern: Cluster 35 — Interval Dynamic Programming

Time Complexity: O(n^2)
Space Complexity: O(n) space-compressed
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        if s == s[::-1]:
            return n

        # dp[j] stores longest palindromic subsequence for substring s[i...j]
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1
            prev_diagonal = 0  # Represents dp[i+1][j-1]
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev_diagonal + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diagonal = temp

        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindromeSubseq("bbbab") == 4
    assert sol.longestPalindromeSubseq("cbbd") == 2
    print("LC 516 verified successfully!")

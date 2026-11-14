"""
LeetCode 1312: Minimum Insertion Steps to Make a String Palindrome
Difficulty: Hard
Pattern: Cluster 42 — Dynamic Programming / LPS Duality & Dual-End Alignment

Time Complexity: O(n^2)
Space Complexity: O(n) auxiliary space
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s == s[::-1]:
            return 0

        # Compute Longest Palindromic Subsequence length in O(n) space
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            prev_diag = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp

        lps_length = dp[n - 1]
        return n - lps_length


if __name__ == "__main__":
    sol = Solution()
    assert sol.minInsertions("zzazz") == 0
    assert sol.minInsertions("mbadm") == 2
    assert sol.minInsertions("leetcode") == 5
    print("LC 1312 (Minimum Insertion Steps to Make a String Palindrome) verified successfully!")

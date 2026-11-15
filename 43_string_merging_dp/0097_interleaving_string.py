"""
LeetCode 97: Interleaving String
Difficulty: Medium
Pattern: Cluster 43 — Dynamic Programming / Dual-Prefix String Merging (1D Space-Compressed)

Time Complexity: O(m * n)
Space Complexity: O(min(m, n)) auxiliary space via 1D rolling boolean array
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # Ensure s2 is the shorter string to minimize rolling array footprint
        if n > m:
            s1, s2 = s2, s1
            m, n = n, m

        dp = [False] * (n + 1)
        dp[0] = True

        # Initialize first row (using only s2 prefixes)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Transition across s1 prefixes
        for i in range(1, m + 1):
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                match_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                match_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = match_s1 or match_s2

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert sol.isInterleave("", "", "") is True
    print("LC 97 (Interleaving String) verified successfully!")

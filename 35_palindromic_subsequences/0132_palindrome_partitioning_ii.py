"""
LeetCode 132: Palindrome Partitioning II
Difficulty: Hard
Pattern: Cluster 35 — Dynamic Programming / Center Expansion Cuts

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if not s or s == s[::-1]:
            return 0

        # cuts[i] = minimum cuts needed for prefix s[0...i]
        cuts = list(range(n))

        for i in range(n):
            # Odd length center expansion: s[i-d ... i+d]
            d = 0
            while i - d >= 0 and i + d < n and s[i - d] == s[i + d]:
                prev_cuts = cuts[i - d - 1] + 1 if i - d > 0 else 0
                cuts[i + d] = min(cuts[i + d], prev_cuts)
                d += 1

            # Even length center expansion: s[i-d ... i+1+d]
            d = 0
            while i - d >= 0 and i + 1 + d < n and s[i - d] == s[i + 1 + d]:
                prev_cuts = cuts[i - d - 1] + 1 if i - d > 0 else 0
                cuts[i + 1 + d] = min(cuts[i + 1 + d], prev_cuts)
                d += 1

        return cuts[n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minCut("aab") == 1
    assert sol.minCut("a") == 0
    assert sol.minCut("ab") == 1
    print("LC 132 verified successfully!")

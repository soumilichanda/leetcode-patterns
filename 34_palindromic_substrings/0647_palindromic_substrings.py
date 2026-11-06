"""
LeetCode 647: Palindromic Substrings
Difficulty: Medium
Pattern: Cluster 34 — Dynamic Programming / Substring Centers

Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        total_palindromes = 0

        def count_expanding(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            total_palindromes += count_expanding(i, i)      # Odd-length centers
            total_palindromes += count_expanding(i, i + 1)  # Even-length centers

        return total_palindromes


if __name__ == "__main__":
    sol = Solution()
    assert sol.countSubstrings("abc") == 3
    assert sol.countSubstrings("aaa") == 6
    print("LC 647 verified successfully!")

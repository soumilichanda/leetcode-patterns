"""
LeetCode 5: Longest Palindromic Substring
Difficulty: Medium
Pattern: Cluster 34 — Dynamic Programming / Two-Pointer Center Expansion

Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary space
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of palindrome found: (right - 1) - (left + 1) + 1
            return right - left - 1

        for i in range(len(s)):
            len_odd = expand_around_center(i, i)
            len_even = expand_around_center(i, i + 1)
            current_max = max(len_odd, len_even)

            if current_max > max_len:
                max_len = current_max
                # Map center coordinate back to starting index
                start = i - (current_max - 1) // 2

        return s[start : start + max_len]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    print("LC 5 verified successfully!")

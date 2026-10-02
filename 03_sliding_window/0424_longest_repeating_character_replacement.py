"""
LeetCode 424: Longest Repeating Character Replacement

Difficulty: Medium
Pattern: Sliding Window (Dynamic Window with Max Frequency Invariant)

Time Complexity: O(n)
Space Complexity: O(26) = O(1) auxiliary space
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: dict[str, int] = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            # Window length minus max frequency yields characters that must be replaced.
            # If replacements exceed k, shrink the window from the left.
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    test_s1, test_k1 = "ABAB", 2
    test_s2, test_k2 = "AABABBA", 1

    print("=== LeetCode 424: Longest Repeating Character Replacement ===")
    print(f"s='{test_s1}', k={test_k1} -> {sol.characterReplacement(test_s1, test_k1)} (Expected: 4)")
    print(f"s='{test_s2}', k={test_k2} -> {sol.characterReplacement(test_s2, test_k2)} (Expected: 4)")
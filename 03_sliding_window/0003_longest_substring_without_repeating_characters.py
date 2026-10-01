"""
LeetCode 3: Longest Substring Without Repeating Characters
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Pattern: Variable-Length Sliding Window (Last-Seen Hash Map)

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is character set size, n is string length
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    test_str = "abcabcbb"
    print(f"Longest Substring Length: {sol.lengthOfLongestSubstring(test_str)}")  # Expected: 3
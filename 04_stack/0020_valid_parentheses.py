"""
LeetCode 20: Valid Parentheses
Difficulty: Easy
Pattern: Stack (LIFO Matching with Hash Map)

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else "#"
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


if __name__ == "__main__":
    sol = Solution()
    test_cases = ["()[]{}", "(]", "([)]", "{[]}", "]", "((("]
    print("=== LC 20: Valid Parentheses Verification ===")
    for test in test_cases:
        print(f"Input: {test:<8} -> Valid: {sol.isValid(test)}")